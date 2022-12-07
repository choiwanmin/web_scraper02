# 웹 스크래핑 코드
# 텔레그램 push
# django로 DB 저장하기
import requests
from bs4 import BeautifulSoup
import telegram
# from . import teletram_info as ti # django_extensions # 장고하고 별개 일때는 from . 규칙을 안붙여도 가능
import env_info as ti # 장고이기때문에 세팅즈에서 베이스 폴더를 여기로 잡고 있기 때문에
from hotdeal.models import Deal

from datetime import datetime, timedelta

# db 테이블 데이터 유지기간 설정 변수
during_date = 3

# DB 테이블 저장을 위한 추천 갯수 지정(3개이상)
up_cnt_limit = 3

TLGM_BOT_API = ti.TLGM_BOT_API
tlgm_bot = telegram.Bot(TLGM_BOT_API) # API , 메모리에 올라감, 식별을 위해 변수지정
#  https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu
url = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'
res = requests.get(url)
# print(res.text)


soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

# def run():
#     items = soup.select("tr.list1, tr.list0")
#     # print(items)
#     # img_url, title, link, replay_count, up_count
#     for item in items:
#         try:
#             img_url = item.select("img.thumb_border")[0].get("src").strip()
#             title = item.select("a font.list_title")[0].text.strip()
#             link = item.select("a font.list_title")[0].parent.get("href").strip()
#             link = link.replace("/zboard/", "")
#             link = link.lstrip('/')
#             link = "https://www.ppomppu.co.kr/zboard/" + link
#             # https://www.ppomppu.co.kr/zboard/view.php?id=ppomppu&page=1&divpage=75&no=444053
#             reply_count = item.select("td span.list_comment2 span")[0].text.strip()
#             up_count = item.select("td.eng.list_vspace")[-2].text.strip()
#             up_count = up_count.split("-")[0]
#             up_count = int(up_count)
#             print(up_count)
#             if up_count >= 3:
#                 # 터미널 프린트
#                 print(img_url, title, link, reply_count, up_count)
#                 # 텔레그램 봇으로  push
#                 chat_id = ti.chat_id
#                 message = title
#                 # tlgm_bot.sendMessage(chat_id, 전송_message)
#                 tlgm_bot.sendMessage(chat_id, message)

#                 # hotdeal 앱의 Deal클래스를 통해 DB 테이블에 데이터 저장
#                 # 스크래핑한 link가 DB 테이블에 몇개 있는지 카운트
#                 # db_link_cnt=Deal.objects.filter(link__iexact=link).count()
#                 # link가 중복되지 않도록 체크하고, 없으면 저장
#                 # if(db_link_cnt==0):
#                 #     # 스크래핑 결과를 DB의 Deal 테이블에 저장
#                 if(Deal.objects.filter(link__iexact=link).count()==0):
#                     Deal(img_url=img_url, title=title, link=link, reply_count=reply_count,up_count=up_count).save()

#         except Exception as e :
#         # except Exception as e :
            # continue


def run():
    # DB 테이블에 3일치만 유지함
    # row, _ = Deal.objects.filter(cdate__lte=dateime.now() - timedelta(days=3)).delete()
    row, _ = Deal.objects.filter(cdate__lte=datetime.now() - timedelta(minutes=during_date)).delete()
    print("DB delete 갯수",row)
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
            reply_count = item.select("td span.list_comment2 span")[0].text.strip()
            up_count = item.select("td.eng.list_vspace")[-2].text.strip()
            up_count = up_count.split("-")[0]
            up_count = int(up_count)
            print(up_count)



            if up_count >= 3:
                # 터미널 프린트
                print(img_url, title, link, reply_count, up_count)
                # hotdeal 앱의 Deal클래스를 통해 DB 테이블에 데이터 저장
                # link가 중복되지 않도록 체크하고, 없으면 저장
                if(Deal.objects.filter(link__iexact=link).count()==0):
                    # 텔레그램 봇으로  push
                    chat_id = ti.chat_id
                    message = title
                    # tlgm_bot.sendMessage(chat_id, 전송_message)
                    tlgm_bot.sendMessage(chat_id, message)
                    # 스크래핑한 link가 DB 테이블에 몇개 있는지 카운트
                    Deal(img_url=img_url, title=title, link=link, reply_count=reply_count,up_count=up_count).save()
                    # db_link_cnt=Deal.objects.filter(link__iexact=link).count()
                    # if(db_link_cnt==0):
                    # 스크래핑 결과를 DB의 Deal 테이블에 저장

        except Exception as e :
            continue