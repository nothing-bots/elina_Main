"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import urllib.request

from bs4 import BeautifulSoup
from telethon import events
from MukeshRobot import telethn as tbot
from telethon.tl import functions, types
from telethon.tl.types import *


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


@tbot.on(events.NewMessage(pattern="/(c|cs)$"))
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("✦ ɴᴇᴇᴅ ᴀᴅᴍɪɴ ᴘᴇᴡᴇʀ.. ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.. ʙᴜᴛ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ɪɴ ᴍʏ ᴘᴍ")
       return

    score_page = "http://static.cricinfo.com/rss/livescores.xml"
    page = urllib.request.urlopen(score_page)
    soup = BeautifulSoup(page, "html.parser")
    result = soup.find_all("description")
    Sed = ""
    for match in result:
        Sed += match.get_text() + "\n\n"
    await event.reply(
        f"<b>✦ ᴍᴀᴛᴄʜ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀᴇᴅ sᴜᴄᴄᴇssғᴜʟ ✦</b>\n\n\n๏ <code>{Sed}</code>",
        parse_mode="HTML",
    )

__mod_name__ = "𝗖𝗥𝗜𝗖𝗞𝗘𝗧"
__help__ = """
 ❍ `/c` ➛ ᴛᴏ ᴄʜᴇᴄᴋ ʟɪᴠᴇ ᴄʀɪᴄᴋᴇᴛ sᴄᴏʀᴇ.
 ❍ `/cs` ➛ ᴛᴏ ᴄʜᴇᴄᴋ ʟɪᴠᴇ ᴄʀɪᴄᴋᴇᴛ sᴄᴏʀᴇ.
"""
