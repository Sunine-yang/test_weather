import os

from getpathInfo import text_Path

text_aaa = text_Path()


# 移除
def re_file_search_big(path=text_aaa):
    try:
        os.remove(path + "big_erro.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "big_base.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "big_condition.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "big_dailys.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "big_aqidays.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "big_aqi.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "big_alarm.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "big_hourlys.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "big_liveinfos.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "search.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "big_houraqi.txt")
    except BaseException:
        pass


# 移除
def re_file_search_big_geo(path=text_aaa):
    try:
        os.remove(path + "geo_erro.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "geo_base.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "geo_condition.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "geo_dailys.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "geo_aqidays.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "geo_aqi.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "geo_alarm.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "geo_hourlys.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "geo_houraqi.txt")
    except BaseException:
        pass


def re_file_ninety(path=text_aaa):
    try:
        os.remove(path + "ninety_empty.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "ninety_erro.txt")
    except BaseException:
        pass


# ==========================================================

# 移除
def min_re_file_search_big(path=text_aaa):
    try:
        os.remove(path + "min_big_erro.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_big_base.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_big_condition.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_big_dailys.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_big_aqidays.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_big_aqi.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_big_alarm.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_big_hourlys.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_big_liveinfos.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_big_houraqi.txt")
    except BaseException:
        pass


def min_re_file_search(path=text_aaa):
    try:
        os.remove(path + "min_search.txt")
    except BaseException:
        pass


# 移除
def min_re_file_search_big_geo(path=text_aaa):
    try:
        os.remove(path + "min_geo_erro.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_geo_base.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_geo_condition.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_geo_dailys.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_geo_aqidays.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_geo_aqi.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_geo_alarm.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_geo_hourlys.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_geo_houraqi.txt")
    except BaseException:
        pass


def min_re_file_ninety(path=text_aaa):
    try:
        os.remove(path + "min_ninety_empty.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_ninety_erro.txt")
    except BaseException:
        pass


def re_big_city_erro_num(path):
    try:
        os.remove(path + "big_erro_citynum.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "live_erro_citynum.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "search_erro_citynum.txt")
    except BaseException:
        pass


def re_geo_city_erro_num(path):
    try:
        os.remove(path + "geo_erro_citynum.txt")
    except BaseException:
        pass


def re_nine_city_erro_num(path):
    try:
        os.remove(path + "nine_erro_citynum.txt")
    except BaseException:
        pass


def re_min_big_city_erro_num(path=text_aaa):
    try:
        os.remove(path + "min_big_erro_citynum.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "min_live_erro_citynum.txt")
    except BaseException:
        pass


def re_min_search_city_erro_num(path=text_aaa):
    try:
        os.remove(path + "min_search_erro_citynum.txt")
    except BaseException:
        pass


def re_min_nine_city_erro_num(path=text_aaa):
    try:
        os.remove(path + "min_nine_erro_citynum.txt")
    except BaseException:
        pass


def re_min_geo_city_erro_num(path=text_aaa):
    try:
        os.remove(path + "min_geo_erro_citynum.txt")
    except BaseException:
        pass


def re_foreign_big(path=text_aaa):
    try:
        os.remove(path + "foreign_big_erro.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "foreign_big_base.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "foreign_big_condition.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "foreign_big_dailys.txt")
    except BaseException:
        pass
    try:
        os.remove(path + "foreign_big_hourlys.txt")
    except BaseException:
        pass


def re_foreign_live(path=text_aaa):
    try:
        os.remove(path + "foreign_big_liveinfos.txt")
    except BaseException:
        pass


def re_foreign_big_num(path):
    try:
        os.remove(path + "foreign_big_erro_citynum.txt")
    except BaseException:
        pass


def re_foreign_live_num(path):
    try:
        os.remove(path + "foreign_live_erro_citynum.txt")
    except BaseException:
        pass
