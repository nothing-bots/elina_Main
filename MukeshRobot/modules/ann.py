"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

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

# Imports from external libraries. (DON'T EDIT)
import requests
from telegram import ParseMode
from telegram.ext import CommandHandler

# Imports dispatcher = updater.dispatcher from __init__.py (*MUST EDIT* CHANGE MODULE NAME TO THE FOLDER NAME OF MODULES IN YOUR BOT)
from MukeshRobot import dispatcher

# Main code, Credit to https://github.com/itspro-dev for making the API. 
def ann(update, context):
    try:
        msg = update.effective_message
        # API (DON'T EDIT)
        url = f'https://api.animeepisode.org/waifu/animenews.php'
        result = requests.get(url).json()
        img = result['Post_image']
        # Message (EDIT THIS PART AS HTML *IF YOU WANT*)
        text = f'''
<b>❍ ᴛɪᴛʟᴇ ➛</b> <code>{result['Post_title']}</code>
        
<b>❍ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➛</b> <code>{result['Description']}</code>

<b>❍ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ➛</b> <code>{result['Post_url']}</code>
'''
        msg.reply_photo(photo=img, caption=text, parse_mode=ParseMode.HTML)

    except Exception as e:
        text = f'<b>Error</b>: <code>' + e + '</code>'
        msg.reply_text(text, parse_mode=ParseMode.HTML)

# Code Handler (YOU CAN CHANGE 'ann' TO ANY 'cmd' FOR THIS TO BE WORKED AS '/cmd' *IF YOU WANT*.)
ANN_HANDLER = CommandHandler('ann', ann, run_async=True)
dispatcher.add_handler(ANN_HANDLER)

#  Buttons for /help .
__mod_name__ = "𝗔𝗡𝗜𝗠𝗘-𝗡"  # *IF YOU WANT* EDIT NAME OF BUTTON IN '/help'

# *IF YOU WANT* EDIT MESSAGE FOR HELP OF THIS MODULE.
__help__ = '''
❍ `/ann` ➛ ɢɪᴠᴇs ʟᴀᴛᴇsᴛ ᴀɴɪᴍᴇ ɴᴇᴡs.
❍ `/subscribe` ➛ sᴜsᴄʀɪʙᴇs ᴛᴏ ᴀɴɪᴍᴇ ɴᴇᴡs ɴᴇᴛᴡᴏʀᴋ ғᴇᴇᴅs.
❍ `/unsubscribe` ➛ sᴜsᴄʀɪʙᴇs ᴛᴏ ᴀɴɪᴍᴇ ɴᴇᴡs ɴᴇᴛᴡᴏʀᴋ ғᴇᴇᴅs.
'''

# DON'T EDIT
__handlers__ = [ANN_HANDLER]
