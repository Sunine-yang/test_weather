import time

from getpathInfo import text_Path_shanghai
from minute.min_big import MinBig
from minute.min_dailys import MinNinety
from minute.min_geo import MinGeo
from minute.min_liveInfos import MinLiveInfos
from minute.min_search import MinSearch
from text.del_txt import min_re_file_search_big, min_re_file_search_big_geo, min_re_file_ninety, \
    min_re_file_search, re_min_big_city_erro_num, re_min_geo_city_erro_num, re_min_nine_city_erro_num, \
    re_min_search_city_erro_num
from util.send_min_email import SendEM
from util.timestamp_deal import isnot_nine
from threading import Thread

big = MinBig(path=text_Path_shanghai())
nin = MinNinety(path=text_Path_shanghai())
geo = MinGeo(path=text_Path_shanghai())
live = MinLiveInfos(path=text_Path_shanghai())
search = MinSearch(path=text_Path_shanghai())
nine_time = isnot_nine()
email = SendEM(path=text_Path_shanghai(), name='上海2')


def run_minute_big():
    num = 1
    num5 = 0
    nine_str = '九点'
    send_time = 5
    while True:
        big_r = big.min_code_to_name('2332508', '长汀县')
        live_r = live.min_liveInfos_api('106566', '西安市')
        if nine_time == 1:
            email.min_big_send_email(nine_str, path=text_Path_shanghai())
            min_re_file_search_big(path=text_Path_shanghai())
            time.sleep(60)
        else:
            if num <= 5:
                if big_r == 1 or live_r == 1:
                    email.min_big_send_email(str(num), path=text_Path_shanghai())
                    min_re_file_search_big(path=text_Path_shanghai())
                    num += 1
                    time.sleep(60)
                else:
                    min_re_file_search_big()
                    re_min_big_city_erro_num(path=text_Path_shanghai())
                    num = 1
                    time.sleep(60)
            else:
                if big_r == 1 or live_r == 1:
                    num5 += 1
                    send_time += 1
                    if num5 == 5:
                        email.min_big_send_email(str(send_time), path=text_Path_shanghai())
                        min_re_file_search_big(path=text_Path_shanghai())
                        num5 = 0
                        time.sleep(60)
                    else:
                        min_re_file_search_big(path=text_Path_shanghai())
                        re_min_big_city_erro_num(path=text_Path_shanghai())
                        time.sleep(60)
                else:
                    min_re_file_search_big(path=text_Path_shanghai())
                    re_min_big_city_erro_num(path=text_Path_shanghai())
                    time.sleep(60)
                    num5 = 0
                    num = 1
                    send_time = 5


def run_minute_geo():
    # ----------------------------------------------------------------------------
    num = 1
    num5 = 0
    nine_str = '九点'
    send_time = 5
    while True:
        geo_r = geo.min_geo_to_name('130.318917', '46.799923', '佳木斯市')
        if nine_time == 1:
            email.min_geo_send_email(nine_str, path=text_Path_shanghai())
            min_re_file_search_big_geo(path=text_Path_shanghai())
            time.sleep(60)
        else:
            if num <= 5:
                if geo_r == 1:
                    email.min_geo_send_email(str(num), path=text_Path_shanghai())
                    min_re_file_search_big_geo(path=text_Path_shanghai())
                    num += 1
                    time.sleep(60)
                else:
                    re_min_geo_city_erro_num(path=text_Path_shanghai())
                    min_re_file_search_big_geo(path=text_Path_shanghai())
                    num = 1
                    time.sleep(60)
            else:
                if geo_r == 1:
                    num5 += 1
                    send_time += 1
                    if num5 == 5:
                        email.min_geo_send_email(str(send_time), path=text_Path_shanghai())
                        min_re_file_search_big_geo(path=text_Path_shanghai())
                        num5 = 0
                        time.sleep(60)
                    else:
                        re_min_geo_city_erro_num(path=text_Path_shanghai())
                        min_re_file_search_big_geo(path=text_Path_shanghai())
                        time.sleep(60)
                else:
                    re_min_geo_city_erro_num(path=text_Path_shanghai())
                    min_re_file_search_big_geo(path=text_Path_shanghai())
                    time.sleep(60)
                    num5 = 0
                    num = 1
                    send_time = 5


def run_minute_nine():
    num = 1
    num5 = 0
    nine_str = '九点'
    send_time = 5
    while True:
        nin_r = nin.min_dailys_api('106566', '西安市')
        if nine_time == 1:
            email.min_ninety_send_email(nine_str, path=text_Path_shanghai())
            min_re_file_ninety(path=text_Path_shanghai())
            time.sleep(60)
        else:
            if num <= 5:
                if nin_r == 1:
                    email.min_ninety_send_email(str(num), path=text_Path_shanghai())
                    min_re_file_ninety(path=text_Path_shanghai())
                    num += 1
                    time.sleep(60)
                else:
                    re_min_nine_city_erro_num(path=text_Path_shanghai())
                    min_re_file_ninety(path=text_Path_shanghai())
                    num = 1
                    time.sleep(60)
            else:
                if nin_r == 1:
                    num5 += 1
                    send_time += 1
                    if num5 == 5:
                        email.min_ninety_send_email(str(send_time), path=text_Path_shanghai())
                        min_re_file_ninety(path=text_Path_shanghai())
                        num5 = 0
                        time.sleep(60)
                    else:
                        re_min_nine_city_erro_num(path=text_Path_shanghai())
                        min_re_file_ninety(path=text_Path_shanghai())
                        time.sleep(60)
                else:
                    re_min_nine_city_erro_num(path=text_Path_shanghai())
                    min_re_file_ninety(path=text_Path_shanghai())
                    time.sleep(60)
                    num5 = 0
                    num = 1
                    send_time = 5


def run_minute_search():
    num = 1
    num5 = 0
    nine_str = '九点'
    send_time = 5
    while True:
        search_r = search.min_search_api()
        if nine_time == 1:
            email.min_search_send_email(nine_str, path=text_Path_shanghai())
            min_re_file_search(path=text_Path_shanghai())
            time.sleep(60)
        else:
            if num <= 5:
                if search_r == 1:
                    email.min_search_send_email(str(num), path=text_Path_shanghai())
                    min_re_file_search(path=text_Path_shanghai())
                    num += 1
                    time.sleep(60)
                else:
                    re_min_search_city_erro_num(path=text_Path_shanghai())
                    min_re_file_search(path=text_Path_shanghai())
                    num = 1
                    time.sleep(60)
            else:
                if search_r == 1:
                    num5 += 1
                    send_time += 1
                    if num5 == 5:
                        email.min_search_send_email(str(send_time), path=text_Path_shanghai())
                        min_re_file_search(path=text_Path_shanghai())
                        num5 = 0
                        time.sleep(60)
                    else:
                        re_min_search_city_erro_num(path=text_Path_shanghai())
                        min_re_file_search(path=text_Path_shanghai())
                        time.sleep(60)
                else:
                    re_min_search_city_erro_num(path=text_Path_shanghai())
                    min_re_file_search(path=text_Path_shanghai())
                    time.sleep(60)
                    num5 = 0
                    num = 1
                    send_time = 5


t1 = Thread(target=run_minute_big)
t2 = Thread(target=run_minute_geo)
t3 = Thread(target=run_minute_nine)
t4 = Thread(target=run_minute_search)

t1.start()
t2.start()
t3.start()
t4.start()
