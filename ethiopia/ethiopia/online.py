"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from ethiopia import ALIVE_NAME
from ethiopia.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**Ethio <Userbot>\n\n"
                     "**Telethon**: 6.9.0\n**Python**: 3.7.3\n"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     "**SYSTEM**: Linux\n"
                     f"**USER**: {DEFAULTUSER}\n\n"
                     "https://github.com/EthioDevX/EthioUserBot")