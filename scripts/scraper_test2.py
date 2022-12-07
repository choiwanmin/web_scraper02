# 웹 스크래핑 코드
# 텔레그램 push
import requests
from bs4 import BeautifulSoup
import telegram
from . import teletram_info as ti

TLGM_BOT_API = ti.TLGM_BOT_API
tlgm_bot = telegram.Bot(TLGM_BOT_API) # API , 메모리에 올라감, 식별을 위해 변수지정
#  https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu
url = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'
res = requests.get(url)
# print(res.text)

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)
items = soup.select("tr.list1, tr.list0")
# print(items)

# img_url, title, link, replay_count, up_count
for item in items:
    try:
        img_url = item.select("img.thumb_border")[0].get("src").strip()
        title = item.select("a font.list_title")[0].text.strip()
        link = item.select("a font.list_title")[0].parent.get("href").strip()
        link = link.replace("/zboard/", "")
        link = link.lstrip('/')
        link = "https://www.ppomppu.co.kr/zboard/" + link
        # https://www.ppomppu.co.kr/zboard/view.php?id=ppomppu&page=1&divpage=75&no=444053
        replay_count = item.select("td span.list_comment2 span")[0].text.strip()
        up_count = item.select("td.eng.list_vspace")[-2].text.strip()
        up_count = up_count.split("-")[0]
        up_count = int(up_count)
        print(up_count)

        if up_count >= 3:
            print(img_url, title, link, replay_count, up_count)
            # 텔레그램 봇으로  push
            chat_id = ti.chat_id
            message = title
            # tlgm_bot.sendMessage(chat_id, 전송_message)
            tlgm_bot.sendMessage(chat_id, message)
    except Exception as e :
    # except Exception as e :
        continue