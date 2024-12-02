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

import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from MukeshRobot import dispatcher
from MukeshRobot.modules.disable import DisableAbleCommandHandler



def covid(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text.split(" ", 1)
    if len(text) == 1:
        r = requests.get("https://corona.lmao.ninja/v2/all").json()
        reply_text = f"**✦ ɢʟᴏʙᴀʟ ᴛᴏᴛᴀʟs** ✦\n\n❍ ᴄᴀsᴇs ➛ {r['cases']:,}\n❍ ᴄᴀsᴇs ᴛᴏᴅᴀʏ ➛ {r['todayCases']:,}\n❍ ᴅᴇᴀᴛʜs ➛ {r['deaths']:,}\n❍ ᴅᴇᴀᴛʜs ᴛᴏᴅᴀʏ ➛ {r['todayDeaths']:,}\n❍ ʀᴇᴄᴏᴠᴇʀᴇᴅ ➛ {r['recovered']:,}\n❍ ᴀᴄᴛɪᴠᴇ ➛ {r['active']:,}\n❍ ᴄʀɪᴛɪᴄᴀʟ ➛ {r['critical']:,}\n❍ ᴄᴀsᴇs/ᴍɪʟ ➛ {r['casesPerOneMillion']}\n❍ ᴅᴇᴀᴛʜs/ᴍɪʟ ➛ {r['deathsPerOneMillion']}"
    else:
        variabla = text[1]
        r = requests.get(f"https://corona.lmao.ninja/v2/countries/{variabla}").json()
        reply_text = f"**✦ ᴄᴀsᴇs ғᴏʀ ➛ {r['country']} ✦**\n\n❍ ᴄᴀsᴇs ➛ {r['cases']:,}\n❍ ᴄᴀsᴇs ᴛᴏᴅᴀʏ ➛ {r['todayCases']:,}\n❍ ᴅᴇᴀᴛʜs ➛ {r['deaths']:,}\n❍ ᴅᴇᴀᴛʜs ᴛᴏᴅᴀʏ ➛ {r['todayDeaths']:,}\n❍ ʀᴇᴄᴏᴠᴇʀᴇᴅ ➛ {r['recovered']:,}\n❍ ᴀᴄᴛɪᴠᴇ ➛ {r['active']:,}\n❍ ᴄʀɪᴛɪᴄᴀʟ ➛ {r['critical']:,}\n❍ ᴄᴀsᴇs/ᴍɪʟ ➛ {r['casesPerOneMillion']}\n❍ ᴅᴇᴀᴛʜs/ᴍɪʟ ➛ {r['deathsPerOneMillion']}"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


COVID_HANDLER = DisableAbleCommandHandler(["covid", "corona"], covid, run_async = True)
dispatcher.add_handler(COVID_HANDLER)

__mod_name__ = "𝗖𝗢𝗩𝗜𝗗-𝟭𝟵"
__help__ = """
❍ `/corona` ➛ ɢɪᴠᴇs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʀᴇɢᴀʀᴅɪɴɢ covid 19 cases
❍ `/covid` ➛ ɢɪᴠᴇs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʀᴇɢᴀʀᴅɪɴɢ ᴄᴏᴠɪᴅ 19 ᴄᴀsᴇs
"""
