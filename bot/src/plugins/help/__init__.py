from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent
from nonebot.params import CommandArg
from nonebot import require

help=on_command('help', priority=1)

@help.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res='''cf/precf
atc/preatc
nc/prenc
today
next
update
help
'''
    await help.finish(res)