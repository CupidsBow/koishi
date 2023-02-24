import time
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent
from nonebot.params import CommandArg
cf=on_command('cf', priority=1)
precf=on_command('precf', priority=1)

@cf.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res=await get_cf()
    await cf.finish(res)

@precf.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res=await get_precf()
    await precf.finish(res)

async def get_cf():
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回 cf 的 API
    # response=requests.get("https://codeforces.com/api/contest.list?gym=false")
    # res=json.dumps(response.json())
    f=open('cf.txt','r')
    res=f.read()
    f.close()
    ans=""
    pos=0
    last=0
    cnt=0
    while(1):
        pos=res.find("id",pos)
        pos+=5
        last=res.find(",",pos)
        contest_id=res[pos:last]
        pos=res.find("name",pos)
        pos+=8
        last=res.find("\"",pos)
        name=res[pos:last]
        pos=res.find("phase",last)
        pos+=9
        last=res.find("\"",pos)
        if res[pos:last]!="BEFORE": break
        pos=res.find("startTimeSeconds",last)
        pos+=19
        last=res.find(",",pos)
        timestamp=int(res[pos:last])
        time_local=time.localtime(timestamp)
        dt=time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        s="比赛名称："+name+"\n"
        s+="比赛时间："+dt+"\n"
        s+="比赛链接："+"https://codeforces.com/contest/"+contest_id
        if ans=="": ans=s
        else: ans=s+"\n"+ans
        cnt+=1
    if cnt==0: return "没有找到要开始的 cf 比赛哦"
    i=0
    sum=0
    while i<len(ans):
        if ans[i]=='\n': sum+=1
        if sum==9: break
        i+=1
    ans=ans[0:i]
    return "找到最近的 "+str(min(cnt,3))+" 场 cf 比赛为：\n"+ans

async def get_precf():
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回 cf 的 API
    # response=requests.get("https://codeforces.com/api/contest.list?gym=false")
    # res=json.dumps(response.json())
    f=open('cf.txt','r')
    res=f.read()
    f.close()
    ans=""
    pos=0
    last=0
    cnt=0
    while(1):
        pos=res.find("id",pos)
        pos+=5
        last=res.find(",",pos)
        contest_id=res[pos:last]
        pos=res.find("name",pos)
        pos+=8
        last=res.find("\"",pos)
        name=res[pos:last]
        pos=res.find("phase",last)
        pos+=9
        last=res.find("\"",pos)
        if res[pos:last]!="BEFORE":
            pos=res.find("startTimeSeconds",last)
            pos+=19
            last=res.find(",",pos)
            timestamp=int(res[pos:last])
            time_local=time.localtime(timestamp)
            dt=time.strftime("%Y-%m-%d %H:%M:%S",time_local)
            s="比赛名称："+name+"\n"
            s+="比赛时间："+dt+"\n"
            s+="比赛链接："+"https://codeforces.com/contest/"+contest_id
            if name.find("\\u")!=-1: continue
            if ans=="": ans=s
            else: ans=s+"\n"+ans
            cnt+=1
            if cnt==3: break
    if cnt==0: return "居然找不到，可能是：\n1. bot裂了\n2. 网站裂了\n3. 缓存裂了\n4. 地球裂了"
    i=0
    sum=0
    while i<len(ans):
        if ans[i]=='\n': sum+=1
        if sum==9: break
        i+=1
    ans=ans[0:i]
    return "找到之前的 "+str(min(cnt,3))+" 场 cf 比赛为：\n"+ans