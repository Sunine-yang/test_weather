from getpathInfo import text_Path

text_aaa = text_Path()
def big_erro():
    f = open(text_aaa+'big_erro.txt', mode='w', encoding="utf-8")
    f.write('【大颗粒接口-接口错误无返回】')
    f.close()


def big_base():
    f = open(text_aaa+'big_base.txt', mode='w', encoding="utf-8")
    f.write('【大颗粒接口-城市信息】')
    f.close()


def big_condition():
    f = open(text_aaa+'big_condition.txt', mode='w', encoding="utf-8")
    f.write('【大颗粒接口-实况天气】')
    f.close()


def big_dailys():
    f = open(text_aaa+'big_dailys.txt', mode='w', encoding="utf-8")
    f.write('【大颗粒接口-多天预报】')
    f.close()


def big_aqidays():
    f = open(text_aaa+'big_aqidays.txt', mode='w', encoding="utf-8")
    f.write('【大颗粒接口-多天空气质量】')
    f.close()


def big_aqi():
    f = open(text_aaa+'big_aqi.txt', mode='w', encoding="utf-8")
    f.write('【大颗粒接口-实时空气质量】')
    f.close()


def big_alarm():
    f = open(text_aaa+'big_alarm.txt', mode='w', encoding="utf-8")
    f.write('【大颗粒接口-预警】')
    f.close()


def big_hourlys():
    f = open(text_aaa+'big_hourlys.txt', mode='w', encoding="utf-8")
    f.write('【大颗粒接口-小时天气】')
    f.close()


def big_liveInfos():
    f = open(text_aaa+'big_liveInfos.txt', mode='w', encoding="utf-8")
    f.write('【大颗粒接口-生活指数】')
    f.close()


def do_txt():
    big_erro()
    big_base()
    big_condition()
    big_dailys()
    big_aqidays()
    big_aqi()
    big_alarm()
    big_hourlys()
    big_liveInfos()
