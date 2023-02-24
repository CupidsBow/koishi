import time
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent
from nonebot.params import CommandArg
import datetime

next=on_command('next', priority=1)

@next.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res=await get_next()
    await next.finish(res)

async def get_next():
    class Contest(object):
        class Struct(object):
            def __init__(self,name,link,time):
                self.name=name
                self.link=link
                self.time=time
        def make_struct(self,name,link,time):
            return self.Struct(name,link,time)
    contest=Contest()
    contest_list=[]
    
    time_now=datetime.date.today()
    time_today=datetime.date.today()
    time_now=str(time_now.day)
    # today=0
    # response=requests.get("https://codeforces.com/api/contest.list?gym=false")
    # res=response.text
    # res=json.dumps(response.json())
    f=open('cf.txt','r')
    res=f.read()
    f.close()
    get_cf=""
    pos=0
    last=0
    cnt_cf=0
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
        time_cf=datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
        # ttt=0
        # ttt=dt.index("-",ttt)
        # ttt+=1
        # ttt=dt.index("-",ttt)
        # ttt+=1
        # eee=dt.index(" ",ttt)
        # today=dt[ttt:eee]
        contest_list.append(contest.make_struct(name,"https://codeforces.com/contest/"+contest_id,time_cf))
        # s="比赛名称："+name+"\n"
        # s+="比赛时间："+dt+"\n"
        # s+="比赛链接："+"https://codeforces.com/contest/"+contest_id
        # get_cf=s
        # cnt_cf+=1
    
    
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
        # ttt=0
        # ttt=dt.index("-",ttt)
        # ttt+=1
        # ttt=dt.index("-",ttt)
        # ttt+=1
        # eee=dt.index(" ",ttt)
        # today=dt[ttt:eee]
        contest_list.append(contest.make_struct(name,"https://atcoder.jp"+contest_id,t_now))
        break
        # s="比赛名称："+name+"\n"
        # s+="比赛时间："+dt+"\n"
        # s+="比赛链接："+"https://atcoder.jp"+contest_id
        # get_atc=s
        # cnt_atc+=1
        # if cnt_atc==1: break
    
    
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
            # ttt=0
            # ttt=dt.index("-",ttt)
            # ttt+=1
            # ttt=dt.index("-",ttt)
            # ttt+=1
            # eee=dt.index(" ",ttt)
            # today=dt[ttt:eee]
            contest_list.append(contest.make_struct(name,"https://ac.nowcoder.com/acm/contest/"+contest_id,start_time))
            break
            # s="比赛名称："+name+"\n"
            # s+="比赛时间："+dt+"\n"
            # s+="比赛链接："+"https://ac.nowcoder.com/acm/contest/"+contest_id
            # get_nowcoder=s
            # cnt_nowcoder+=1
            # if cnt_nowcoder==1: break
    
    n=len(contest_list)
    if n==0: return '最近没有比赛哦'
    else:
        # contest_list.sort(key=operator.attrgetter('time'))
        ans=""
        cnt=0
        mintime=datetime.datetime.strptime('2099-12-12 19:00:00','%Y-%m-%d %H:%M:%S')
        for i in range(0,n):
            if contest_list[i].time.__le__(mintime):
                mintime=contest_list[i].time
        for i in range(0,n):
            if(contest_list[i].time.__eq__(mintime)):
                dt=datetime.datetime.strftime(contest_list[i].time,'%Y-%m-%d %H:%M:%S')
                ans+="\n比赛名称："+contest_list[i].name
                ans+="\n比赛时间："+dt
                ans+="\n比赛链接："+contest_list[i].link
                cnt+=1
        # if cnt_cf!=0:
        #     ans=ans+"\n"+get_cf
        # if cnt_atc!=0:
        #     ans=ans+"\n"+get_atc
        # if cnt_nowcoder!=0:
        #     ans=ans+"\n"+get_nowcoder
        return '找到最近的 '+str(cnt)+' 场比赛如下：'+ans