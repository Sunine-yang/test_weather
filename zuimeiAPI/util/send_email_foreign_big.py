# coding=<encoding name> ： # coding=utf-8
import yagmail
import yaml

from getpathInfo import text_Path
from text.del_txt import re_foreign_big_num
from util.conf_read import ConfRead




class SendEFB:
    def __init__(self, path=text_Path(), name='广州'):
        self.a = path
        self.name = name

    # def deal_file():
    #     with open(a + "foreign_big_base1.txt", 'a+', encoding="UTF-8") as base1:
    #         base1.seek(0)
    #         base1_re = base1.readlines()
    #     with open(a + "foreign_big_base2.txt", 'a+', encoding="UTF-8") as base2:
    #         base2.seek(0)
    #         base2_re = base2.readlines()
    #     with open(a + "foreign_big_base3.txt", 'a+', encoding="UTF-8") as base3:
    #         base3.seek(0)
    #         base3_re = base3.readlines()
    #     with open(a + "foreign_big_base4.txt", 'a+', encoding="UTF-8") as base4:
    #         base4.seek(0)
    #         base4_re = base4.readlines()
    #     with open(a + "foreign_big_base5.txt", 'a+', encoding="UTF-8") as base5:
    #         base5.seek(0)
    #         base5_re = base5.readlines()
    #     # 合并
    #     with open(a + "foreign_big_base.txt", 'a+', encoding="UTF-8") as base:
    #         base.seek(0)
    #         base.writelines(base1_re + base2_re + base3_re + base4_re + base5_re)
    #
    #     with open(a + "foreign_big_condition1.txt", 'a+', encoding="UTF-8") as con1:
    #         con1.seek(0)
    #         con1_re = con1.readlines()
    #     with open(a + "foreign_big_condition2.txt", 'a+', encoding="UTF-8") as con2:
    #         con2.seek(0)
    #         con2_re = con2.readlines()
    #     with open(a + "foreign_big_condition3.txt", 'a+', encoding="UTF-8") as con3:
    #         con3.seek(0)
    #         con3_re = con3.readlines()
    #     with open(a + "foreign_big_condition4.txt", 'a+', encoding="UTF-8") as con4:
    #         con4.seek(0)
    #         con4_re = con4.readlines()
    #     with open(a + "foreign_big_condition5.txt", 'a+', encoding="UTF-8") as con5:
    #         con5.seek(0)
    #         con5_re = con5.readlines()
    #     # 合并
    #     with open(a + "foreign_big_condition.txt", 'a+', encoding="UTF-8") as con:
    #         con.seek(0)
    #         con.writelines(con1_re + con2_re + con3_re + con4_re + con5_re)
    #
    #
    #     with open(a + "foreign_big_dailys1.txt", 'a+', encoding="UTF-8") as dailys1:
    #         dailys1.seek(0)
    #         dailys1_re = dailys1.readlines()
    #     with open(a + "foreign_big_dailys2.txt", 'a+', encoding="UTF-8") as dailys2:
    #         dailys2.seek(0)
    #         dailys2_re = dailys2.readlines()
    #     with open(a + "foreign_big_dailys3.txt", 'a+', encoding="UTF-8") as dailys3:
    #         dailys3.seek(0)
    #         dailys3_re = dailys3.readlines()
    #     with open(a + "foreign_big_dailys4.txt", 'a+', encoding="UTF-8") as dailys4:
    #         dailys4.seek(0)
    #         dailys4_re = dailys4.readlines()
    #     with open(a + "foreign_big_dailys5.txt", 'a+', encoding="UTF-8") as dailys5:
    #         dailys5.seek(0)
    #         dailys5_re = dailys5.readlines()
    #     # 合并
    #     with open(a + "foreign_big_dailys.txt", 'a+', encoding="UTF-8") as dailys:
    #         dailys.seek(0)
    #         dailys.writelines(dailys1_re + dailys2_re + dailys3_re + dailys4_re + dailys5_re)
    #
    #     with open(a + "foreign_big_erro1.txt", 'a+', encoding="UTF-8") as erro1:
    #         erro1.seek(0)
    #         erro1_re = erro1.readlines()
    #     with open(a + "foreign_big_erro2.txt", 'a+', encoding="UTF-8") as erro2:
    #         erro2.seek(0)
    #         erro2_re = erro2.readlines()
    #     with open(a + "foreign_big_erro3.txt", 'a+', encoding="UTF-8") as erro3:
    #         erro3.seek(0)
    #         erro3_re = erro3.readlines()
    #     with open(a + "foreign_big_erro4.txt", 'a+', encoding="UTF-8") as erro4:
    #         erro4.seek(0)
    #         erro4_re = erro4.readlines()
    #     with open(a + "foreign_big_erro5.txt", 'a+', encoding="UTF-8") as erro5:
    #         erro5.seek(0)
    #         erro5_re = erro5.readlines()
    #     # 合并
    #     with open(a + "foreign_big_erro.txt", 'a+', encoding="UTF-8") as erro:
    #         erro.seek(0)
    #         erro.writelines(erro1_re + erro2_re + erro3_re + erro4_re + erro5_re)
    #
    #     with open(a + "foreign_big_hourlys1.txt", 'a+', encoding="UTF-8") as hour1:
    #         hour1.seek(0)
    #         hour1_re = hour1.readlines()
    #     with open(a + "foreign_big_hourlys2.txt", 'a+', encoding="UTF-8") as hour2:
    #         hour2.seek(0)
    #         hour2_re = hour2.readlines()
    #     with open(a + "foreign_big_hourlys3.txt", 'a+', encoding="UTF-8") as hour3:
    #         hour3.seek(0)
    #         hour3_re = hour3.readlines()
    #     with open(a + "foreign_big_hourlys4.txt", 'a+', encoding="UTF-8") as hour4:
    #         hour4.seek(0)
    #         hour4_re = hour4.readlines()
    #     with open(a + "foreign_big_hourlys5.txt", 'a+', encoding="UTF-8") as hour5:
    #         hour5.seek(0)
    #         hour5_re = hour5.readlines()
    #     # 合并
    #     with open(a + "foreign_big_hourlys.txt", 'a+', encoding="UTF-8") as hour:
    #         hour.seek(0)
    #         hour.writelines(hour1_re + hour2_re + hour3_re + hour4_re + hour5_re)
    #
    #     with open(a + "foreign_big_liveinfos1.txt", 'a+', encoding="UTF-8") as live1:
    #         live1.seek(0)
    #         live1_re = live1.readlines()
    #     with open(a + "foreign_big_liveinfos2.txt", 'a+', encoding="UTF-8") as live2:
    #         live2.seek(0)
    #         live2_re = live2.readlines()
    #     with open(a + "foreign_big_liveinfos3.txt", 'a+', encoding="UTF-8") as live3:
    #         live3.seek(0)
    #         live3_re = live3.readlines()
    #     with open(a + "foreign_big_liveinfos4.txt", 'a+', encoding="UTF-8") as live4:
    #         live4.seek(0)
    #         live4_re = live4.readlines()
    #     with open(a + "foreign_big_liveinfos5.txt", 'a+', encoding="UTF-8") as live5:
    #         live5.seek(0)
    #         live5_re = live5.readlines()
    #     # 合并
    #     with open(a + "foreign_big_liveinfos.txt", 'a+', encoding="UTF-8") as live:
    #         live.seek(0)
    #         live.writelines(live1_re + live2_re + live3_re + live4_re + live5_re)

    # ====================================================================================

    def foreign_base(self):
        with open(self.a + "foreign_big_base.txt", 'a+', encoding="UTF-8") as f:
            f.seek(0)
            big_base = len(f.readlines())
        if big_base >= 1:
            with open(self.a + "foreign_big_base.txt", 'r+', encoding="UTF-8") as f:
                return f.readlines(), big_base
        else:
            return ['城市信息-无错误\n'], 0

    def foreign_condition(self):
        with open(self.a + "foreign_big_condition.txt", 'a+', encoding="UTF-8") as f:
            f.seek(0)
            big_condition = len(f.readlines())
        if big_condition >= 1:
            with open(self.a + "foreign_big_condition.txt", 'r+', encoding="UTF-8") as f:
                return f.readlines(), big_condition
        else:
            return ['实况天气-无错误\n'], 0

    def foreign_dailys(self):
        with open(self.a + "foreign_big_dailys.txt", 'a+', encoding="UTF-8") as f:
            f.seek(0)
            big_dailys = len(f.readlines())
        if big_dailys >= 1:
            with open(self.a + "foreign_big_dailys.txt", 'r+', encoding="UTF-8") as f:
                return f.readlines(), big_dailys
        else:
            return ['多天预报-无错误\n'], 0

    def foreign_erro(self):
        with open(self.a + "foreign_big_erro.txt", 'a+', encoding="UTF-8") as f:
            f.seek(0)
            big_erro = len(f.readlines())
        if big_erro >= 1:
            with open(self.a + "foreign_big_erro.txt", 'r+', encoding="UTF-8") as f:
                return f.readlines(), big_erro
        else:
            return ['接口错误无返回-无错误\n'], 0

    def foreign_hourlys(self):
        with open(self.a + "foreign_big_hourlys.txt", 'a+', encoding="UTF-8") as f:
            f.seek(0)
            big_hourlys = len(f.readlines())
        if big_hourlys >= 1:
            with open(self.a + "foreign_big_hourlys.txt", 'r+', encoding="UTF-8") as f:
                return f.readlines(), big_hourlys
        else:
            return ['小时天气-无错误\n'], 0

    #  =======================================================================================

    def foreign_erro_city_num(self):
        with open(self.a + "foreign_big_erro_citynum.txt", mode='a+', encoding='UTF-8') as f:
            f.seek(0)
            erro_num = len(f.readlines())
        return erro_num

    def send_email_foreign_big(self, path=text_Path()):
        a1, num1 = self.foreign_base()
        a1.insert(0, f'【---------- 城市信息-模块错误----------】[{num1}]\n')
        a2, num2 = self.foreign_condition()
        a2.insert(0, f'【----------实况天气-模块错误----------】[{num2}]\n')
        a3, num3 = self.foreign_dailys()
        a3.insert(0, f'【----------多天预报-模块错误----------】[{num3}]\n')
        a4, num4 = self.foreign_erro()
        a4.insert(0, f'【----------接口错误无返回----------】[{num4}]\n')
        a5, num5 = self.foreign_hourlys()
        a5.insert(0, f'【----------小时天气-模块错误----------】[{num5}]\n')

        big = a1 + a2 + a3 + a4 + a5
        b = ''.join(big)

        e_name = ConfRead.conf_get('email.conf', 'email', 'email')
        e_r_name = yaml.load(e_name, Loader=yaml.FullLoader)
        # 链接邮箱服务器
        yag = yagmail.SMTP(user="lizechen@droi.com", password="a124578", host='smtp.263.net')
        # 邮箱正文
        contents_big = b
        # 错误城市数量

        # 发送邮件
        yag.send(e_r_name,
                 f'[vivo]-[{self.name}]-[数据]-[国外站点]-[大颗粒-accucode]-[{self.foreign_erro_city_num()}]',
                 contents_big)
        re_foreign_big_num(path)


if __name__ == '__main__':
    pass
