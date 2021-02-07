from util.conf_read import ConfRead
from util.testSQL import TestSQL


class ForeignDateDeal:
    def __init__(self):
        self.sql = TestSQL()

    def foreign_date(self, numstr):
        data = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'foreign_big', 'sql1') + numstr)
        accucode = []  # 城市编码
        cityname = []  # 城市名
        province = []  # 省份
        country = []  # 国家
        timezone = []  # 时区
        geolong = []  # 经度
        geolat = []  # 纬度

        for i in data:
            accucode.append(i[1])
            cityname.append(i[2])
            province.append(i[3])
            country.append(i[4])
            timezone.append(i[5])
            geolong.append(i[6])
            geolat.append(i[7])

        # print(accucode)
        # print(cityname)
        # print(geolong)
        # print(geolat)
        # print(timezone)
        return accucode, cityname, province, country, timezone, geolong, geolat

    def foreign_dic_code_name(self):
        data = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'foreign_big', 'sql1') + ' limit 0, 10000')
        dic_code_name = {}
        dic_citycode = {}
        dic_province = {}
        dic_timeZone = {}
        for name in data:
            # 键值对， 城市编码：城市名
            dic_code_name[name[1]] = name[2]

        for code in data:
            # 键值对， 城市码（accucode）：城市编码
            dic_citycode[code[1]] = code[1]

        for pro in data:
            # 键值对， 城市码（accucode）：省市区
            dic_province[pro[1]] = pro[3]

        for zone in data:
            # 键值对， 城市码（accucode）：时区
            dic_timeZone[zone[1]] = zone[5]

        return dic_code_name, dic_citycode, dic_province, dic_timeZone

        # def foreign_dic_citycode(self, numstr):

    #     citycode = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'foreign_big', 'sql1') + numstr)
    #     dic = {}
    #     for i in citycode:
    #         # 键值对， 城市码（accucode）：城市编码
    #         dic[i[1]] = i[1]
    #     return dic

    # def foreign_dic_province(self, numstr):
    #     citycode = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'foreign_big', 'sql1') + numstr)
    #     dic = {}
    #     for i in citycode:
    #         # 键值对， 城市码（accucode）：省市区
    #         dic[i[1]] = i[3]
    #     return dic

    # def china_dic_timeZone(self, numstr):
    #     citycode = self.sql.do_sql(ConfRead.conf_get('sql.conf', 'foreign_big', 'sql1') + numstr)
    #     dic = {}
    #     for i in citycode:
    #         # 键值对， 城市码（accucode）：时区
    #         dic[i[1]] = i[5]
    #     return dic


if __name__ == '__main__':
    a = ForeignDateDeal()


