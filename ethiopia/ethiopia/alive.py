"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from ethiopia import ETHIO_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ETHIO_NAME) if ETHIO_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/0bdef0088deecc05bf991.png"
pm_caption = "Ethio <Userbot> 🇪🇹 is running\n\n"
pm_caption += "SYSTEM: Linux**\n"
pm_caption += "TELETHON VERSION: 6.9.0\nPython:3.7.3\n"
pm_caption += f"My Boss 💪 : {DEFAULTUSER} \n"
pm_caption += "UserBot created by 😎 : @EthioUserBot\n\n"
pm_caption += "Deploy Your Own : [Repo](https://github.com/Kalebpy/EthioUserBot)\n"

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
