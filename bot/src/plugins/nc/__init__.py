from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent
from nonebot.params import CommandArg
import datetime
nc=on_command('nc', priority=1)
prenc=on_command('prenc', priority=1)

@nc.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res=await get_nowcoder()
    await nc.finish(res)

@prenc.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res=await get_prenowcoder()
    await prenc.finish(res)

async def get_nowcoder():
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回 cf 的 API
    time_now=datetime.date.today()
    # response=requests.get("https://ac.nowcoder.com/acm/contest/vip-index")
    # res=response.text
    f=open('nc.txt','r',encoding='utf-8')
    res=f.read()
    f.close()
    ans=""
    pos=res.find("js-current")
    last=pos
    endpos=res.find("js-end")
    res=res[pos:endpos]
    pos=0
    last=0
    cnt=0
    while(1):
        pos=res.find("data-id",last)
        if pos==-1: break
        pos+=9
        last=res.find("\"",pos)
        contest_id=res[pos:last]
        pos=res.find("platform-item-cont",pos)
        pos=res.find("_blank",pos)
        pos+=8
        last=res.find("<",pos)
        name=res[pos:last]
        pos=res.find("比赛时间",pos)
        pos+=9
        last=res.find("至",pos)
        last-=2
        dt=res[pos:last]
        start_time=datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M')
        s="比赛名称："+name+"\n"
        s+="比赛时间："+dt+"\n"
        s+="比赛链接："+"https://ac.nowcoder.com/acm/contest/"+contest_id
        if time_now.__le__(start_time):
            if ans=="": ans=s
            else: ans=ans+"\n"+s
            cnt+=1
        if cnt==3: break
    if cnt==0: return "没有找到要开始的牛客比赛哦"
    return "找到最近的 "+str(cnt)+" 场牛客比赛为：\n"+ans

async def get_prenowcoder():
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回 cf 的 API
    # time_now=datetime.date.today()
    # response=requests.get("https://ac.nowcoder.com/acm/contest/vip-index")
    # res=response.text
    f=open('nc.txt','r',encoding='utf-8')
    res=f.read()
    f.close()
    ans=""
    pos=res.find("js-end")
    last=pos
    # endpos=res.find("js-end")
    res=res[pos:]
    pos=0
    last=0
    cnt=0
    while(1):
        pos=res.find("data-id",last)
        if pos==-1: break
        pos+=9
        last=res.find("\"",pos)
        contest_id=res[pos:last]
        pos=res.find("platform-item-cont",pos)
        pos=res.find("_blank",pos)
        pos+=8
        last=res.find("<",pos)
        name=res[pos:last]
        pos=res.find("比赛时间",pos)
        pos+=9
        last=res.find("至",pos)
        last-=2
        dt=res[pos:last]
        start_time=datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M')
        s="比赛名称："+name+"\n"
        s+="比赛时间："+dt+"\n"
        s+="比赛链接："+"https://ac.nowcoder.com/acm/contest/"+contest_id
        # if time_now.__le__(start_time):
        if ans=="": ans=s
        else: ans=s+"\n"+ans
        cnt+=1
        if cnt==3: break
    if cnt==0: return "居然找不到，可能是：\n1. bot裂了\n2. 网站裂了\n3. 缓存裂了\n4. 地球裂了"
    return "找到之前的 "+str(cnt)+" 场牛客比赛为：\n"+ans