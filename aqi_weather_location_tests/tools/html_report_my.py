#-*-coding:GBK -*-
import smtplib, os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Test_mail:
    def __init__(self, data):
        self.msg = MIMEMultipart()
        self.user = 'zhouyang@droi.com'
        self.to_user = 'zhouyang@droi.com'
        self.msg["Subject"] = '运行失败'
        self.msg["From"] = self.user
        self.msg["To"] = self.to_user
        self.pas = 'zhou123...'
        self.msg.attach(MIMEText(data))

    def smtp_on(self):

        s = smtplib.SMTP('smtp.263.net', 465, timeout=30)
        s.login(self.user, self.pas)
        s.sendmail(self.user, ['zhouyang@droi.com'], self.msg.as_string())
        s.close()

