# china-direct-domain

合并多个开源规则库的国内直连域名，去掉前缀、正则、关键词和 IP 类规则，统一小写、校验格式后去重，输出一行一个的纯域名。每天北京时间 02:30 由 GitHub Actions 自动更新。

最近更新：2026-10-22 22:20（北京时间）

## 文件

| 文件 | 说明 | 条数 | 链接 |
| --- | --- | ---: | --- |
| china-direct-domains.txt | 精简版（父域名已在列表时去掉子域名） | 113,953 | [raw](https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/china-direct-domains.txt) |
| china-direct-domains-full.txt | 完整去重版 | 115,274 | [raw](https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/china-direct-domains-full.txt) |
| stats.json | 本次各来源条数与失败来源 | - | [raw](https://raw.githubusercontent.com/passionsu-su/china-direct-domain/main/stats.json) |

## 上游规则库

| 规则库 | 文件 | 格式 | 本次有效域名数 | 状态 |
| --- | --- | --- | ---: | --- |
| [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat) | direct-list.txt（release 分支） | 纯域名 / full: domain: | 110,518 | 正常 |
| [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat) | china-list.txt（release 分支） | 纯域名 / full: domain: | 109,795 | 正常 |
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Shadowrocket/China) | Shadowrocket/China/China_Domain.list | .域名后缀 | 3,689 | 正常 |
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Shadowrocket/ChinaMax) | Shadowrocket/ChinaMax/ChinaMax_Domain.list | .域名后缀 | 110,695 | 正常 |
| [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Shadowrocket/Direct) | Shadowrocket/Direct/Direct.list | DOMAIN / DOMAIN-SUFFIX 规则 | 195 | 正常 |
| [felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list) | accelerated-domains.china.conf | dnsmasq server=/域名/ | 109,795 | 正常 |
| [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket) | lazy.conf 中所有 RULE-SET ...,DIRECT 规则集（动态解析） | DOMAIN / DOMAIN-SUFFIX / HOST 规则 | 6,183 | 正常 |
| [LOWERTOP/Shadowrocket](https://github.com/LOWERTOP/Shadowrocket/blob/main/lazy.conf) | lazy.conf 内联 DOMAIN/DOMAIN-SUFFIX ...,DIRECT | Shadowrocket 规则 | 0 | 无内容 |

规则数为从该文件解析出的有效域名条数，不同来源间大量重叠，合并去重后见上方文件条数。

## 处理规则

- 去掉开头的点和 full: / domain: 前缀
- 丢弃 regexp: / keyword: / DOMAIN-KEYWORD / IP-CIDR / GEOIP / USER-AGENT 等非域名规则
- 统一小写，校验域名格式，去重
- 精简版：按层级从短到长，父域名已收录时跳过其子域名
- 某个来源下载失败时用其余来源继续，失败项写入 stats.json；总数少于 50,000 时本次不提交
