import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, USERBOT_NAME, USERNAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**Please set ALIVE_NAME, if you want the userbot to work properly**"
USERBOTNAME = str(USERBOT_NAME) if USERBOT_NAME else "**Please set USERBOT_NAME.**"
USERNAME = str(USERNAME) if USERNAME else "**Please set `USERNAME` in heroku vars**"


@command(pattern="^*alive", outgoing=True)
async def amireallyalive(alive):
    await alive.edit("**{USERBOTNAME} is alive & running.\n"
                     "**Telethon**: 6.9.0\n**Python**: 3.7.3\n"
                     "**User**: {USERNAME}\n"
                     f"**Master**: {DEFAULTUSER}\n"
                     "**Source code: https://GitHub.com/KenXer/Wolfik"
                     "**Repo status**: Private")
