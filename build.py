#!/usr/bin/env python3
"""国内直连纯域名合并脚本：下载各开源规则库 -> 清洗 -> 去重 -> 输出两个 TXT。
用法: python3 build.py   (输出到本脚本所在目录的 output/)
"""
import os, re, sys, json, time, datetime, urllib.request, concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.getcwd()

LS = "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/"
BM = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/"
SOURCES = [  # (名称, URL, 格式)
    ("Loyalsoldier direct-list", LS + "direct-list.txt", "plain"),
    ("Loyalsoldier china-list", LS + "china-list.txt", "plain"),
    ("blackmatrix7 China_Domain", BM + "China/China_Domain.list", "auto"),
    ("blackmatrix7 ChinaMax_Domain", BM + "ChinaMax/ChinaMax_Domain.list", "auto"),
    ("blackmatrix7 Direct", BM + "Direct/Direct.list", "auto"),
    ("felixonmars accelerated-domains.china", "https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf", "dnsmasq"),
    ("ACL4SSR ChinaDomain", "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaDomain.list", "auto"),
    ("Loyalsoldier clash-rules direct", "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt", "auto"),
]
LAZY = "https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy.conf"

DOM = re.compile(r"^(?=.{1,253}$)([a-z0-9_]([a-z0-9_-]{0,61}[a-z0-9])?\.)*[a-z0-9_]([a-z0-9_-]{0,61}[a-z0-9])?$")
IPV4 = re.compile(r"^\d+(\.\d+){3}$")
RULE_TYPES = {"DOMAIN", "DOMAIN-SUFFIX", "HOST", "HOST-SUFFIX"}


JSD_HOSTS = ["cdn", "fastly", "testingcf", "gcore"]  # jsDelivr 镜像，按顺序尝试


def jsdelivr(url):
    m = re.match(r"https?://raw\.githubusercontent\.com/([^/]+)/([^/]+)/(?:refs/heads/)?([^/]+)/(.+)", url)
    if not m:
        return []
    path = f"gh/{m.group(1)}/{m.group(2)}@{m.group(3)}/{m.group(4)}"
    return [f"https://{h}.jsdelivr.net/{path}" for h in JSD_HOSTS]


def fetch(url, tries=3):
    """先下 raw.githubusercontent.com，失败则依次改用 jsDelivr 镜像。"""
    errs = []
    for i, u in enumerate([url] + jsdelivr(url)):
        try:
            return _fetch(u, tries if i == 0 else 2)
        except Exception as e:
            errs.append(f"{u.split('/')[2]}: {e}")
    raise RuntimeError("; ".join(errs))


def _fetch(url, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 china-direct-build"})
            with urllib.request.urlopen(req, timeout=60) as r:
                t = r.read().decode("utf-8", "ignore")
            if not t.strip():
                raise RuntimeError("empty response")
            return t
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{type(last).__name__}: {last}")


def clean(d):
    d = d.strip().strip("'\"").lower()
    for p in ("full:", "domain:", "+."):
        if d.startswith(p):
            d = d[len(p):]
    d = d.lstrip(".*").rstrip(".")
    if not d or "." not in d or IPV4.match(d) or not DOM.match(d):
        return None
    return d


def parse(text, fmt, direct_only=False):
    out = []
    for raw in text.splitlines():
        l = raw.split("#")[0].strip() if fmt != "rules" else raw.strip()
        if not l or l[0] in "#!;[":
            continue
        if fmt == "dnsmasq":
            m = re.match(r"server=/([^/]+)/", l)
            if m and (d := clean(m.group(1))):
                out.append(d)
            continue
        if l.startswith("- "):  # clash payload yaml
            l = l[2:].strip().strip("'\"")
        if l.startswith(("regexp:", "keyword:", "payload:")):
            continue
        if "," in l:
            p = [x.strip() for x in l.split(",")]
            if p[0].upper() not in RULE_TYPES or len(p) < 2:
                continue  # DOMAIN-KEYWORD / IP-CIDR / GEOIP / USER-AGENT 等丢弃
            if direct_only and (len(p) < 3 or p[2].upper() != "DIRECT"):
                continue
            d = clean(p[1])
        else:
            if fmt == "rules":
                continue
            d = clean(l.split()[0])
        if d:
            out.append(d)
    return out


def main():
    results, failed, retry, urls = {}, [], [], {"LOWERTOP lazy.conf 内联 DIRECT": LAZY}
    jobs = list(SOURCES)
    # LOWERTOP lazy.conf：动态解析 RULE-SET ...,DIRECT 与内联 DIRECT 行
    try:
        lazy = fetch(LAZY)
        results["LOWERTOP lazy.conf 内联 DIRECT"] = parse(lazy, "rules", direct_only=True)
        for l in lazy.splitlines():
            p = [x.strip() for x in l.strip().split(",")]
            if len(p) >= 3 and p[0].upper() == "RULE-SET" and p[2].upper() == "DIRECT":
                jobs.append((f"LOWERTOP RULE-SET {p[1].rsplit('/', 1)[-1]}", p[1], "auto"))
    except Exception as e:
        failed.append(f"LOWERTOP lazy.conf ({e})")

    with cf.ThreadPoolExecutor(8) as ex:
        futs = {ex.submit(fetch, u): (n, f, u) for n, u, f in jobs}
        for fu in cf.as_completed(futs):
            n, f, _ = futs[fu]
            urls[n] = futs[fu][2]
            try:
                results[n] = parse(fu.result(), f)
            except Exception as e:
                retry.append((n, futs[fu][2], f, e))

    # 第二轮：镜像偶发 503 时稍等再试一次
    if retry:
        time.sleep(15)
    for n, u, f, e in retry:
        try:
            results[n] = parse(fetch(u), f)
        except Exception as e2:
            failed.append(f"{n} ({e2})")

    full = set()
    for v in results.values():
        full.update(v)
    keep = set()
    for d in sorted(full, key=lambda x: x.count(".")):
        parts = d.split(".")
        if not any(".".join(parts[i:]) in keep for i in range(1, len(parts))):
            keep.add(d)

    with open(os.path.join(OUT, "china-direct-domains.txt"), "w") as f:
        f.write("\n".join(sorted(keep)) + "\n")
    with open(os.path.join(OUT, "china-direct-domains-full.txt"), "w") as f:
        f.write("\n".join(sorted(full)) + "\n")

    if len(full) < 50000:
        raise SystemExit(f"Too few domains ({len(full)}), aborting. Failed: {failed}")
    upd = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
    stats = {"updated": upd.strftime("%Y-%m-%d %H:%M CST"), "full": len(full), "compact": len(keep),
             "sources": {k: len(v) for k, v in sorted(results.items())}, "failed": failed}
    json.dump(stats, open(os.path.join(OUT, "stats.json"), "w"), ensure_ascii=False, indent=2)
    write_readme(stats, urls, [n for n, _, _ in jobs] + ["LOWERTOP lazy.conf 内联 DIRECT"])
    print(json.dumps(stats, ensure_ascii=False, indent=1))


def page(url):
    m = re.match(r"https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/(.+)", url)
    if not m:
        return url, url, url
    o, r, b, p = m.groups()
    return f"{o}/{r}", f"https://github.com/{o}/{r}", f"https://github.com/{o}/{r}/blob/{b}/{p}"


def write_readme(st, urls, order):
    RAW = "https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/"
    failed_names = {x.split(" (")[0] for x in st["failed"]}
    L = ["# china-direct-domain", "",
         "合并多个开源规则库的国内直连域名，去掉前缀、正则、关键词和 IP 类规则，统一小写、校验格式后去重，输出一行一个的纯域名。每天北京时间 02:30 由 GitHub Actions 自动更新。", "",
         f"最近更新：{st['updated']}　上游来源：{len(order)} 个（成功 {len(order) - len(failed_names)}，失败 {len(failed_names)}）", "",
         "## 文件", "",
         "| 文件 | 说明 | 条数 | 链接 |", "| --- | --- | ---: | --- |",
         f"| china-direct-domains.txt | 精简版（父域名已在列表时去掉子域名） | {st['compact']:,} | [raw]({RAW}china-direct-domains.txt) |",
         f"| china-direct-domains-full.txt | 完整去重版 | {st['full']:,} | [raw]({RAW}china-direct-domains-full.txt) |",
         f"| stats.json | 各来源条数与失败来源 | - | [raw]({RAW}stats.json) |", "",
         "## 上游规则库", "",
         "| # | 来源 | 规则库 | 文件 | 有效域名数 | 状态 |", "| ---: | --- | --- | --- | ---: | --- |"]
    for i, n in enumerate(order, 1):
        u = urls.get(n, "")
        repo, home, blob = page(u)
        fname = u.rsplit("/", 1)[-1] if u else "-"
        cnt = st["sources"].get(n)
        status = "⚠️ 下载失败" if n in failed_names else ("正常" if cnt else "无内容")
        L.append(f"| {i} | {n} | [{repo}]({home}) | [{fname}]({blob}) | {cnt or 0:,} | {status} |")
    L += ["", "有效域名数为从该文件解析出的合法域名条数（含与其他来源重叠的部分）。LOWERTOP 的规则集由 lazy.conf 中所有 `RULE-SET ...,DIRECT` 动态解析，lazy.conf 变化时来源会随之增减。", "",
          "## 处理规则", "",
          "- 去掉开头的点和 full: / domain: / +. 前缀",
          "- 丢弃 regexp: / keyword: / DOMAIN-KEYWORD / IP-CIDR / GEOIP / USER-AGENT 等非域名规则",
          "- 统一小写，校验域名格式（需含点，排除纯 IP），去重",
          "- 精简版：父域名已收录时去掉其子域名",
          "- raw.githubusercontent.com 下载失败时自动改用 jsDelivr 镜像，仍失败的来源 15 秒后重试一次",
          "- 某个来源失败时用其余来源继续，失败项写入 stats.json；总数少于 50,000 时本次不提交", ""]
    open(os.path.join(OUT, "README.md"), "w").write("\n".join(L))


if __name__ == "__main__":
    main()
