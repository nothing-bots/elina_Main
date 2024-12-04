#API CREDITS - @Yash_Sharama_1807 and @KIRITO1240
#PROVIDED BY - @NovaXMod
#MADE BY - @KIRITO_1240

#IMPORTS
import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import *
#NAME -> YOUR BOTS FILE NAME 
from MukeshRobot import pbot as app


@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"❍ ᴄᴏsᴘʟᴀʏ ʙʏ ➛ ᴢᴇʀᴏ ᴛᴡᴏ \n\n❍ ᴄʀᴇᴅɪᴛs ʙʏ ➛ ᴊss ʙᴏᴛs")

@app.on_message(filters.command("ncosplay"))
async def ncosplay(_,msg):
    if msg.chat.type != ChatType.PRIVATE:
      await msg.reply_text("❍ sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʙᴏᴛ",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ɢᴏ ᴘᴍ",url=f"https://t.me/{app.me.username}?start=True")]
            ]
        ))
    else:
       ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()

       await msg.reply_photo(ncosplay, caption=f"❍ ᴄᴏsᴘʟᴀʏ ʙʏ ➛ 『 ＥＬＩＮＡ 』\n\n❍ ᴄʀᴇᴅɪᴛs ʙʏ ➛ @Botz_X_Hub")


__mod_name__ = "𝗖𝗢𝗦𝗣𝗟𝗔𝗬"
__help__ = """
 ❍ /cosplay ➛ ʀᴀɴᴅᴏᴍ ᴄᴏsᴘʟᴀʏ ɪᴍᴀɢᴇ.
 
 ❍ /ncosplay ➛ ʀᴀɴᴅᴏᴍ ɴᴜᴅᴇ ᴄᴏsᴘʟᴀʏ ɪᴍᴀɢᴇ.
 """
 
