import requests
from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

JOKES_API_URL = "https://hindijokes.apinepdev.workers.dev/"

@register(pattern="^/(joke|jokes)$")
async def fetch_joke(event):
    if event.fwd_from:
        return

    # Send "Generating a joke" message
    processing_message = await event.reply("GENERATING A JOKE FOR YOU BABY...")

    try:
        # Make a request to the Jokes API
        response = requests.get(JOKES_API_URL)

        if response.status_code == 200:
            # Extract the joke from the API response
            joke_data = response.json()
            joke = joke_data.get("hindi_Jokes", "❍ ɴᴏ ᴊᴏᴋᴇ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ")

            # Add signature below the joke
            signature = "\n\n๏ ᴊᴏᴋᴇs ɢᴇɴᴇʀᴀᴛᴇᴅ ᴠɪᴀ ➠ [『 ＥＬＩＮＡ 』](https://t.me/Elina_Roxbot)"
            reply_message = f"💌 {joke}{signature}"
        else:
            reply_message = "❍ ᴇʀʀᴏʀ ғᴇᴛᴄʜɪɴɢ ᴊᴏᴋᴇ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ."
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        reply_message = f"❍ ᴇʀʀᴏʀ ➛ {str(e)}. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ."
    except Exception as e:
        # Handle unexpected errors
        reply_message = f"❍ ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴇʀʀᴏʀ ➛ {str(e)}. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ."

    # Edit the "Generating a joke" message with the final reply
    await processing_message.edit(reply_message)

__mod_name__ = "𝗝𝗢𝗞𝗘𝗦"

__help__ = """
❍ ᴡʀɪᴛᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ➛ `/joke` ᴛᴏ ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴊᴏᴋᴇs.
"""
