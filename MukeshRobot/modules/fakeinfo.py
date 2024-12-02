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

from faker import Faker
from faker.providers import internet
from telethon import events
from MukeshRobot import telethn as tbot
from pyrogram import filters
from MukeshRobot import pbot

@tbot.on(events.NewMessage(pattern="/fakegen$"))
async def hi(event):
    fake = Faker()
    print("❍ ғᴀᴋᴇ ᴅᴇᴛᴀɪʟs ɢᴇɴᴇʀᴀᴛᴇᴅ\n")
    name = str(fake.name())
    fake.add_provider(internet)
    address = str(fake.address())
    ip = fake.ipv4_private()
    cc = fake.credit_card_full()
    email = fake.ascii_free_email()
    job = fake.job()
    android = fake.android_platform_token()
    pc = fake.chrome()
    await event.reply(
        f"<b>✦ ғᴀᴋᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b> ✦\n\n<b>❍ ɴᴀᴍᴇ ➛ </b><code>{name}</code>\n\n<b>❍ ᴀᴅᴅʀᴇss ➛ </b><code>{address}</code>\n\n<b>❍ ɪᴘ ᴀᴅᴅʀᴇss ➛ </b><code>{ip}</code>\n\n<b>❍ ᴄʀᴇᴅɪᴛ ᴄᴀʀᴅ ➛ </b><code>{cc}</code>\n\n<b>❍ ᴇᴍᴀɪʟ ɪᴅ ➛ </b><code>{email}</code>\n\n<b>❍ ᴊᴏʙ ➛ </b><code>{job}</code>\n\n<b>❍ ᴀɴᴅʀᴏɪᴅ ᴜsᴇʀ ᴀɢᴇɴᴛ ➛ </b><code>{android}</code>\n\n<b>❍ ᴘᴄ ᴜsᴇʀ ᴀɢᴇɴᴛ ➛ </b><code>{pc}</code>",
        parse_mode="HTML",
    )

@pbot.on_message(filters.command('picgen'))
async def picgen(_, message):
    img = "https://thispersondoesnotexist.com/image"
    text = f"❍ ғᴀᴋᴇ ɪᴍᴀɢᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ."
    await message.reply_photo(photo=img, caption=text)




__mod_name__ = "𝗙𝗔𝗞𝗘-𝗜𝗡𝗙𝗢"

__help__ = """
❍ `/fakegen` ➛ ɢᴇɴᴇʀᴀᴛᴇs ғᴀᴋᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ
❍ `/picgen` ➛ ɢᴇɴᴇʀᴀᴛᴇ ᴀ ғᴀᴋᴇ ᴘɪᴄ
"""
