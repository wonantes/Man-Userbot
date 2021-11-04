import requests

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd
from userbot.utils import edit_or_reply


@bot.on(man_cmd(outgoing=True, pattern="lyrictd(?: |$)(.*)"))
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("**Silahkan Masukan Judul Lagu**")
    try:
        xxnx = await edit_or_reply(event,"`Searching Lyrics...`")
        resp = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{resp['data']}"
        await xxnx.edit(result)
    except Exception as e:
        await xxnx.edit(f"**ERROR:** `{e}`")


CMD_HELP.update(
    {
        "lyrics": f"**Plugin : **`lyrics`\
        \n\n  •  **Syntax :** `{cmd}lyrics` <judul lagu>\
        \n  •  **Function : **Dapatkan lirik yang cocok dengan judul lagu.\
    "
    }
)
