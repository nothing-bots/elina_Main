# Module to get info about anime, characters, manga etc. by @TheRealPhoenix

from jikanpy import Jikan
from jikanpy.exceptions import APIException

from telegram import (
    Message,
    Chat,
    User,
    ParseMode,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async

from MukeshRobot import dispatcher

jikan = Jikan()


def anime(update: Update, context: CallbackContext):
    msg = update.effective_message
    args = context.args
    query = " ".join(args)
    res = ""
    try:
        res = jikan.search("anime", query)
    except APIException:
        msg.reply_text("❍ ᴇʀʀᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ ᴛʜᴇ ᴀᴘɪ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ !")
        return ""
    try:
        res = res.get("results")[0].get("mal_id")  # Grab first result
    except APIException:
        msg.reply_text("❍ ᴇʀʀᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ ᴛʜᴇ ᴀᴘɪ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ !")
        return ""
    if res:
        anime = jikan.anime(res)
        title = anime.get("title")
        japanese = anime.get("title_japanese")
        type = anime.get("type")
        duration = anime.get("duration")
        synopsis = anime.get("synopsis")
        source = anime.get("source")
        status = anime.get("status")
        episodes = anime.get("episodes")
        score = anime.get("score")
        rating = anime.get("rating")
        genre_lst = anime.get("genres")
        genres = ""
        for genre in genre_lst:
            genres += genre.get("name") + ", "
        genres = genres[:-2]
        studios = ""
        studio_lst = anime.get("studios")
        for studio in studio_lst:
            studios += studio.get("name") + ", "
        studios = studios[:-2]
        duration = anime.get("duration")
        premiered = anime.get("premiered")
        image_url = anime.get("image_url")
        url = anime.get("url")
        trailer = anime.get("trailer_url")
    else:
        msg.reply_text("❍ ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ !")
        return
    rep = f"✦ <b>{title} ({japanese})</b> ✦\n\n"
    rep += f"<b>❍ ᴛʏᴘᴇ ➛</b> <code>{type}</code>\n"
    rep += f"<b>❍ sᴏᴜʀᴄᴇ ➛</b> <code>{source}</code>\n"
    rep += f"<b>❍ sᴛᴀᴛᴜs ➛</b> <code>{status}</code>\n"
    rep += f"<b>❍ ɢᴇɴʀᴇs ➛</b> <code>{genres}</code>\n"
    rep += f"<b>❍ ᴇᴘɪsᴏᴅᴇs ➛</b> <code>{episodes}</code>\n"
    rep += f"<b>❍ ᴅᴜʀᴀᴛɪᴏɴ ➛</b> <code>{duration}</code>\n"
    rep += f"<b>❍ sᴄᴏʀᴇ ➛</b> <code>{score}</code>\n"
    rep += f"<b>❍ sᴛᴜᴅɪᴏ(s) ➛</b> <code>{studios}</code>\n"
    rep += f"<b>❍ ᴘʀᴇᴍɪᴇʀᴇᴅ ➛</b> <code>{premiered}</code>\n"
    rep += f"<b>❍ ʀᴀᴛɪɴɢ ➛</b> <code>{rating}</code>\n\n"
    rep += f"❍ <a href='{image_url}'>\u200c</a>"
    rep += f"❍ <i>{synopsis}</i>\n"
    if trailer:
        keyb = [
            [
                InlineKeyboardButton("ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ", url=url),
                InlineKeyboardButton("ᴛʀᴀɪʟᴇʀ", url=trailer),
            ]
        ]
    else:
        keyb = [[InlineKeyboardButton("ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ", url=url)]]

    msg.reply_text(
        rep, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(keyb)
    )


def character(update: Update, context: CallbackContext):
    msg = update.effective_message
    res = ""
    args = context.args
    query = " ".join(args)
    try:
        search = jikan.search("character", query).get("results")[0].get("mal_id")
    except APIException:
        msg.reply_text("❍ ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ!")
        return ""
    if search:
        try:
            res = jikan.character(search)
        except APIException:
            msg.reply_text("❍ ᴇʀʀᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ ᴛʜᴇ ᴀᴘɪ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ !")
            return ""
    if res:
        name = res.get("name")
        kanji = res.get("name_kanji")
        about = res.get("about")
        if len(about) > 4096:
            about = about[:4000] + "..."
        image = res.get("image_url")
        url = res.get("url")
        rep = f"❍ <b>{name} ({kanji})</b>\n\n"
        rep += f"❍ <a href='{image}'>\u200c</a>"
        rep += f"❍ <i>{about}</i>\n"
        keyb = [[InlineKeyboardButton("ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ", url=url)]]

        msg.reply_text(
            rep, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(keyb)
        )


def upcoming(update: Update, context: CallbackContext):
    msg = update.effective_message
    rep = "❍ <b>ᴜᴘᴄᴏᴍɪɴɢ ᴀɴɪᴍᴇ</b>\n"
    later = jikan.season_later()
    anime = later.get("anime")
    for new in anime:
        name = new.get("title")
        url = new.get("url")
        rep += f"❍ <a href='{url}'>{name}</a>\n"
        if len(rep) > 2000:
            break
    msg.reply_text(rep, parse_mode=ParseMode.HTML)


def manga(update: Update, context: CallbackContext):
    msg = update.effective_message
    args = context.args
    query = " ".join(args)
    res = ""
    manga = ""
    try:
        res = jikan.search("manga", query).get("results")[0].get("mal_id")
    except APIException:
        msg.reply_text("❍ ᴇʀʀᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ ᴛʜᴇ ᴀᴘɪ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ !")
        return ""
    if res:
        try:
            manga = jikan.manga(res)
        except APIException:
            msg.reply_text("❍ ᴇʀʀᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ ᴛʜᴇ ᴀᴘɪ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ !")
            return ""
        title = manga.get("title")
        japanese = manga.get("title_japanese")
        type = manga.get("type")
        status = manga.get("status")
        score = manga.get("score")
        volumes = manga.get("volumes")
        chapters = manga.get("chapters")
        genre_lst = manga.get("genres")
        genres = ""
        for genre in genre_lst:
            genres += genre.get("name") + ", "
        genres = genres[:-2]
        synopsis = manga.get("synopsis")
        image = manga.get("image_url")
        url = manga.get("url")
        rep = f"❍ <b>{title} ({japanese})</b>\n"
        rep += f"<b>❍ ᴛʏᴘᴇ ➛ </b> <code>{type}</code>\n"
        rep += f"<b>❍ sᴛᴀᴛᴜs ➛ </b> <code>{status}</code>\n"
        rep += f"<b>❍ ɢᴇɴʀᴇs ➛ </b> <code>{genres}</code>\n"
        rep += f"<b>❍ sᴄᴏʀᴇ ➛ </b> <code>{score}</code>\n"
        rep += f"<b>❍ ᴠᴏʟᴜᴍᴇs ➛ </b> <code>{volumes}</code>\n"
        rep += f"<b>❍ ᴄʜᴀᴘᴛᴇʀs ➛ </b> <code>{chapters}</code>\n\n"
        rep += f"❍ <a href='{image}'>\u200c</a>"
        rep += f"❍ <i>{synopsis}</i>"
        keyb = [[InlineKeyboardButton("ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ", url=url)]]

        msg.reply_text(
            rep, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(keyb)
        )


__mod_name__ = "𝗠-𝗔𝗡𝗜𝗠𝗘"

__help__ = """
 ❍ /manime ➛ ᴄʜᴋ ᴍʏ ᴀɴɪᴍᴇ
 ❍ /mupcoming ➛ ᴄʜᴋ ᴍʏ ᴜᴘᴄᴏᴍɪɴɢ ᴀɴɪᴍᴇ
 ❍ /mcharacter ➛ ᴄʜᴋ ᴍʏ ғᴀᴠ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ
 ❍ /mmanga ➛ ᴄʜᴋ ᴍʏ ᴍᴀɴɢᴀ
 
 """

ANIME_HANDLER = CommandHandler("manime", anime, pass_args=True, run_async=True)
CHARACTER_HANDLER = CommandHandler(
    "mcharacter", character, pass_args=True, run_async=True
)
UPCOMING_HANDLER = CommandHandler("mupcoming", upcoming, run_async=True)
MANGA_HANDLER = CommandHandler("mmanga", manga, pass_args=True, run_async=True)

dispatcher.add_handler(ANIME_HANDLER)
dispatcher.add_handler(CHARACTER_HANDLER)
dispatcher.add_handler(UPCOMING_HANDLER)
dispatcher.add_handler(MANGA_HANDLER)
    
