import requests
from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

GPT_API_URL = "https://chatgpt.apinepdev.workers.dev"


@register(pattern="^/solve (.*)")
async def chat_gpt(event):
    if event.fwd_from:
        return

    query = event.pattern_match.group(1)

    if query:
        # Send "Please wait" message
        processing_message = await event.reply("📝")

        try:
            # Make a request to GPT API
            response = requests.get(f"{GPT_API_URL}/?question={query}")

            if response.status_code == 200:
                # Extract the answer from the API response
                result = response.json()

                # Check if "join" key is present and remove it
                if "join" in result:
                    del result["join"]

                # Add signature to the answer
                answer = result.get("answer", "❍ ɴᴏ ᴀɴsᴡᴇʀ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ sᴏʟᴠɪɴɢ ᴀɪ.")
                signature = "\n\n❍ sᴏʟᴠɪɴɢ ʙʏ ➛ [๛ᴀ ᴠ ɪ s ʜ ᴀ ༗](https://t.me/Avishaxbot)"
                reply_message = answer + signature

                # Edit the "Please wait" message with the final answer
                await processing_message.edit(reply_message)
            else:
                # If there's an error with the API, inform the user
                await processing_message.edit("Error communicating with ChatGPT API.")
        except requests.exceptions.RequestException as e:
            # Handle network-related errors
            await processing_message.edit(f"Error: {str(e)}. Please try again later.")
        except Exception as e:
            # Handle unexpected errors
            await processing_message.edit(f"Unexpected error: {str(e)}. Please try again later.")
    else:
        # Provide information about the correct command format
        await event.reply("❍ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇsᴛɪᴏɴ after /solve ᴄᴏᴍᴍᴀɴᴅ.\n\n❍ ғᴏʀ ᴇxᴀᴍᴘʟᴇ ➛ /solve ᴡʜᴀᴛ ɪs ᴛʜᴇ ʟᴏɢ¹¹ ᴠᴀʟᴜᴇ ?")


mod_name = "𝗦𝗢𝗟𝗩𝗘"
help = """
 ❍ sᴏʟᴠᴇ ᴛʜᴇ ᴀɴʏ sᴜʙᴊᴇᴄᴛs, ᴀɴʏ ᴄʟᴀss, ᴀɴʏ ᴄʜᴀᴘᴛᴇʀ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇ ᴅᴏᴜʙᴛ 💭

 ❍ /solve  *➛* ʀᴇᴘʟʏ ᴛo ǫᴜᴇsᴛɪᴏɴs ᴀɴʏ sᴜʙᴊᴇᴄᴛs ᴀɴʏ ᴄʟᴀss. 💭
 """
