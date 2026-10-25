# china-direct-domain

合并多个开源规则库的国内直连域名，去掉前缀、正则、关键词和 IP 类规则，统一小写、校验格式后去重，输出一行一个的纯域名。每天北京时间 02:30 由 GitHub Actions 自动更新。

最近更新：2026-10-26 03:14 CST　上游来源：21 个（成功 21，失败 0）

## 文件

| 文件 | 说明 | 条数 | 下载 |
| --- | --- | ---: | --- |
| china-direct-domains.txt | 精简版（父域名已在列表时去掉子域名） | 114,389 | [raw](https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/china-direct-domains.txt) · [ghfast](https://ghfast.top/https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/china-direct-domains.txt) · [gh-proxy](https://gh-proxy.com/https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/china-direct-domains.txt) · [jsDelivr-Fastly](https://fastly.jsdelivr.net/gh/passionsu-su/china-direct-domain@main/china-direct-domains.txt) · [jsDelivr-CF](https://testingcf.jsdelivr.net/gh/passionsu-su/china-direct-domain@main/china-direct-domains.txt) |
| china-direct-domains-full.txt | 完整去重版 | 115,316 | [raw](https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/china-direct-domains-full.txt) · [ghfast](https://ghfast.top/https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/china-direct-domains-full.txt) · [gh-proxy](https://gh-proxy.com/https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/china-direct-domains-full.txt) · [jsDelivr-Fastly](https://fastly.jsdelivr.net/gh/passionsu-su/china-direct-domain@main/china-direct-domains-full.txt) · [jsDelivr-CF](https://testingcf.jsdelivr.net/gh/passionsu-su/china-direct-domain@main/china-direct-domains-full.txt) |
| stats.json | 各来源条数与失败来源 | - | [raw](https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/stats.json) · [ghfast](https://ghfast.top/https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/stats.json) · [gh-proxy](https://gh-proxy.com/https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/stats.json) · [jsDelivr-Fastly](https://fastly.jsdelivr.net/gh/passionsu-su/china-direct-domain@main/stats.json) · [jsDelivr-CF](https://testingcf.jsdelivr.net/gh/passionsu-su/china-direct-domain@main/stats.json) |

国内访问：raw 直连不稳定时可用表中镜像。ghfast / gh-proxy 为第三方 GitHub 代理，实时获取最新文件；jsDelivr（Fastly / Cloudflare 节点）有缓存，每次更新后工作流会主动刷新缓存，个别节点可能仍滞后几分钟到数小时。第三方镜像可能随时失效，请多备一个。

## 上游规则库

| # | 来源 | 规则库 | 文件 | 有效域名数 | 状态 |
| ---: | --- | --- | --- | ---: | --- |
| 1 | Loyalsoldier direct-list | [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat) | [direct-list.txt](https://github.com/Loyalsoldier/v2ray-rules-dat/blob/release/direct-list.txt) | 110,191 | 正常 |
| 2 | Loyalsoldier china-list | [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat) | [china-list.txt](https://github.com/Loyalsoldier/v2ray-rules-dat/blob/release/china-list.txt) | 109,507 | 正常 |
| 3 | blackmatrix7 China_Domain | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [China_Domain.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/China/China_Domain.list) | 3,689 | 正常 |
| 4 | blackmatrix7 ChinaMax_Domain | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [ChinaMax_Domain.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/ChinaMax/ChinaMax_Domain.list) | 110,697 | 正常 |
| 5 | blackmatrix7 Direct | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [Direct.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/Direct/Direct.list) | 195 | 正常 |
| 6 | felixonmars accelerated-domains.china | [felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list) | [accelerated-domains.china.conf](https://github.com/felixonmars/dnsmasq-china-list/blob/master/accelerated-domains.china.conf) | 109,507 | 正常 |
| 7 | ACL4SSR ChinaDomain | [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR) | [ChinaDomain.list](https://github.com/ACL4SSR/ACL4SSR/blob/master/Clash/ChinaDomain.list) | 606 | 正常 |
| 8 | Loyalsoldier clash-rules direct | [Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules) | [direct.txt](https://github.com/Loyalsoldier/clash-rules/blob/release/direct.txt) | 110,191 | 正常 |
| 9 | LOWERTOP RULE-SET Apple.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [Apple.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/QuantumultX/Apple/Apple.list) | 1,823 | 正常 |
| 10 | LOWERTOP RULE-SET BiliBili.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [BiliBili.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/BiliBili/BiliBili.list) | 115 | 正常 |
| 11 | LOWERTOP RULE-SET NetEaseMusic.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [NetEaseMusic.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/NetEaseMusic/NetEaseMusic.list) | 10 | 正常 |
| 12 | LOWERTOP RULE-SET Baidu.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [Baidu.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/Baidu/Baidu.list) | 251 | 正常 |
| 13 | LOWERTOP RULE-SET DouBan.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [DouBan.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/DouBan/DouBan.list) | 3 | 正常 |
| 14 | LOWERTOP RULE-SET WeChat.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [WeChat.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/QuantumultX/WeChat/WeChat.list) | 40 | 正常 |
| 15 | LOWERTOP RULE-SET Sina.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [Sina.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/Sina/Sina.list) | 107 | 正常 |
| 16 | LOWERTOP RULE-SET Zhihu.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [Zhihu.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/Zhihu/Zhihu.list) | 2 | 正常 |
| 17 | LOWERTOP RULE-SET XiaoHongShu.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [XiaoHongShu.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/XiaoHongShu/XiaoHongShu.list) | 4 | 正常 |
| 18 | LOWERTOP RULE-SET DouYin.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [DouYin.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/DouYin/DouYin.list) | 13 | 正常 |
| 19 | LOWERTOP RULE-SET China.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [China.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/QuantumultX/China/China.list) | 3,689 | 正常 |
| 20 | LOWERTOP RULE-SET Lan.list | [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) | [Lan.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/Lan/Lan.list) | 124 | 正常 |
| 21 | LOWERTOP lazy.conf 内联 DIRECT | [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket) | [lazy.conf](https://github.com/LOWERTOP/Shadowrocket/blob/main/lazy.conf) | 0 | 无内容 |

有效域名数为从该文件解析出的合法域名条数（含与其他来源重叠的部分）。LOWERTOP 的规则集由 lazy.conf 中所有 `RULE-SET ...,DIRECT` 动态解析，lazy.conf 变化时来源会随之增减。

## 处理规则

- 去掉开头的点和 full: / domain: / +. 前缀
- 丢弃 regexp: / keyword: / DOMAIN-KEYWORD / IP-CIDR / GEOIP / USER-AGENT 等非域名规则
- 统一小写，校验域名格式（需含点，排除纯 IP），去重
- 精简版：父域名已收录时去掉其子域名
- raw.githubusercontent.com 下载失败时自动改用 jsDelivr 镜像，仍失败的来源 15 秒后重试一次
- 某个来源失败时用其余来源继续，失败项写入 stats.json；总数少于 50,000 时本次不提交
