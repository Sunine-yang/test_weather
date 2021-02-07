import re
from log.Log import logger


# 取数字
def get_num(string):
    num = re.findall(r"\d+\.?\d*", string)
    return "".join(num)


# 取°C前面的内容
def get_tmp_num(string):
    num = re.findall(r"^.*?(?=°C)", string)
    return "".join(num)


# 取空气质量文字描述
def get_api(string):
    num = re.findall(r"\s(.*)", string)
    return "".join(num)


def get_icon_src(string):
    num = re.findall(r"(?<=res/img/weather_icon/ic_weather_).+(?=.svg)", string)
    return "".join(num)


# 提取字符串最后两个字符
def last_two(string):
    num = re.findall(r".{2}$", string)
    return "".join(num)


def last_nineteen(string):
    num = re.findall(r".{19}$", string)
    return "".join(num)


def last_five(string):
    num = re.findall(r".{5}$", string)
    return "".join(num)


def last_long(string, long):
    num = re.findall(fr".{{{long}}}$", string)
    return "".join(num)


# 百度信息流来源 图片地址 .png@ jpeg@
def baidu_get_jpeg(string):
    num = re.findall(r'.{4}@', string)
    return "".join(num)


# 气象在线信息流来源 图片地址 .png .jpg
def weatherol_get_jpg(string):
    num = re.findall(r'.{4}$', string)
    return "".join(num)


def get_time(string):
    num = re.findall(r'^.*?(?=:)', string)
    return int("".join(num))


def get_tmp(string):
    num = re.findall(r'^.*?(?=°)', string)
    return int("".join(num))


def hourly_tmp(string):
    num = re.findall(r'^.*?(?=℃)', string)
    return int("".join(num))


def hourly_per(string):
    num = re.findall(r'^.*?(?=%)', string)
    return int("".join(num))


def hourly_wind(string):
    num = re.findall(r'^.*?(?=级)', string)
    return int("".join(num))


def hourly_gust(string):
    num = re.findall(r'^.*?(?=km/h)', string)
    return int("".join(num))


def hourly_vis(string):
    num = re.findall(r'^.*?(?=km)', string)
    return int("".join(num))


def common_last_tmp(string):
    num = re.findall(r'(?<=\/).+?(?=℃)', string)
    return int("".join(num))


def common_first_tmp(string):
    num = re.findall(r'^.*?(?=/)', string)
    return int("".join(num))


# 获取四个字符
def get_scenic_name(string):
    num = re.findall(r'^.{4}', string)
    return "".join(num)


# 取第一个字符
def first_one(string):
    num = re.findall(r'^.', string)
    return "".join(num)


def daily_date(string):
    num = re.findall(r'^.*?(?= )', string)
    return "".join(num)


def daily_day(string):
    num = re.findall(r'(?<=月).+?(?=日)', string)
    return int("".join(num))


def daily_month(string):
    num = re.findall(r'^.*?(?=月)', string)
    return int("".join(num))


def daily_rain(string):
    num = re.findall(r'^.*?(?=mm)', string)
    return int("".join(num))

def days_tmp_max(string):
    num = re.findall(r'^.*?(?=°/)', string)
    return int("".join(num))

def days_tmp_min(string):
    num = re.findall(r'(?<=/).+?(?=°)', string)
    return int("".join(num))

def sun_come_deal(string):
    num = re.findall(r'(?<=日出时间).+?(?= )', string)
    return "".join(num)

def sun_left_deal(string):
    num = re.findall(r'(?<=日落时间).+?(?= )', string)
    return "".join(num)

def moon_come_deal(string):
    num = re.findall(r'(?<=月出时间,).+?(?=,)', string)
    return "".join(num)

def moon_left_deal(string):
    num = re.findall(r'(?<=月落时间,).*', string)
    return "".join(num)

def moon_left_day_deal(string):
    num = re.findall(r'^..', string)
    return "".join(num)

def life_card(string):
    num = re.findall(r'^.*?(?=：)', string)
    return "".join(num)


if __name__ == '__main__':
    print(daily_date('12月17日'))
