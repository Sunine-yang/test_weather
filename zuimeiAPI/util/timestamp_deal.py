# coding=<encoding name> ： # coding=utf-8
import datetime
from dateutil.parser import parse


def ts_deal(re):
    # 时间戳
    d = datetime.datetime.fromtimestamp(re / 1000)
    str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")

    now = datetime.datetime.now()
    str2 = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    a = parse(str1)
    b = parse(str2)

    c = ((b - a).seconds / 60) / 60
    return c


def ts_nine(re):
    now = datetime.datetime.now()
    str_h = now.strftime("%H")

    # 昨天
    day1 = now + datetime.timedelta(days=-1)
    # 前天
    day2 = now + datetime.timedelta(days=-2)

    day1_re = day1.strftime("%Y-%m-%d")
    day2_re = day2.strftime("%Y-%m-%d")

    d = datetime.datetime.fromtimestamp(re / 1000)
    str1 = d.strftime("%Y-%m-%d")

    if int(str_h) > 9:
        if str1 == day1_re:
            return 1
        else:
            return 2
    else:
        if str1 == day1_re or str1 == day2_re:
            return 1
        else:
            return 2


def aqi_today():
    now = datetime.datetime.now()
    str_h = now.strftime("%H")

    if int(str_h) > 9:
        return 1
    else:
        return 2


def hourlys_zero(re):
    now = datetime.datetime.now()
    str_h = now.strftime("%H")

    d = datetime.datetime.fromtimestamp(re / 1000)
    str1 = d.strftime("%H")

    a = int(str1) - int(str_h)
    if a == 0:
        return 1
    else:
        return 2


def ninety_start_end():
    now = datetime.datetime.now()
    start_day_time = now + datetime.timedelta(days=-1)
    end_day_time = now + datetime.timedelta(days=90)
    start_day = start_day_time.strftime("%Y%m%d")
    end_day = end_day_time.strftime("%Y%m%d")
    return start_day, end_day


def ninety_erro_day(daynum):
    now = datetime.datetime.now()
    start_day_time = now + datetime.timedelta(days=-1)
    answ_day_time = start_day_time + datetime.timedelta(days=daynum)
    answ_day = answ_day_time.strftime("%Y-%m-%d")
    return answ_day


# 传入格式时间字符串，判断与当前时间整点小时的差值是否为1
def houraqi_time(time):
    a = datetime.datetime.now()
    a_time = datetime.datetime.strftime(a, '%H')

    b = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
    b_time = datetime.datetime.strftime(b, '%H')

    if int(a_time) - int(b_time) == 1 or int(a_time) - int(b_time) == -23 or int(a_time) - int(b_time) == 0:
        return 1
    else:
        return 2


# 多天预报 为了将下标转化为日期
# 准备以下标0的时间作为第一天，然后加就完事了
def daily_day_deal(time, num):
    d = datetime.datetime.fromtimestamp(time / 1000)
    time = d + datetime.timedelta(days=num)
    str1 = time.strftime("%Y-%m-%d")
    return str1


# 多天空气质量，将下标转化为日期，跟上面差不多
def aqi_days_day_deal(time, num):
    b = datetime.datetime.strptime(time, '%Y-%m-%d')

    time = b + datetime.timedelta(days=num)
    str1 = time.strftime("%Y-%m-%d")
    return str1


# 将小时天气的时间戳转化为时间
def hourlys_time_deal(re):
    d = datetime.datetime.fromtimestamp(re / 1000)
    str1 = d.strftime("%Y-%m-%d %H:%M")
    return str1


# 判断现在时间是否为早上九点
def isnot_nine():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    if time == '09:00':
        return 1
    else:
        return 2


if __name__ == '__main__':
    a = ts_deal(1611644400000)
    print(a)
