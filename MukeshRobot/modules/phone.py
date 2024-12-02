import json

import requests
from telegram.ext import CommandHandler, run_async

from MukeshRobot import dispatcher
from MukeshRobot.modules.helper_funcs.alternate import send_message
from MukeshRobot.modules.helper_funcs.chat_status import user_admin

__mod_name__ = "𝗖𝗔𝗟𝗟𝗘𝗥"
__help__ = """
❍ /phone ꜰɪʟʟ ᴀɴʏ ᴍᴏʙɪʟᴇ ɴᴜᴍʙᴇʀ ᴛᴏ ᴄʜᴇᴄᴋ ɪɴꜰᴏ.
"""


@run_async
@user_admin
def phone(update, context):

    args = update.effective_message.text.split(None, 1)
    information = args[1]
    number = information
    key = "f66950368a61ebad3cba9b5924b4532d"
    api = (
        "http://apilayer.net/api/validate?access_key="
        + key
        + "&number="
        + number
        + "&country_code=&format=1"
    )
    output = requests.get(api)
    content = output.text
    obj = json.loads(content)
    country_code = obj["country_code"]
    country_name = obj["country_name"]
    location = obj["location"]
    carrier = obj["carrier"]
    line_type = obj["line_type"]
    validornot = obj["valid"]
    aa = "✦ ᴠᴀʟɪᴅ ➛" + str(validornot)
    a = "✦ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ➛ " + str(number)
    b = "✦ ᴄᴏᴜɴᴛʀʏ ➛ " + str(country_code)
    c = "✦ ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ ➛ " + str(country_name)
    d = "✦ ʟᴏᴄᴀᴛɪᴏɴ ➛ " + str(location)
    e = "✦ ᴄᴀʀʀɪᴇʀ ➛ " + str(carrier)
    f = "✦ ᴅᴇᴠɪᴄᴇ ➛ " + str(line_type)
    g = f"{aa}\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}"
    send_message(update.effective_message, g)


PHONE_HANDLER = CommandHandler("phone", phone)

dispatcher.add_handler(PHONE_HANDLER)


__command_list__ = ["phone"]
__handlers__ = [PHONE_HANDLER]
