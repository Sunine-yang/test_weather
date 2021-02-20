#-*-coding:GBK -*-
import smtplib, os,sys,socket
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
socket.setdefaulttimeout(0.003)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from path_data import Path_data
from email.header import Header

class Test_mail:
    def __init__(self, title):
        self.msg = MIMEMultipart()
        self.user = 'zhouyang@droi.com'
        self.pas = 'zhou123...'
        self.to_user = ['zhouyang@droi.com','niuyuanman@droi.com','liuyang@droi.com','chengyu@droi.com']
        self.msg["Subject"] = title
        self.msg["From"] = Header('周阳', 'utf-8')  # 发送者
        self.msg["To"] =Header('监控组', 'utf-8')  # 发送者
    def smtp_on(self, path):
        try:
            absolute_path = Path_data.get_path() + r"\test_data\test_log_report\%s.txt" % path
            with open(absolute_path, 'r', encoding='utf8') as f:
                self.msg.attach(MIMEText(f.read()))
            s = smtplib.SMTP_SSL('smtp.263.net', 465, timeout=30)
            s.login(self.user, self.pas)
            s.sendmail(self.user, self.to_user, self.msg.as_string())
            s.close()
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')
    def error_mail(self,data):
        try:
            self.msg.attach(MIMEText(data))
            s = smtplib.SMTP_SSL('smtp.263.net', 465, timeout=30)
            s.login(self.user, self.pas)
            s.sendmail(self.user,self.user, self.msg.as_string())
            s.close()
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')
#,'liuyang@droi.com','chengyu@droi.com','niuyuanman@droi.com'
if __name__ == '__main__':
    Test_mail('test').error_mail('guangzhou_location')
