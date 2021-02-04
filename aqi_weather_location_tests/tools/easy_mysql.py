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

        # 数据库连接重试功能和连接超时功能的DB连接
        _conn_status = True
        _max_retries_count = 10  # 设置最大重试次数
        _conn_retries_count = 0  # 初始重试次数
        _conn_timeout = 30  # 连接超时时间为3秒
        while _conn_status and _conn_retries_count <= _max_retries_count:
            try:
                print('连接数据库中..')
                conn = pymysql.connect(host=cls.read_yaml["host"],
                                       user=cls.read_yaml["user"],
                                       password=cls.read_yaml["password"],
                                       port=cls.read_yaml["port"],
                                       db=cls.read_yaml["db"],
                                       charset=cls.read_yaml["charset"], connect_timeout=_conn_timeout)
                _conn_status = False  # 如果conn成功则_status为设置为False则退出循环，返回db连接对象
                return conn
            except:
                _conn_retries_count += 1
                print(_conn_retries_count)
                print('连接数据库连接异常')
                time.sleep(3)  # 此为测试看效果
            continue
    @classmethod
    def query_one(cls, sql):
        global cursor
        try:

            cursor = cls.reConndb().cursor()
            start = datetime.datetime.now()
            cls.logger.info('数据库连接成功')
            cls.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            query_result = cursor.fetchone()
            cls.logger.info('数据查询完成')
            end = datetime.datetime.now()
            time_reault=end-start
            print(time_reault)
            cls.logger.info('数据库查询耗时 %s'%(time_reault))
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
            cls.logger.info('数据库连接成功')
            cls.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            query_result = cursor.fetchall()
            cls.logger.info('数据查询完成')
            end = datetime.datetime.now()
            time_reault = end - start
            print(time_reault)
            cls.logger.info('数据库查询耗时 %s' % (time_reault))
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