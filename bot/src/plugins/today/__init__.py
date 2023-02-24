import time
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent
from nonebot.params import CommandArg
import datetime

today=on_command('today', priority=1)

@today.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res=await get_today()
    await today.finish(res)

async def get_today():
    time_now=datetime.date.today()
    time_today=datetime.date.today()
    time_now=datetime.datetime.strftime(time_now,'%Y-%m-%d')
    today=0
    # response=requests.get("https://codeforces.com/api/contest.list?gym=false")
    # res=json.dumps(response.json())
    f=open('cf.txt','r')
    res=f.read()
    f.close()
    get_cf=""
    cnt_cf=0
    pos=0
    last=0
    while(1):
        pos=res.find("id",pos)
        if pos==-1: break
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
        today=time.strftime("%Y-%m-%d",time_local)
        if today==time_now:
            s="比赛名称："+name+"\n"
            s+="比赛时间："+dt+"\n"
            s+="比赛链接："+"https://codeforces.com/contest/"+contest_id
            if get_cf=="": get_cf=s
            else: get_cf=s+'\n'+get_cf
            cnt_cf+=1
    # if cnt_cf!=0 and int(today)!=int(time_now): cnt_cf=0
    
    
    # response=requests.get("https://atcoder.jp/contests/")
    # res=response.text
    f=open('atc.txt','r',encoding='utf-8')
    res=f.read()
    f.close()
    get_atc=""
    pos=res.find("upcoming",0)
    last=pos
    endpos=res.find("recent",0)
    res=res[pos:endpos]
    pos=0
    last=0
    cnt_atc=0
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
        today=datetime.datetime.strftime(t_now,'%Y-%m-%d')
        if today==time_now:
            s="比赛名称："+name+"\n"
            s+="比赛时间："+dt+"\n"
            s+="比赛链接："+"https://atcoder.jp"+contest_id
            if get_atc=="": get_atc=s
            else: get_atc+='\n'+s
            cnt_atc+=1
        else: break
    # if cnt_atc!=0 and int(today)!=int(time_now): cnt_atc=0
    
    
    # response=requests.get("https://ac.nowcoder.com/acm/contest/vip-index")
    # res=response.text
    f=open('nc.txt','r',encoding='utf-8')
    res=f.read()
    f.close()
    get_nowcoder=""
    pos=res.find("js-current")
    last=pos
    endpos=res.find("js-end")
    res=res[pos:endpos]
    pos=0
    last=0
    cnt_nowcoder=0
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
        if time_today.__le__(start_time):
            today=datetime.datetime.strftime(start_time,'%Y-%m-%d')
            if today==time_now:
                s="比赛名称："+name+"\n"
                s+="比赛时间："+dt+"\n"
                s+="比赛链接："+"https://ac.nowcoder.com/acm/contest/"+contest_id
                if get_nowcoder=="": get_nowcoder=s
                else: get_nowcoder+='\n'+s
                cnt_nowcoder+=1
            else: break
    # if cnt_nowcoder!=0 and int(today)!=int(time_now): cnt_nowcoder=0
    
    
    ans=""
    if cnt_cf+cnt_atc+cnt_nowcoder==0: return '今天没有比赛哦 =￣ω￣='
    else:
        if cnt_cf!=0:
            ans=ans+"\n"+get_cf
        if cnt_atc!=0:
            ans=ans+"\n"+get_atc
        if cnt_nowcoder!=0:
            ans=ans+"\n"+get_nowcoder
        return '找到今天的比赛如下：'+ans