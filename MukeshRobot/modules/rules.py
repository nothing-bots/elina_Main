from typing import Optional

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import escape_markdown

import MukeshRobot.modules.sql.rules_sql as sql
from MukeshRobot import dispatcher
from MukeshRobot.modules.helper_funcs.chat_status import connection_status, user_admin
from MukeshRobot.modules.helper_funcs.string_handling import markdown_parser


@connection_status
def get_rules(update: Update, context: CallbackContext):
    args = context.args
    here = args and args[0] == "here"
    chat_id = update.effective_chat.id
    # connection_status sets update.effective_chat
    real_chat = update.effective_message.chat
    dest_chat = real_chat.id if here else None
    send_rules(update, chat_id, real_chat.type == real_chat.PRIVATE or here, dest_chat)


# Do not async - not from a handler
def send_rules(update, chat_id, from_pm=False, dest_chat=None):
    bot = dispatcher.bot
    user = update.effective_user  # type: Optional[User]
    reply_msg = update.message.reply_to_message
    dest_chat = dest_chat or user.id
    try:
        chat = bot.get_chat(chat_id)
    except BadRequest as excp:
        if excp.message == "❍ ᴄʜᴀᴛ ɴᴏᴛ ғᴏᴜɴᴅ." and from_pm:
            bot.send_message(
                dest_chat,
                "❍ ᴛʜᴇ ʀᴜʟᴇs sʜᴏʀᴛᴄᴜᴛ ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ ʜᴀsɴ'ᴛ ʙᴇᴇɴ sᴇᴛ ᴘʀᴏᴘᴇʀʟʏ! ᴀsᴋ ᴀᴅᴍɪɴs ᴛᴏ "
                "ғɪx ᴛʜɪs.\n❍ ᴍᴀʏʙᴇ ᴛʜᴇʏ ғᴏʀɢᴏᴛ ᴛʜᴇ ʜʏᴘʜᴇɴ ɪɴ ɪᴅ",
            )
            return
        else:
            raise

    rules = sql.get_rules(chat_id)
    text = f"❍ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ *{escape_markdown(chat.title)}* ᴀʀᴇ\n\n❍ {rules}"

    if from_pm and rules:
        bot.send_message(
            dest_chat,
            text,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )
    elif from_pm:
        bot.send_message(
            dest_chat,
            "❍ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs ʜᴀᴠᴇɴ'ᴛ sᴇᴛ ᴀɴʏ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ ʏᴇᴛ. "
            "❍ ᴛʜɪs ᴘʀᴏʙᴀʙʟʏ ᴅᴏᴇsɴ'ᴛ ᴍᴇᴀɴ ɪᴛ's ʟᴀᴡʟᴇss ᴛʜᴏᴜɢʜ...!",
        )
    elif rules and reply_msg:
        reply_msg.reply_text(
            "❍ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ʀᴜʟᴇs.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʀᴜʟᴇs",
                            url=f"t.me/{bot.username}?start={chat_id}",
                        ),
                    ],
                ],
            ),
        )
    elif rules:
        update.effective_message.reply_text(
            "❍ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ʀᴜʟᴇs.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʀᴜʟᴇs",
                            url=f"t.me/{bot.username}?start={chat_id}",
                        ),
                    ],
                ],
            ),
        )
    else:
        update.effective_message.reply_text(
            "❍ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs ʜᴀᴠᴇɴ'ᴛ sᴇᴛ ᴀɴʏ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ ʏᴇᴛ. "
            "❍ ᴛʜɪs ᴘʀᴏʙᴀʙʟʏ ᴅᴏᴇsɴ'ᴛ ᴍᴇᴀɴ ɪᴛ's ʟᴀᴡʟᴇss ᴛʜᴏᴜɢʜ...!",
        )


@connection_status
@user_admin
def set_rules(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    msg = update.effective_message  # type: Optional[Message]
    raw_text = msg.text
    args = raw_text.split(None, 1)  # use python's maxsplit to separate cmd and args
    txt = entities = None
    if len(args) == 2:
        txt = args[1]
        entities = msg.parse_entities()
    elif msg.reply_to_message:
        txt = msg.reply_to_message.text
        entities = msg.reply_to_message.parse_entities()
    if txt:
        offset = len(txt) - len(raw_text)  # set correct offset relative to command
        markdown_rules = markdown_parser(
            txt,
            entities=entities,
            offset=offset,
        )

        sql.set_rules(chat_id, markdown_rules)
        update.effective_message.reply_text("❍ sᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ɢʀᴏᴜᴘ.")
    else:
        update.effective_message.reply_text("❍ ᴛʜᴇʀᴇ's... ɴᴏ ʀᴜʟᴇs ?")


@connection_status
@user_admin
def clear_rules(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    sql.set_rules(chat_id, "")
    update.effective_message.reply_text("❍ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʟᴇᴀʀᴇᴅ ʀᴜʟᴇs !")


def __stats__():
    return f"❅ ɢʀᴏᴜᴘ ʜᴀᴠᴇ ʀᴜʟᴇs ➛ {sql.num_chats()}\n"


def __import_data__(chat_id, data):
    # set chat rules
    rules = data.get("info", {}).get("rules", "")
    sql.set_rules(chat_id, rules)


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, user_id):
    return f"❍ ᴛʜɪs ᴄʜᴀᴛ ʜᴀs ʜᴀᴅ ɪᴛ's ʀᴜʟᴇs sᴇᴛ ➛ `{bool(sql.get_rules(chat_id))}`"


__help__ = """
 ❍ `/rules`* ➛* ɢᴇᴛ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.
 
 ❍ `/rules here`* ➛* ɢᴇᴛ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ ʙᴜᴛ sᴇɴᴅ ɪᴛ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
 
✿ *ᴀᴅᴍɪɴs ᴏɴʟʏ* ✿

 ❍ `/setrules <your rules here>`* ➛* sᴇᴛ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.
 ❍ `/clearrules`* ➛* ᴄʟᴇᴀʀ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.
"""

__mod_name__ = "𝗥𝗨𝗟𝗘𝗦"

GET_RULES_HANDLER = CommandHandler("rules", get_rules, run_async=True)
SET_RULES_HANDLER = CommandHandler("setrules", set_rules, run_async=True)
RESET_RULES_HANDLER = CommandHandler("clearrules", clear_rules, run_async=True)

dispatcher.add_handler(GET_RULES_HANDLER)
dispatcher.add_handler(SET_RULES_HANDLER)
dispatcher.add_handler(RESET_RULES_HANDLER)
    
