# coding=<encoding name>= ： # coding=utf-8
import yagmail
import yaml

from getpathInfo import text_Path
from text.del_txt import re_min_big_city_erro_num, re_min_search_city_erro_num, \
    re_min_nine_city_erro_num, re_min_geo_city_erro_num
from util.conf_read import ConfRead

a = text_Path()


def min_alarm():
    with open(a + "min_big_alarm.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_alarm = len(f.readlines())
    if big_alarm >= 1:
        with open(a + "min_big_alarm.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_alarm
    else:
        return [], 0


def min_aqi():
    with open(a + "min_big_aqi.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_aqi = len(f.readlines())
    if big_aqi >= 1:
        with open(a + "min_big_aqi.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_aqi
    else:
        return [], 0


def min_aqidays():
    with open(a + "min_big_aqidays.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_aqidays = len(f.readlines())
    if big_aqidays >= 1:
        with open(a + "min_big_aqidays.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_aqidays
    else:
        return [], 0


def min_base():
    with open(a + "min_big_base.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_base = len(f.readlines())
    if big_base >= 1:
        with open(a + "min_big_base.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_base
    else:
        return [], 0


def min_condition():
    with open(a + "min_big_condition.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_condition = len(f.readlines())
    if big_condition >= 1:
        with open(a + "min_big_condition.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_condition
    else:
        return [], 0


def min_dailys():
    with open(a + "min_big_dailys.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_dailys = len(f.readlines())
    if big_dailys >= 1:
        with open(a + "min_big_dailys.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_dailys
    else:
        return [], 0


def min_erro():
    with open(a + "min_big_erro.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_erro = len(f.readlines())
    if big_erro >= 1:
        with open(a + "min_big_erro.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_erro
    else:
        return [], 0


def min_hourlys():
    with open(a + "min_big_hourlys.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_hourlys = len(f.readlines())
    if big_hourlys >= 1:
        with open(a + "min_big_hourlys.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_hourlys
    else:
        return [], 0


def min_houraqi():
    with open(a + "min_big_houraqi.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        houraqi = len(f.readlines())
    if houraqi >= 1:
        with open(a + "min_big_houraqi.txt", mode='r+', encoding='utf-8') as f:
            return f.readlines(), houraqi
    else:
        return [], 0


# ===============================================================================

def min_liveInfos():
    with open(a + "min_big_liveinfos.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_liveinfos = len(f.readlines())
    if big_liveinfos >= 1:
        with open(a + "min_big_liveinfos.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_liveinfos
    else:
        return [], 0


# ===============================================================================

def min_ninety_erro():
    with open(a + "min_ninety_erro.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        ninety = len(f.readlines())
    if ninety >= 1:
        with open(a + "min_ninety_erro.txt", mode='r+', encoding='utf-8') as f:
            return f.readlines(), ninety
    else:
        return [], 0


def min_ninety_empty():
    with open(a + "min_ninety_empty.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        ninety = len(f.readlines())
    if ninety >= 1:
        with open(a + "min_ninety_empty.txt", mode='r+', encoding='utf-8') as f:
            return f.readlines(), ninety
    else:
        return [], 0


# ================================================================================

def min_search():
    with open(a + "min_search.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        search = len(f.readlines())
    if search >= 1:
        with open(a + "min_search.txt", mode='r+', encoding='utf-8') as f:
            return f.readlines(), search
    else:
        return [], 0


# ---------------------------------------------------------------

def min_geo_alarm():
    with open(a + "min_geo_alarm.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_alarm = len(f.readlines())
    if big_alarm >= 1:
        with open(a + "min_geo_alarm.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_alarm
    else:
        return [], 0


def min_geo_aqi():
    with open(a + "min_geo_aqi.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_aqi = len(f.readlines())
    if big_aqi >= 1:
        with open(a + "min_geo_aqi.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_aqi
    else:
        return [], 0


def min_geo_aqidays():
    with open(a + "min_geo_aqidays.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_aqidays = len(f.readlines())
    if big_aqidays >= 1:
        with open(a + "min_geo_aqidays.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_aqidays
    else:
        return [], 0


def min_geo_base():
    with open(a + "min_geo_base.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_base = len(f.readlines())
    if big_base >= 1:
        with open(a + "min_geo_base.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_base
    else:
        return [], 0


def min_geo_condition():
    with open(a + "min_geo_condition.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_condition = len(f.readlines())
    if big_condition >= 1:
        with open(a + "min_geo_condition.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_condition
    else:
        return [], 0


def min_geo_dailys():
    with open(a + "min_geo_dailys.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_dailys = len(f.readlines())
    if big_dailys >= 1:
        with open(a + "min_geo_dailys.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_dailys
    else:
        return [], 0


def min_geo_erro():
    with open(a + "min_geo_erro.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_erro = len(f.readlines())
    if big_erro >= 1:
        with open(a + "min_geo_erro.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_erro
    else:
        return [], 0


def min_geo_hourlys():
    with open(a + "min_geo_hourlys.txt", 'a+', encoding="utf-8") as f:
        f.seek(0)
        big_hourlys = len(f.readlines())
    if big_hourlys >= 1:
        with open(a + "min_geo_hourlys.txt", 'r+', encoding="utf-8") as f:
            return f.readlines(), big_hourlys
    else:
        return [], 0


def min_geo_houraqi():
    with open(a + "min_geo_houraqi.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        houraqi = len(f.readlines())
    if houraqi >= 1:
        with open(a + "min_geo_houraqi.txt", mode='r+', encoding='utf-8') as f:
            return f.readlines(), houraqi
    else:
        return [], 0


# ====================================================================================
def big_erro_city_num():
    with open(a + "min_big_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        erro_num = len(f.readlines())
    return erro_num


def nine_erro_city_num():
    with open(a + "min_nine_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        erro_num = len(f.readlines())
    return erro_num


def geo_erro_city_num():
    with open(a + "min_geo_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        erro_num = len(f.readlines())
    return erro_num


def live_erro_city_num():
    with open(a + "min_live_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        erro_num = len(f.readlines())
    return erro_num


def search_erro_city_num():
    with open(a + "min_search_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        erro_num = len(f.readlines())
    return erro_num


# ====================================================================================

def min_big_send_email(time):
    # =====================================================================
    a1, num1 = min_alarm()
    if a1 == []:
        pass
    else:
        a1.insert(0, f'【----------预警信息-模块错误----------】[{num1}]\n')
    a2, num2 = min_aqi()
    if a2 == []:
        pass
    else:
        a2.insert(0, f'【----------实时空气质量-模块错误----------】[{num2}]\n')
    a3, num3 = min_aqidays()
    if a3 == []:
        pass
    else:
        a3.insert(0, f'【----------多天空气质量-模块错误----------】[{num3}]\n')
    a4, num4 = min_base()
    if a4 == []:
        pass
    else:
        a4.insert(0, f'【---------- 城市信息-模块错误----------】[{num4}]\n')
    a5, num5 = min_condition()
    if a5 == []:
        pass
    else:
        a5.insert(0, f'【----------实况天气-模块错误----------】[{num5}]\n')
    a6, num6 = min_dailys()
    if a1 == []:
        pass
    else:
        a6.insert(0, f'【----------多天预报-模块错误----------】[{num6}]\n')
    a7, num7 = min_erro()
    if a7 == []:
        pass
    else:
        a7.insert(0, f'【----------接口错误无返回----------】[{num7}]\n')
    a8, num8 = min_hourlys()
    if a8 == []:
        pass
    else:
        a8.insert(0, f'【----------小时天气-模块错误----------】[{num8}]\n')
    a9, num9 = min_liveInfos()
    if a9 == []:
        pass
    else:
        a9.insert(0, f'【---------- 生活指数-模块错误----------】[{num9}]\n')
    a10, num10 = min_houraqi()
    if a10 == []:
        pass
    else:
        a10.insert(0, f'【---------- 小时空气质量-模块错误----------】[{num10}]\n')

    big = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    big_num = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    b = ''.join(big)
    e_name = ConfRead.conf_get('email.conf', 'email', 'email')
    e_r_name = yaml.load(e_name, Loader=yaml.FullLoader)
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="lizechen@droi.com", password="a124578", host='smtp.263.net')
    # 邮箱正文
    contents_big = b

    # file1 = log_path + 'logs.log'
    # 发送邮件
    yag.send(e_r_name,
             f'[vivo]-[广州]-[API]-[大颗粒-accucode]-[{big_erro_city_num()}]-[生活指数]-[{live_erro_city_num()}]-[第{time}次]',
             contents_big)
    re_min_big_city_erro_num()


def min_search_send_email(time):
    # =================================================================================
    s, s_num = min_search()
    if s == []:
        pass
    else:
        s.insert(0, f'【----------搜索接口-模块错误----------】[{s_num - 4}]\n')
    sea = ''.join(s)
    e_name = ConfRead.conf_get('email.conf', 'email', 'email')
    e_r_name = yaml.load(e_name, Loader=yaml.FullLoader)
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="lizechen@droi.com", password="a124578", host='smtp.263.net')
    # 邮箱正文
    contents_search = sea
    # 发送邮件

    yag.send(e_r_name, f'[vivo]-[广州]-[API]-[搜索]-[{search_erro_city_num()}]-[第{time}次]', contents_search)
    re_min_search_city_erro_num()


def min_ninety_send_email(time):
    # ================================================================================
    b1, num_nine1 = min_ninety_erro()
    if b1 == []:
        pass
    else:
        b1.insert(0, f'【----------九十日-接口异常和天数判断-模块错误----------】[{num_nine1}]\n')
    b2, num_nine2 = min_ninety_empty()
    if b2 == []:
        pass
    else:
        b2.insert(0, f'【----------九十日-字段是否为空-模块错误----------】[{num_nine2}]\n')
    nine = b1 + b2
    nine_num = num_nine1 + num_nine2
    c = ''.join(nine)

    e_name = ConfRead.conf_get('email.conf', 'email', 'email')
    e_r_name = yaml.load(e_name, Loader=yaml.FullLoader)
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="lizechen@droi.com", password="a124578", host='smtp.263.net')
    # 邮箱正文
    contents_nine = c
    # file1 = log_path + 'logs.log'
    # 发送邮件
    yag.send(e_r_name, f'[vivo]-[广州]-[API]-[九十日]-[{nine_erro_city_num()}]-[第{time}次]', contents_nine)
    re_min_nine_city_erro_num()


def min_geo_send_email(time):
    # ================================================================================
    g1, gnum1 = min_geo_alarm()
    if g1 == []:
        pass
    else:
        g1.insert(0, f'【----------预警信息-模块错误----------】[{gnum1}]\n')
    g2, gnum2 = min_geo_aqi()
    if g2 == []:
        pass
    else:
        g2.insert(0, f'【----------实时空气质量-模块错误----------】[{gnum2}]\n')
    g3, gnum3 = min_geo_aqidays()
    if g3 == []:
        pass
    else:
        g3.insert(0, f'【----------多天空气质量-模块错误----------】[{gnum3}]\n')
    g4, gnum4 = min_geo_base()
    if g4 == []:
        pass
    else:
        g4.insert(0, f'【---------- 城市信息-模块错误----------】[{gnum4}]\n')
    g5, gnum5 = min_geo_condition()
    if g5 == []:
        pass
    else:
        g5.insert(0, f'【----------实况天气-模块错误----------】[{gnum5}]\n')
    g6, gnum6 = min_geo_dailys()
    if g6 == []:
        pass
    else:
        g6.insert(0, f'【----------多天预报-模块错误----------】[{gnum6}]\n')
    g7, gnum7 = min_geo_erro()
    if g7 == []:
        pass
    else:
        g7.insert(0, f'【----------接口错误无返回----------】[{gnum7}]\n')
    g8, gnum8 = min_geo_hourlys()
    if g8 == []:
        pass
    else:
        g8.insert(0, f'【----------小时天气-模块错误----------】[{gnum8}]\n')
    g9, gnum9 = min_geo_houraqi()
    if g9 == []:
        pass
    else:
        g9.insert(0, f'【---------- 小时空气质量-模块错误----------】[{gnum9}]\n')

    geo = g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9
    geo_num = gnum1 + gnum2 + gnum3 + gnum4 + gnum5 + gnum6 + gnum7 + gnum8 + gnum9
    geo_a = ''.join(geo)
    # ================================================================================

    e_name = ConfRead.conf_get('email.conf', 'email', 'email')
    e_r_name = yaml.load(e_name, Loader=yaml.FullLoader)
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="lizechen@droi.com", password="a124578", host='smtp.263.net')
    # 邮箱正文
    contents_geo = geo_a
    yag.send(e_r_name, f'[vivo]-[广州]-[API]-[经纬度]-[{geo_erro_city_num()}]-[第{time}次]', contents_geo)
    re_min_geo_city_erro_num()


if __name__ == '__main__':
    min_big_send_email('2')
