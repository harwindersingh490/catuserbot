"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**MY BOT IS RUNNING SUCCESFULLY**\n\n"
                     "`☞Telethon version: 1.11.3\n`"
                     "`☞Python: 3.8.2\n`"
                     "`☞Bot was modified by:` CAT\n"
                     "`☞and created by :` GodXAnubis\n"
                     "`☞Database Status: Databases functioning normally!\n\n`"
                     "`☞Always with you, my master!😎😎\n`"
                
                     #"[Deploy this userbot Now](https://github.com/sandy1709/catuserbot)"
                    )
