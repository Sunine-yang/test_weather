# coding=<encoding name> ： # coding=utf-8
import yagmail
import yaml

from getpathInfo import text_Path
from text.del_txt import re_foreign_live_num
from util.conf_read import ConfRead


class SendEFL:
    def __init__(self, path=text_Path(), name='广州'):
        self.a = path
        self.name = name

    def foreign_liveInfos(self):
        with open(self.a + "foreign_big_liveinfos.txt", 'a+', encoding="UTF-8") as f:
            f.seek(0)
            big_liveinfos = len(f.readlines())
        if big_liveinfos >= 1:
            with open(self.a + "foreign_big_liveinfos.txt", 'r+', encoding="UTF-8") as f:
                return f.readlines(), big_liveinfos
        else:
            return ['生活指数-无错误\n'], 0

    #  =======================================================================================

    def foreign_erro_live_city_num(self):
        with open(self.a + "foreign_live_erro_citynum.txt", mode='a+', encoding='UTF-8') as f:
            f.seek(0)
            erro_num = len(f.readlines())
        return erro_num

    def send_email_foreign_live(self, path=text_Path()):
        a6, num6 = self.foreign_liveInfos()
        a6.insert(0, f'【---------- 生活指数-模块错误----------】[{num6}]\n')

        big = a6
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
                 f'[vivo]-[{self.name}]-[数据]-[国外站点]-[生活指数][{self.foreign_erro_live_city_num()}]',
                 contents_big)
        re_foreign_live_num(path)


if __name__ == '__main__':
    pass
