"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from ethiopia import ETHIO_NAME
from ethiopia.utils import admin_cmd

DEFAULTUSER = str(ETHIO_NAME) if ETHIO_NAME else "No Name set yet, please add ETHIO_NAME."

@command(outgoing=True, pattern="^*alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("EthioUserBot is running.\n\n"
                     "System: Linux\nTelethon version: 6.9.0\nPython: 3.7.3\n"
                     "UserBot created by: @EthioUserBot"
                     f"\nUser: {DEFAULTUSER}\n"
                     "")
