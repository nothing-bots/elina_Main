from datetime import datetime
from functools import wraps

from telegram.ext import CallbackContext

from MukeshRobot.modules.helper_funcs.misc import is_module_loaded

FILENAME = __name__.rsplit(".", 1)[-1]

if is_module_loaded(FILENAME):
    from telegram import ParseMode, Update
    from telegram.error import BadRequest, Unauthorized
    from telegram.ext import CommandHandler, JobQueue
    from telegram.utils.helpers import escape_markdown

    from MukeshRobot import EVENT_LOGS, LOGGER, dispatcher
    from MukeshRobot.modules.helper_funcs.chat_status import user_admin
    from MukeshRobot.modules.sql import log_channel_sql as sql

    def loggable(func):
        @wraps(func)
        def log_action(
            update: Update,
            context: CallbackContext,
            job_queue: JobQueue = None,
            *args,
            **kwargs,
        ):
            if not job_queue:
                result = func(update, context, *args, **kwargs)
            else:
                result = func(update, context, job_queue, *args, **kwargs)

            chat = update.effective_chat
            message = update.effective_message

            if result:
                datetime_fmt = "%H:%M - %d-%m-%Y"
                result += f"\n❍ <b>ᴇᴠᴇɴᴛ sᴛᴀᴍᴘ</b> ➛ <code>{datetime.utcnow().strftime(datetime_fmt)}</code>"

                if message.chat.type == chat.SUPERGROUP and message.chat.username:
                    result += f'\n❍ <b>ʟɪɴᴋ ➛ </b> <a href="https://t.me/{chat.username}/{message.message_id}">ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>'
                log_chat = sql.get_chat_log_channel(chat.id)
                if log_chat:
                    send_log(context, log_chat, chat.id, result)

            return result

        return log_action

    def gloggable(func):
        @wraps(func)
        def glog_action(update: Update, context: CallbackContext, *args, **kwargs):
            result = func(update, context, *args, **kwargs)
            chat = update.effective_chat
            message = update.effective_message

            if result:
                datetime_fmt = "%H:%M - %d-%m-%Y"
                result += "\n❍ <b>ᴇᴠᴇɴᴛ sᴛᴀᴍᴘ</b> ➛ <code>{}</code>".format(
                    datetime.utcnow().strftime(datetime_fmt)
                )

                if message.chat.type == chat.SUPERGROUP and message.chat.username:
                    result += f'\n❍ <b>ʟɪɴᴋ ➛</b> <a href="https://t.me/{chat.username}/{message.message_id}">ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>'
                log_chat = str(EVENT_LOGS)
                if log_chat:
                    send_log(context, log_chat, chat.id, result)

            return result

        return glog_action

    def send_log(
        context: CallbackContext, log_chat_id: str, orig_chat_id: str, result: str
    ):
        bot = context.bot
        try:
            bot.send_message(
                log_chat_id,
                result,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        except BadRequest as excp:
            if excp.message == "❍ ᴄʜᴀᴛ ɴᴏᴛ ғᴏᴜɴᴅ":
                bot.send_message(
                    orig_chat_id, "❍ ᴛʜɪs ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʜᴀs ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ - ᴜɴsᴇᴛᴛɪɴɢ."
                )
                sql.stop_chat_logging(orig_chat_id)
            else:
                LOGGER.warning(excp.message)
                LOGGER.warning(result)
                LOGGER.exception("❍ ᴄᴏᴜʟᴅ ɴᴏᴛ ᴘᴀʀsᴇ")

                bot.send_message(
                    log_chat_id,
                    result
                    + "\n\n❍ ғᴏʀᴍᴀᴛᴛɪɴɢ ʜᴀs ʙᴇᴇɴ ᴅɪsᴀʙʟᴇᴅ ᴅᴜᴇ ᴛᴏ ᴀɴ ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴇʀʀᴏʀ.",
                )
                
    @user_admin
    def logging(update: Update, context: CallbackContext):
        bot = context.bot
        message = update.effective_message
        chat = update.effective_chat

        log_channel = sql.get_chat_log_channel(chat.id)
        if log_channel:
            log_channel_info = bot.get_chat(log_channel)
            message.reply_text(
                f"❍ ᴛʜɪs ɢʀᴏᴜᴘ ʜᴀs ᴀʟʟ ɪᴛ's ʟᴏɢs sᴇɴᴛ ᴛᴏ"
                f" {escape_markdown(log_channel_info.title)} (`{log_channel}`)",
                parse_mode=ParseMode.MARKDOWN,
            )

        else:
            message.reply_text("❍ ɴᴏ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʜᴀs ʙᴇᴇɴ sᴇᴛ ғᴏʀ ᴛʜɪs ɢʀᴏᴜᴘ !")

    @user_admin
    def setlog(update: Update, context: CallbackContext):
        bot = context.bot
        message = update.effective_message
        chat = update.effective_chat
        if chat.type == chat.CHANNEL:
            message.reply_text(
                "❍ ɴᴏᴡ, ғᴏʀᴡᴀʀᴅ ᴛʜᴇ /setlog ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛɪᴇ ᴛʜɪs ᴄʜᴀɴɴᴇʟ ᴛᴏ !"
            )

        elif message.forward_from_chat:
            sql.set_chat_log_channel(chat.id, message.forward_from_chat.id)
            try:
                message.delete()
            except BadRequest as excp:
                if excp.message == "❍ ᴍᴇssᴀɢᴇ ᴛᴏ ᴅᴇʟᴇᴛᴇ ɴᴏᴛ ғᴏᴜɴᴅ":
                    pass
                else:
                    LOGGER.exception(
                        "❍ ᴇʀʀᴏʀ ᴅᴇʟᴇᴛɪɴɢ ᴍᴇssᴀɢᴇ ɪɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. sʜᴏᴜʟᴅ ᴡᴏʀᴋ ᴀɴʏᴡᴀʏ ᴛʜᴏᴜɢʜ."
                    )

            try:
                bot.send_message(
                    message.forward_from_chat.id,
                    f"❍ ᴛʜɪs ᴄʜᴀɴɴᴇʟ ʜᴀs ʙᴇᴇɴ sᴇᴛ ᴀs ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ғᴏʀ {chat.title or chat.first_name}.",
                )
            except Unauthorized as excp:
                if excp.message == "❍ ғᴏʀʙɪᴅᴅᴇɴ : ʙᴏᴛ ɪs ɴᴏᴛ ᴀ ᴍᴇᴍʙᴇʀ ᴏғ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴄʜᴀᴛ":
                    bot.send_message(chat.id, "❍ sᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛ ʟᴏɢ ᴄʜᴀɴɴᴇʟ !")
                else:
                    LOGGER.exception("❍ ᴇʀʀᴏʀ ɪɴ sᴇᴛᴛɪɴɢ ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.")

            bot.send_message(chat.id, "❍ sᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛ ʟᴏɢ ᴄʜᴀɴɴᴇʟ !")

        else:
            message.reply_text(
                "❍ ᴛʜᴇ sᴛᴇᴘs ᴛᴏ sᴇᴛ ᴀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀʀᴇ\n"
                " ❍ ᴀᴅᴅ ʙᴏᴛ ᴛᴏ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴄʜᴀɴɴᴇʟ\n"
                "❍ sᴇɴᴅ /setlog ᴛᴏ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ\n"
                "❍ ғᴏʀᴡᴀʀᴅ ᴛʜᴇ /setlog ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ\n"
            )

    @user_admin
    def unsetlog(update: Update, context: CallbackContext):
        bot = context.bot
        message = update.effective_message
        chat = update.effective_chat

        log_channel = sql.stop_chat_logging(chat.id)
        if log_channel:
            bot.send_message(
                log_channel, f"❍ ᴄʜᴀɴɴᴇʟ ʜᴀs ʙᴇᴇɴ ᴜɴʟɪɴᴋᴇᴅ ғʀᴏᴍ {chat.title}"
            )
            message.reply_text("❍ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʜᴀs ʙᴇᴇɴ ᴜɴ-sᴇᴛ.")

        else:
            message.reply_text("❍ ɴᴏ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʜᴀs ʙᴇᴇɴ sᴇᴛ ʏᴇᴛ !")

    def __stats__():
        return f"❅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ sᴇᴛ ➛ {sql.num_logchannels()}\n"

    def __migrate__(old_chat_id, new_chat_id):
        sql.migrate_chat(old_chat_id, new_chat_id)

    def __chat_settings__(chat_id, user_id):
        log_channel = sql.get_chat_log_channel(chat_id)
        if log_channel:
            log_channel_info = dispatcher.bot.get_chat(log_channel)
            return f"❍ ᴛʜɪs ɢʀᴏᴜᴘ ʜᴀs ᴀʟʟ ɪᴛ's ʟᴏɢs sᴇɴᴛ ᴛᴏ ➛ {escape_markdown(log_channel_info.title)} (`{log_channel}`)"
        return "❍ ɴᴏ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ɪs sᴇᴛ ғᴏʀ ᴛʜɪs ɢʀᴏᴜᴘ !"

    __help__ = """
✿ *ᴀᴅᴍɪɴs ᴏɴʟʏ* ✿

 ❍ /logchannel *➛* ɢᴇᴛ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ɪɴғᴏ
 ❍ /setlog *➛* sᴇᴛ ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
 ❍ /unsetlog *➛* ᴜɴsᴇᴛ ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.

✿ sᴇᴛᴛɪɴɢ ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ɪs ᴅᴏɴᴇ ʙʏ ✿

❍ ᴀᴅᴅɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴄʜᴀɴɴᴇʟ (ᴀs ᴀɴ ᴀᴅᴍɪɴ!)
❍ sᴇɴᴅɪɴɢ /setlog ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ
❍ ғᴏʀᴡᴀʀᴅɪɴɢ ᴛʜᴇ /setlog ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ
"""

    __mod_name__ = "𝗟-𝗖𝗛𝗔𝗡𝗡𝗘𝗟"

    LOG_HANDLER = CommandHandler("logchannel", logging, run_async=True)
    SET_LOG_HANDLER = CommandHandler("setlog", setlog, run_async=True)
    UNSET_LOG_HANDLER = CommandHandler("unsetlog", unsetlog, run_async=True)

    dispatcher.add_handler(LOG_HANDLER)
    dispatcher.add_handler(SET_LOG_HANDLER)
    dispatcher.add_handler(UNSET_LOG_HANDLER)

else:
    # run anyway if module not loaded
    def loggable(func):
        return func

    def gloggable(func):
        return func
        
