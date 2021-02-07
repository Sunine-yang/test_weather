# coding=<encoding name> ： # coding=utf-8

import pymysql


class TestSQL:
    def __init__(self):
        # 链接数据库
        self.conn = pymysql.connect(
            host='139.9.217.1',
            user='testDbUser',
            password='Bestweather_zmtq^#@2020',
            port=4108,
            db='weather',
            charset='utf8'
        )

    def do_sql(self, sql):
        # 必须有一个游标对象， 用来给数据库发送sql语句，创建游标
        cur = self.conn.cursor()
        self.conn.ping(reconnect=True)
        cur.execute(sql)
        self.conn.commit()
        data = cur.fetchall()
        # 关闭游标
        cur.close()
        # 关闭连接
        self.conn.close()
        return data


if __name__ == '__main__':
    a = TestSQL()
    sql = "SELECT accuCode , province , timeZone , accuCode, geoLong, geoLat, cityCode FROM `xy_w2_city_crawl_china_list` WHERE citycode NOT LIKE 'G%' AND citycode NOT LIKE 'C%'"
    data = a.do_sql(sql)

    for i in data:
        print(i)
