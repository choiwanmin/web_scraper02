# 웹 스크래핑 코드
import requests
from bs4 import BeautifulSoup

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
            
    except Exception as e :
        continue