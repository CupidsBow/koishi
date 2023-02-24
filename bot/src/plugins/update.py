from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent
from nonebot.params import CommandArg
import requests
import json

update=on_command('update', priority=1)

@update.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    await get_cf()
    await get_atc()
    await get_nowcoder()
    await update.finish("更新成功")

async def get_cf():
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回 cf 的 API
    response=requests.get("https://codeforces.com/api/contest.list?gym=false",timeout=10)
    res=response.text
    pos=res.find("unavailable")
    if pos!=-1: return
    res=json.dumps(response.json())
    f=open('cf.txt','w')
    f.write(res)
    f.close()

async def get_atc():
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回 cf 的 API
    response=requests.get("https://atcoder.jp/contests/",timeout=10)
    res=response.text
    f=open('atc.txt','w',encoding='utf-8')
    f.write(res)
    f.close()

async def get_nowcoder():
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回 cf 的 API
    response=requests.get("https://ac.nowcoder.com/acm/contest/vip-index",timeout=10)
    res=response.text
    f=open('nc.txt','w',encoding='utf-8')
    f.write(res)
    f.close()