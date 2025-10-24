import os
from dhooks import Webhook, Embed, File

image2_path = 'pj.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[PJ forum je azuriran - click here -](https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=11&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2025&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=)**",
        color=0x3498DB
    )

    embed.set_image(url="attachment://pj.png")
    file = File(image2_path, name="pj.png")
    hook.send("@everyone 📢 PJ", embed=embed, file=file)
