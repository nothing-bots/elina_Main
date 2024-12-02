from MukeshRobot import telethn as tbot
import os
import re
import bs4
import requests
from telethon import types
from telethon.tl import functions
from MukeshRobot.events import register

langi = "en"


@register(pattern="^/imdb (.*)")
async def imdb(e):
    if e.fwd_from:
        return
    try:
        movie_name = e.pattern_match.group(1)
        remove_space = movie_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + final_name + "&s=all"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        odds = soup.findAll("tr", "odd")
        mov_title = odds[0].findNext("td").findNext("td").text
        mov_link = (
            "http://www.imdb.com/" + odds[0].findNext("td").findNext("td").a["href"]
        )
        page1 = requests.get(mov_link)
        soup = bs4.BeautifulSoup(page1.content, "lxml")
        if soup.find("div", "poster"):
            poster = soup.find("div", "poster").img["src"]
        else:
            poster = ""
        if soup.find("div", "title_wrapper"):
            pg = soup.find("div", "title_wrapper").findNext("div").text
            mov_details = re.sub(r"\s+", " ", pg)
        else:
            mov_details = ""
        credits = soup.findAll("div", "credit_summary_item")
        if len(credits) == 1:
            director = credits[0].a.text
            writer = "❍ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ"
            stars = "❍ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ"
        elif len(credits) > 2:
            director = credits[0].a.text
            writer = credits[1].a.text
            actors = []
            for x in credits[2].findAll("a"):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        else:
            director = credits[0].a.text
            writer = "❍ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ"
            actors = []
            for x in credits[1].findAll("a"):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        if soup.find("div", "inline canwrap"):
            story_line = soup.find("div", "inline canwrap").findAll("p")[0].text
        else:
            story_line = "❍ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ"
        info = soup.findAll("div", "txt-block")
        if info:
            mov_country = []
            mov_language = []
            for node in info:
                a = node.findAll("a")
                for i in a:
                    if "country_of_origin" in i["href"]:
                        mov_country.append(i.text)
                    elif "primary_language" in i["href"]:
                        mov_language.append(i.text)
        if soup.findAll("div", "ratingValue"):
            for r in soup.findAll("div", "ratingValue"):
                mov_rating = r.strong["title"]
        else:
            mov_rating = "❍ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ"
        await e.reply(
            "<a href=" + poster + ">&#8203;</a>"
            "<b>❍ ᴛɪᴛʟᴇ ➛ </b><code>"
            + mov_title
            + "</code>\n<code>"
            + mov_details
            + "</code>\n<b>❍ ʀᴀᴛɪɴɢ ➛ </b><code>"
            + mov_rating
            + "</code>\n<b>❍ ᴄᴏᴜɴᴛʀʏ ➛ </b><code>"
            + mov_country[0]
            + "</code>\n<b>❍ ʟᴀɴɢᴜᴀɢᴇ ➛ </b><code>"
            + mov_language[0]
            + "</code>\n<b>❍ ᴅɪʀᴇᴄᴛᴏʀ ➛ </b><code>"
            + director
            + "</code>\n<b>❍ ᴡʀɪᴛᴇʀ ➛ </b><code>"
            + writer
            + "</code>\n<b>❍ sᴛᴀʀs ➛ </b><code>"
            + stars
            + "</code>\n<b>❍ ɪᴍᴅʙ ᴜʀʟ ➛ </b>"
            + mov_link
            + "\n<b>❍ sᴛᴏʀʏ ʟɪɴᴇ ➛ </b>"
            + story_line,
            link_preview=True,
            parse_mode="HTML",
        )
    except IndexError:
        await e.reply("❍ ᴘʟᴢ ᴇɴᴛᴇʀ ᴠᴀʟɪᴅ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ.")

__mod_name__ = "𝗜𝗠𝗗𝗕"
__help__ = """
 ❍ /imdb ➛ sᴇᴀʀᴄʜ ᴀ ᴍᴏᴠɪᴇ ᴅᴇᴛᴀɪʟs.
 """
