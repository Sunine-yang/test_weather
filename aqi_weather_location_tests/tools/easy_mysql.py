#-*-coding:GBK -*-
import datetime
import time
import pymysql
from tools.logger import Logger
from tools.read_yaml import ReadYaml
class EasyMysql:
   
    def __init__(self,service):
        self.logger=Logger.report_logger()
        self.read_yaml = ReadYaml.read_yaml(service)[service]
    def reConndb(self):

        # ���ݿ��������Թ��ܺ����ӳ�ʱ���ܵ�DB����
        _conn_status = True
        _max_retries_count = 10  # ����������Դ���
        _conn_retries_count = 0  # ��ʼ���Դ���
        _conn_timeout = 30  # ���ӳ�ʱʱ��Ϊ3��
        while _conn_status and _conn_retries_count <= _max_retries_count:
            try:
                print('�������ݿ���..')
                conn = pymysql.connect(host=self.read_yaml["host"],
                                       user=self.read_yaml["user"],
                                       password=self.read_yaml["password"],
                                       port=self.read_yaml["port"],
                                       db=self.read_yaml["db"],
                                       charset=self.read_yaml["charset"], connect_timeout=_conn_timeout)
                _conn_status = False  # ���conn�ɹ���_statusΪ����ΪFalse���˳�ѭ��������db���Ӷ���
                return conn
            except:
                _conn_retries_count += 1
                print(_conn_retries_count)
                print('�������ݿ������쳣')
                time.sleep(3)  # ��Ϊ���Կ�Ч��
            continue

    def query_one(self, sql):
        global cursor
        try:

            cursor = self.reConndb().cursor()
            start = datetime.datetime.now()
            self.logger.info('���ݿ����ӳɹ�')
            self.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            query_result = cursor.fetchone()
            self.logger.info('���ݲ�ѯ���')
            end = datetime.datetime.now()
            time_reault=end-start
            print(time_reault)
            self.logger.info('���ݿ��ѯ��ʱ %s'%(time_reault))
            cursor.close()
            self.reConndb().close()
            return query_result
        except:
            return None




    def query_all(self, sql):
        global cursor
        try:
            cursor = self.reConndb().cursor()
            start = datetime.datetime.now()
            self.logger.info('���ݿ����ӳɹ�')
            self.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            query_result = cursor.fetchall()
            self.logger.info('���ݲ�ѯ���')
            end = datetime.datetime.now()
            time_reault = end - start
            print(time_reault)
            self.logger.info('���ݿ��ѯ��ʱ %s' % (time_reault))
            cursor.close()
            self.reConndb().close()
            return query_result
        except:
            return None



if __name__ == '__main__':

    a=EasyMysql('guangzhou').query_all("SELECT * FROM xy_w2_city_crawl_china_list  WHERE cityCode in"
                                       " (SELECT city_id from xy_w2_pm25 where isvalid='1')")
    print(a)