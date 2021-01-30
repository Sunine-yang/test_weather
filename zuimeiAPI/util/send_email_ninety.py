# coding=<encoding name>= ： # coding=utf-8
import yagmail
import yaml

from getpathInfo import text_Path
from text.del_txt import re_nine_city_erro_num
from util.conf_read import ConfRead

a = text_Path()


def ninety_erro():
    with open(a + "ninety_erro.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        ninety = len(f.readlines())
    if ninety >= 1:
        with open(a + "ninety_erro.txt", mode='r+', encoding='utf-8') as f:
            return f.readlines(), ninety
    else:
        return ['九十日-接口异常和天数判断-无错误\n'], 0


def ninety_empty():
    with open(a + "ninety_empty.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        ninety = len(f.readlines())
    if ninety >= 1:
        with open(a + "ninety_empty.txt", mode='r+', encoding='utf-8') as f:
            return f.readlines(), ninety
    else:
        return ['九十日-字段是否为空-无错误\n'], 0

def erro_city_num():
    with open(a + "nine_erro_citynum.txt", mode='a+', encoding='utf-8') as f:
        f.seek(0)
        erro_num = len(f.readlines())
    return erro_num

def send_email_nine():
    e_name = ConfRead.conf_get('email.conf', 'email', 'email')
    e_r_name = yaml.load(e_name, Loader=yaml.FullLoader)
    b1, num_nine1 = ninety_erro()
    b1.insert(0, f'【----------九十日-接口异常和天数判断-模块错误----------】[{num_nine1}]\n')
    b2, num_nine2 = ninety_empty()
    b2.insert(0, f'【----------九十日-字段是否为空-模块错误----------】[{num_nine2}]\n')
    nine = b1 + b2
    nine_num = num_nine1 + num_nine2
    c = ''.join(nine)
    yag = yagmail.SMTP(user="lizechen@droi.com", password="a124578", host='smtp.263.net')
    # 邮箱正文

    contents_ninety = c

    # file1 = log_path + 'logs.log'
    # 发送邮件

    yag.send(e_r_name, f'[vivo]-[广州]-[数据]-[九十日]-[{erro_city_num()}]', contents_ninety)
    re_nine_city_erro_num()

if __name__ == '__main__':
    send_email_nine()
