#!/usr/bin/env python3
"""Turn china-direct-domains.txt (one bare domain per line, suffix intent)
into ready-to-use rule-set files for proxy clients. Every entry means
"this domain and all its subdomains".

rules/clash.yaml          Clash / Clash Premium / mihomo / Stash rule-provider
                          (behavior: domain, format: yaml, '+.' = domain + subdomains)
rules/surge-domainset.txt Surge / Loon DOMAIN-SET (leading '.' = domain + subdomains)
rules/singbox.json        sing-box source rule-set (domain_suffix)
"""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
doms = [l.strip() for l in open(os.path.join(ROOT, "china-direct-domains.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")]
if len(doms) < 50000:
    raise SystemExit(f"only {len(doms)} domains, refusing to write rule sets")
os.makedirs(os.path.join(ROOT, "rules"), exist_ok=True)
with open(os.path.join(ROOT, "rules/clash.yaml"), "w", encoding="utf-8") as f:
    f.write("payload:\n" + "".join(f"  - '+.{d}'\n" for d in doms))
with open(os.path.join(ROOT, "rules/surge-domainset.txt"), "w", encoding="utf-8") as f:
    f.write("".join(f".{d}\n" for d in doms))
with open(os.path.join(ROOT, "rules/singbox.json"), "w", encoding="utf-8") as f:
    json.dump({"version": 2, "rules": [{"domain_suffix": doms}]}, f, ensure_ascii=False, separators=(",", ":"))
print(f"rules/: {len(doms)} domains written in clash, surge and sing-box formats")

# README section (build.py rewrites README each run, so re-append it here).
B = "https://fastly.jsdelivr.net/gh/passionsu-su/china-direct-domain@main/"
sec = ("\n## 代理客户端规则集（rules/）\n\n由精简版生成，每条表示该域名及其所有子域名，随每月更新自动重建。\n\n"
       "| 文件 | 适用客户端 | 用法 |\n| --- | --- | --- |\n"
       f"| rules/clash.yaml | Clash Premium / mihomo / Clash Verge / Stash | rule-providers：behavior: domain，format: yaml，{B}rules/clash.yaml |\n"
       f"| rules/surge-domainset.txt | Surge / Loon | DOMAIN-SET,{B}rules/surge-domainset.txt,DIRECT |\n"
       f"| rules/singbox.json | sing-box 1.10+ | route.rule_set：type remote，format source，{B}rules/singbox.json |\n")
rp = os.path.join(ROOT, "README.md")
txt = open(rp, encoding="utf-8").read()
if "## 代理客户端规则集" in txt:
    txt = txt.split("\n## 代理客户端规则集")[0].rstrip("\n") + "\n"
open(rp, "w", encoding="utf-8").write(txt + sec)
