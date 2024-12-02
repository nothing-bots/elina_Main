import requests
from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

INSTAGRAM_API_URL = "https://instagramdownloader.apinepdev.workers.dev/"

@register(pattern="^/insta(?: |$)(.*)")
async def search_and_send_instagram_video(event):
    if event.fwd_from:
        return

    # Extract the Instagram video URL from the user's message
    insta_video_url = event.pattern_match.group(1).strip()

    if not insta_video_url:
        await event.reply("❍ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ɪɴsᴛᴀɢʀᴀᴍ ᴠɪᴅᴇᴏ ᴜʀʟ.")
        return

    # Send "Please wait" message
    processing_message = await event.reply("❍ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴡʜɪʟᴇ ғᴇᴛᴄʜɪɴɢ ʏᴏᴜʀ ᴅᴏᴡɴʟᴏᴀᴅ...")

    try:
        # Make a request to the Instagram Video Downloader API
        response = requests.get(f"{INSTAGRAM_API_URL}?url={insta_video_url}")

        if response.status_code == 200:
            # Downloaded Instagram video URL
            video_url = response.json().get("data")[0].get("url", "❍ ɴᴏ ᴠɪᴅᴇᴏ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ")

            # Format the reply with a clickable link
            reply_message = f"✦ ʏᴏᴜʀ ɪɴsᴛᴀ ɪᴍᴀɢᴇs/ʀᴇᴇʟs ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ.\n\n๏ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ɪᴍᴀɢᴇ/ʀᴇᴇʟs ➠ [ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ]({video_url})\n\n๏ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ᴠɪᴀ ➠ [๛ᴀ ᴠ ɪ s ʜ ᴀ ༗](https://t.me/AvishaxBot)"
        else:
            reply_message = "❍ ᴇʀʀᴏʀ ғᴇᴛᴄʜɪɴɢ ɪɴsᴛᴀɢʀᴀᴍ ᴠɪᴅᴇᴏ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ."
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        reply_message = f"❍ ᴇʀʀᴏʀ : {str(e)}. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ."
    except Exception as e:
        # Handle unexpected errors
        reply_message = f"❍ ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴇʀʀᴏʀ : {str(e)}. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ."

    # Edit the "Please wait" message with the final reply
    await processing_message.edit(reply_message)

__mod_name__ = "𝗧𝗢𝗢𝗟𝗦"

__help__ = """
❍ /insta ➛ ᴘᴀsᴛᴇ ɪɴsᴛᴀ ʀᴇᴇʟs / ɪᴍᴀɢᴇ ᴜʀʟ ɪs ʜᴇʀᴇ ʙᴀʙʏ ᴛᴏ ᴅᴏᴡɴʟᴏᴀʀᴅ ɪɴsᴛᴀ ᴠɪᴅᴇᴏ/ ʀᴇᴇʟs.

❍ /fbdl ➛ ᴘᴀsᴛᴇ ғᴀᴄᴇʙᴏᴏᴋ ʀᴇᴇʟs ᴜʀʟ ʙᴀʙʏ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ғᴀᴄᴇʙᴏᴏᴋ ʀᴇᴇʟs.

❍ ᴄᴏᴍᴍᴀɴᴅ ➛ `/yt` ᴠɪᴅᴇᴏ ᴜʀʟ
"""
