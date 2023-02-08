import time
from nonebot import on_command,on_request
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent,FriendRequestEvent,GroupRequestEvent
from nonebot.params import CommandArg
import datetime
import requests
import json
from nonebot import require
import nonebot
import asyncio

self_add=on_request(priority=60)
group_add=on_request(priority=60)

@self_add.handle()
async def ad_f(bot: Bot, event: FriendRequestEvent):
    await event.approve(bot)
    id = int(event.get_user_id())
    await asyncio.sleep(1)
    await bot.call_api('send_private_msg',user_id=id,message=Message('''---koishi bot---
cf/precf
atc/preatc
nc/prenc
today
next
update
help
QQ -> 1143957699
'''
    ))

@group_add.handle()
async def ad_f(bot: Bot, event: GroupRequestEvent):
    await event.approve(bot)
    await asyncio.sleep(1)