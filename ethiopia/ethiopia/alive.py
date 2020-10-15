"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ETHIO_NAME) if ETHIO_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/fc3aef09eb9b82d244f97.jpg"
pm_caption += "**Ethio UserBot**\n"
pm_caption += "Telethon**: 6.0.9**\n**Python**: 3.7.4\n"
pm_caption += "**OS** : Linux\n"
pm_caption += f"**User** : {DEFAULTUSER} \n"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

    
