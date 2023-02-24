from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent
from nonebot.params import CommandArg
import datetime
atc=on_command('atc', priority=1)
preatc=on_command('preatc', priority=1)

@atc.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res=await get_atc()
    await atc.finish(res)

@preatc.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res=await get_preatc()
    await preatc.finish(res)

async def get_atc():
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回 cf 的 API
    # response=requests.get("https://atcoder.jp/contests/")
    # res=response.text
    f=open('atc.txt','r',encoding='utf-8')
    res=f.read()
    f.close()
    ans=""
    pos=res.find("upcoming",0)
    last=pos
    endpos=res.find("recent",0)
    res=res[pos:endpos]
    pos=0
    last=0
    cnt=0
    while(1):
        pos=res.find("fixtime-full",pos)
        if pos==-1: break
        pos=res.find(">",pos)
        pos+=1
        last=res.find("+",pos)
        dt=res[pos:last]
        t_now=datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
        t_now-=datetime.timedelta(hours=1)
        dt=datetime.datetime.strftime(t_now,'%Y-%m-%d %H:%M:%S')
        pos=res.find("contest",pos)
        pos-=1
        last=res.find("\"",pos)
        contest_id=res[pos:last]
        pos+=1
        pos=res.find("/",pos)
        pos+=1
        name=res[pos:last]
        s="比赛名称："+name+"\n"
        s+="比赛时间："+dt+"\n"
        s+="比赛链接："+"https://atcoder.jp"+contest_id
        if ans=="": ans=s
        else: ans=ans+"\n"+s
        cnt+=1
        if cnt==3: break
    if cnt==0: return "没有找到要开始的 atc 比赛哦"
    return "找到最近的 "+str(cnt)+" 场 atc 比赛为：\n"+ans

async def get_preatc():
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回 cf 的 API
    # response=requests.get("https://atcoder.jp/contests/")
    # res=response.text
    f=open('atc.txt','r',encoding='utf-8')
    res=f.read()
    f.close()
    ans=""
    pos=res.find("recent",0)
    last=pos
    # endpos=res.find("recent",0)
    res=res[pos:]
    pos=0
    last=0
    cnt=0
    while(1):
        pos=res.find("fixtime-full",pos)
        if pos==-1: break
        pos=res.find(">",pos)
        pos+=1
        last=res.find("+",pos)
        dt=res[pos:last]
        t_now=datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
        t_now-=datetime.timedelta(hours=1)
        dt=datetime.datetime.strftime(t_now,'%Y-%m-%d %H:%M:%S')
        pos=res.find("contest",pos)
        pos-=1
        last=res.find("\"",pos)
        contest_id=res[pos:last]
        pos+=1
        pos=res.find("/",pos)
        pos+=1
        name=res[pos:last]
        s="比赛名称："+name+"\n"
        s+="比赛时间："+dt+"\n"
        s+="比赛链接："+"https://atcoder.jp"+contest_id
        if ans=="": ans=s
        else: ans=s+"\n"+ans
        cnt+=1
        if cnt==3: break
    if cnt==0: return "居然找不到，可能是：\n1. bot裂了\n2. 网站裂了\n3. 缓存裂了\n4. 地球裂了"
    return "找到之前的 "+str(cnt)+" 场 atc 比赛为：\n"+ans