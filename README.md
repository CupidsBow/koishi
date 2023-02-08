# koishi

基于 [nonebot2](https://github.com/nonebot/nonebot2) 与 [gocqhttp](https://github.com/Mrs4s/go-cqhttp) 的 QQ 机器人。

# 功能

- cf/precf 返回最近 / 之前最多 3 场次 codeforces 赛事。
- atc/preatc 返回最近 / 之前最多 3 场次 atcoder 赛事。
- nc/prenc 返回最近 / 之前最多 3 场次牛客赛事。
- today 返回当天相关比赛事赛。
- next 返回最近的下一场次赛事。
- update 手动更新数据。
- help 返回指令。
- 早上 8 点 1 分自动在每个群播报当天相关赛事（直接拉进群就可以了）。
- 每个整点 30 分更新本地数据，成功发送消息 '更新成功' 。（嫌太频繁可以手动改一下 schedule 插件里的时间）
- 自动同意好友和拉群。

# 如何使用

.env.dev 文件加超管，不加也没事。\
schedule 插件添加「更新数据」的消息接收方。\
cmd 跑 bot.py，再跑 gocqhttp。

# 特别感谢

- [nonebot2](https://github.com/nonebot/nonebot2)
- [gocqhttp](https://github.com/Mrs4s/go-cqhttp)
- [BruceKZ](https://github.com/BruceKZ)

# 题外话

~~因为自己比较懒~~因为自己号经常风控 bot 挂不了在服务器上所以发在这里，不确定有没有人需要。\
最多返回 3 场次是感觉这样不至于太刷屏(¿)。\
单个插件只把插件文件夹拷下来就可以了。\
最开始搭只是想提醒自己每周六的 abc 。\
屎山代码轻喷。\
联系 QQ: 1143957699。\
代码有错误或者代码里有信息没删干净欢迎联系。
