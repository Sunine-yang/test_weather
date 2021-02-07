import datetime
from dateutil.parser import parse

import pytz


def foreign_condition(re, timezone):
    # 时间戳
    d = datetime.datetime.fromtimestamp(re / 1000)
    str1 = d.strftime("%H")

    ist = pytz.timezone(timezone)
    now = datetime.datetime.now(tz=ist)
    str2 = now.strftime("%H")

    a = int(str1)
    b = int(str2)

    c = int(str1) - int(str2)
    if c == 0:
        return 1
    else:
        return 2


def foreign_ts_nine(re, timezone):
    ist = pytz.timezone(timezone)
    now = datetime.datetime.now(tz=ist)
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
