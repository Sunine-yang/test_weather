# coding=<encoding name> ： # coding=utf-8
import yagmail
import yaml

from getpathInfo import text_Path
from text.del_txt import re_geo_city_erro_num
from util.conf_read import ConfRead


class SendEG:
    def __init__(self, path=text_Path(), name='广州'):
        self.a = path
        self.name = name

    def alarm(self):
        with open(self.a + "geo_alarm.txt", 'a+', encoding="utf-8") as f:
            f.seek(0)
            big_alarm = len(f.readlines())
        if big_alarm >= 1:
            with open(self.a + "geo_alarm.txt", 'r+', encoding="utf-8") as f:
                return f.readlines(), big_alarm
        else:
            return ['预警-无错误\n'], 0

    def aqi(self):
        with open(self.a + "geo_aqi.txt", 'a+', encoding="utf-8") as f:
            f.seek(0)
            big_aqi = len(f.readlines())
        if big_aqi >= 1:
            with open(self.a + "geo_aqi.txt", 'r+', encoding="utf-8") as f:
                return f.readlines(), big_aqi
        else:
            return ['实时空气质量-无错误\n'], 0

    def aqidays(self):
        with open(self.a + "geo_aqidays.txt", 'a+', encoding="utf-8") as f:
            f.seek(0)
            big_aqidays = len(f.readlines())
        if big_aqidays >= 1:
            with open(self.a + "geo_aqidays.txt", 'r+', encoding="utf-8") as f:
                return f.readlines(), big_aqidays
        else:
            return ['多天空气质量-无错误\n'], 0

    def base(self):
        with open(self.a + "geo_base.txt", 'a+', encoding="utf-8") as f:
            f.seek(0)
            big_base = len(f.readlines())
        if big_base >= 1:
            with open(self.a + "geo_base.txt", 'r+', encoding="utf-8") as f:
                return f.readlines(), big_base
        else:
            return ['城市信息-无错误\n'], 0

    def condition(self):
        with open(self.a + "geo_condition.txt", 'a+', encoding="utf-8") as f:
            f.seek(0)
            big_condition = len(f.readlines())
        if big_condition >= 1:
            with open(self.a + "geo_condition.txt", 'r+', encoding="utf-8") as f:
                return f.readlines(), big_condition
        else:
            return ['实况天气-无错误\n'], 0

    def dailys(self):
        with open(self.a + "geo_dailys.txt", 'a+', encoding="utf-8") as f:
            f.seek(0)
            big_dailys = len(f.readlines())
        if big_dailys >= 1:
            with open(self.a + "geo_dailys.txt", 'r+', encoding="utf-8") as f:
                return f.readlines(), big_dailys
        else:
            return ['多天预报-无错误\n'], 0

    def erro(self):
        with open(self.a + "geo_erro.txt", 'a+', encoding="utf-8") as f:
            f.seek(0)
            big_erro = len(f.readlines())
        if big_erro >= 1:
            with open(self.a + "geo_erro.txt", 'r+', encoding="utf-8") as f:
                return f.readlines(), big_erro
        else:
            return ['接口错误无返回-无错误\n'], 0

    def hourlys(self):
        with open(self.a + "geo_hourlys.txt", 'a+', encoding="utf-8") as f:
            f.seek(0)
            big_hourlys = len(f.readlines())
        if big_hourlys >= 1:
            with open(self.a + "geo_hourlys.txt", 'r+', encoding="utf-8") as f:
                return f.readlines(), big_hourlys
        else:
            return ['小时天气-无错误\n'], 0

    def houraqi(self):
        with open(self.a + "geo_houraqi.txt", mode='a+', encoding='utf-8') as f:
            f.seek(0)
            houraqi = len(f.readlines())
        if houraqi >= 1:
            with open(self.a + "geo_houraqi.txt", mode='r+', encoding='utf-8') as f:
                return f.readlines(), houraqi
        else:
            return ['小时空气质量-无错误\n'], 0

    def erro_city_num(self):
        with open(self.a + "geo_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
            f.seek(0)
            erro_num = len(f.readlines())
        return erro_num

    def send_email_geo(self, path=text_Path()):
        a1, num1 = self.alarm()
        a1.insert(0, f'【----------预警信息-模块错误----------】[{num1}]\n')
        a2, num2 = self.aqi()
        a2.insert(0, f'【----------实时空气质量-模块错误----------】[{num2}]\n')
        a3, num3 = self.aqidays()
        a3.insert(0, f'【----------多天空气质量-模块错误----------】[{num3}]\n')
        a4, num4 = self.base()
        a4.insert(0, f'【---------- 城市信息-模块错误----------】[{num4}]\n')
        a5, num5 = self.condition()
        a5.insert(0, f'【----------实况天气-模块错误----------】[{num5}]\n')
        a6, num6 = self.dailys()
        a6.insert(0, f'【----------多天预报-模块错误----------】[{num6}]\n')
        a7, num7 = self.erro()
        a7.insert(0, f'【----------接口错误无返回----------】[{num7}]\n')
        a8, num8 = self.hourlys()
        a8.insert(0, f'【----------小时天气-模块错误----------】[{num8}]\n')
        a9, num9 = self.houraqi()
        a9.insert(0, f'【---------- 小时空气质量-模块错误----------】[{num9}]\n')

        big = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
        big_num = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
        b = ''.join(big)

        e_name = ConfRead.conf_get('email.conf', 'email', 'email')
        e_r_name = yaml.load(e_name, Loader=yaml.FullLoader)
        # 链接邮箱服务器
        yag = yagmail.SMTP(user="lizechen@droi.com", password="a124578", host='smtp.263.net')
        # 邮箱正文
        contents_big = b
        # 发送邮件
        yag.send(e_r_name, f'[vivo]-[{self.name}]-[数据]-[国内站点]-[大颗粒-经纬度]-[{self.erro_city_num()}]', contents_big)
        re_geo_city_erro_num(path)


if __name__ == '__main__':
    pass
