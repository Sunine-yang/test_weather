#-*-coding:GBK -*-
import datetime
import time
import pymysql
from tools.logger import Logger
from tools.read_yaml import ReadYaml
class EasyMysql:
    def __init__(self,service):
        self.service=ReadYaml.read_yaml()[service]['sql_name']
        self.logger=Logger.report_logger()
        self.read_yaml=ReadYaml.read_yaml()[self.service]


    def reConndb(self):
        print(self.read_yaml)
        # 数据库连接重试功能和连接超时功能的DB连接
        _conn_status = True
        _max_retries_count = 10  # 设置最大重试次数
        _conn_retries_count = 0  # 初始重试次数
        _conn_timeout = 30  # 连接超时时间为3秒
        while _conn_status and _conn_retries_count <= _max_retries_count:
            try:
                print('连接数据库中..')
                conn = pymysql.connect(host=self.read_yaml["host"],
                                       user=self.read_yaml["user"],
                                       password=self.read_yaml["password"],
                                       port=self.read_yaml["port"],
                                       db=self.read_yaml["db"],
                                       charset=self.read_yaml["charset"], connect_timeout=_conn_timeout)
                _conn_status = False  # 如果conn成功则_status为设置为False则退出循环，返回db连接对象
                return conn
            except:
                _conn_retries_count += 1
                print(_conn_retries_count)
                print('连接数据库连接异常')
                time.sleep(3)  # 此为测试看效果
            continue

    def query_one(self, sql):
        global cursor
        try:

            cursor = self.reConndb().cursor()
            start = datetime.datetime.now()
            self.logger.info('数据库连接成功')
            self.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            query_result = cursor.fetchone()
            self.logger.info('数据查询完成')
            end = datetime.datetime.now()
            time_reault=end-start
            self.logger.info('数据库查询耗时 %s'%(time_reault))
            return query_result
        except:
            return None
        finally:
            cursor.close()
            self.reConndb().close()


    def query_all(self, sql):
        global cursor
        try:
            cursor = self.reConndb().cursor()
            start = datetime.datetime.now()
            self.logger.info('数据库连接成功')
            self.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            query_result = cursor.fetchall()
            self.logger.info('数据查询完成')
            end = datetime.datetime.now()
            time_reault = end - start
            self.logger.info('数据库查询耗时 %s' % (time_reault))
            return query_result
        except:
            return None
        finally:
            cursor.close()
            self.reConndb().close()

    def update(self, sql):
        try:
            cursor = self.reConndb().cursor()
            self.reConndb().ping(reconnect=True)
            cursor.execute(sql)
            self.reConndb().commit()
            cursor.close()
            self.reConndb().close()
            return True
        except:
            return None

if __name__ == '__main__':

    a=EasyMysql('shanghai').query_all("SELECT t.city_id,b.accuCode, b.cityname, b.province, t.aqi, t.aqi_level  FROM xy_w2_city_crawl_china_list b INNER JOIN xy_w2_pm25 t ON b.citycode = t.city_id WHERE t.isvalid = '1' AND t.crawl_time IS NOT NULL AND t.aqi!='0' AND t.city_id IS NOT NULL AND public_time > 1612085434000 ORDER BY (t.aqi+0)")
    print(a)