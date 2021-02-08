#-*-coding:GBK -*-
import smtplib, os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from path_data import Path_data


class Test_mail:
    def __init__(self, title, path):
        self.msg = MIMEMultipart()
        self.user = 'zhouyang@droi.com'
        self.to_user = 'zhouyang@droi.com'
        self.msg["Subject"] = title
        self.msg["From"] = self.user
        self.msg["To"] = self.to_user
        self.pas = 'zhou123...'

        # self.path=os.listdir(Path_data.get_path()+"/test_data/test_log_report")
        absolute_path = Path_data.get_path() + "/test_data/test_log_report/%s.txt" % path
        #part = MIMEApplication(open(absolute_path, 'rb').read())
        #part.add_header('Content-Disposition', 'attachment', filename="%s.txt" % path)
        with open(absolute_path, 'r', encoding='utf8') as f:
            self.msg.attach(MIMEText(f.read()))
        #self.msg.attach(part)
        #Data_analysis.data_delete('test')
    def smtp_on(self):

        s = smtplib.SMTP('smtp.263.net', 465, timeout=30)
        s.login(self.user, self.pas)
        s.sendmail(self.user, ['zhouyang@droi.com','liuyang@droi.com','niuyuanman@droi.com','chengyu@droi.com'], self.msg.as_string())
        s.close()
#
if __name__ == '__main__':
    Test_mail('test','Air_Quality_Ranking').smtp_on()
