import datetime

from log.Log import logger

i = datetime.datetime.now()


def get_date():
    pass

    # print("当前是星期 %s" % i.isoweekday())
    # print("当前的日期和时间是 %s" % i)
    # print("ISO格式的日期和时间是 %s" % i.isoformat())
    # print("当前的年份是 %s" % i.year)
    # print("当前的月份是 %s" % i.month)
    # print("当前的日期是  %s" % i.day)
    # print("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
    # print("当前小时是 %s" % i.hour)
    # print("当前分钟是 %s" % i.minute)
    # print("当前秒是  %s" % i.second)


# 获取当前日期
def format_month():
    try:
        date = datetime.datetime.now().strftime('%d日')
        a = datetime.datetime.now().timetuple()
        VersionInfo = str(a.tm_mon) + "月" + date
    except BaseException:
        print('datetime函数获取当前日期失败!')
        logger.info('datetime函数获取当前日期失败!')
    else:
        print(f'成功用datetime函数获取当前日期成功，当前日期为：{VersionInfo}')
        logger.info(f'成功用datetime函数获取当前日期成功，当前日期为：{VersionInfo}')
        return str(VersionInfo)


# 获取当前星期几
def format_weekday():
    try:
        weekday = i.isoweekday()
    except BaseException:
        print('datetime函数获取当前星期失败！')
        logger.info('datetime函数获取当前星期失败！')
    else:
        print(f'成功用datetime函数获取当前星期成功，当前星期为：{weekday}')
        logger.info(f'成功用datetime函数获取当前星期成功，当前星期为：{weekday}')
        if weekday == 1:
            return '星期一'
        elif weekday == 2:
            return '星期二'
        elif weekday == 3:
            return '星期三'
        elif weekday == 4:
            return '星期四'
        elif weekday == 5:
            return '星期五'
        elif weekday == 6:
            return '星期六'
        else:
            return '星期日'


def format_time():
    hour = i.hour
    return hour


def week_deal(weekday):
    if weekday == 1:
        weekday = '星期一'
    elif weekday == 2:
        weekday = '星期二'
    elif weekday == 3:
        weekday = '星期三'
    elif weekday == 4:
        weekday = '星期四'
    elif weekday == 5:
        weekday = '星期五'
    elif weekday == 6:
        weekday = '星期六'
    else:
        weekday = '星期日'

    return weekday
if __name__ == '__main__':
    print(format_month())
