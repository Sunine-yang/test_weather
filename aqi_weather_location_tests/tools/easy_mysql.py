#-*-coding:GBK -*-
import datetime
import time
import pymysql
from tools.logger import Logger
from tools.read_yaml import ReadYaml
class EasyMysql:
    logger=Logger.report_logger()
    read_yaml=ReadYaml.read_yaml()['mysql']
    @classmethod
    def reConndb(cls):

        # ���ݿ��������Թ��ܺ����ӳ�ʱ���ܵ�DB����
        _conn_status = True
        _max_retries_count = 10  # ����������Դ���
        _conn_retries_count = 0  # ��ʼ���Դ���
        _conn_timeout = 30  # ���ӳ�ʱʱ��Ϊ3��
        while _conn_status and _conn_retries_count <= _max_retries_count:
            try:
                print('�������ݿ���..')
                conn = pymysql.connect(host=cls.read_yaml["host"],
                                       user=cls.read_yaml["user"],
                                       password=cls.read_yaml["password"],
                                       port=cls.read_yaml["port"],
                                       db=cls.read_yaml["db"],
                                       charset=cls.read_yaml["charset"], connect_timeout=_conn_timeout)
                _conn_status = False  # ���conn�ɹ���_statusΪ����ΪFalse���˳�ѭ��������db���Ӷ���
                return conn
            except:
                _conn_retries_count += 1
                print(_conn_retries_count)
                print('�������ݿ������쳣')
                time.sleep(3)  # ��Ϊ���Կ�Ч��
            continue
    @classmethod
    def query_one(cls, sql):
        global cursor
        try:

            cursor = cls.reConndb().cursor()
            start = datetime.datetime.now()
            cls.logger.info('���ݿ����ӳɹ�')
            cls.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            query_result = cursor.fetchone()
            cls.logger.info('���ݲ�ѯ���')
            end = datetime.datetime.now()
            time_reault=end-start
            print(time_reault)
            cls.logger.info('���ݿ��ѯ��ʱ %s'%(time_reault))
            return query_result
        except:
            return None
        finally:
            cursor.close()
            cls.reConndb().close()

    @classmethod
    def query_all(cls, sql):
        global cursor
        try:
            cursor = cls.reConndb().cursor()
            start = datetime.datetime.now()
            cls.logger.info('���ݿ����ӳɹ�')
            cls.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            query_result = cursor.fetchall()
            cls.logger.info('���ݲ�ѯ���')
            end = datetime.datetime.now()
            time_reault = end - start
            print(time_reault)
            cls.logger.info('���ݿ��ѯ��ʱ %s' % (time_reault))
            return query_result
        except:
            return None
        finally:
            cursor.close()
            cls.reConndb().close()
    @classmethod
    def update(cls, sql):
        try:
            cursor = cls.reConndb().cursor()
            cls.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            cls.reConndb().commit()
            cursor.close()
            cls.reConndb().close()
            return True
        except:
            return None

if __name__ == '__main__':

    a=EasyMysql.query_all("SELECT * FROM xy_w2_city_crawl_china_list  WHERE cityCode in (SELECT city_id from xy_w2_pm25 where isvalid='1')")
    print(a)