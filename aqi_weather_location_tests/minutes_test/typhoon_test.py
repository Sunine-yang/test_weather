#-*-coding:GBK -*-

from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from analysis.url_data import Url_data
from lib.test_api import TestAPI
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from tools.test_html import Test_mail



class Typhoon_Minutes:
    def __init__(self):
        self.result_check = Result_check('weather_typhoon')
        self.read_ymal=ReadYaml.read_yaml()
    def weather_typhoon_list_check(self):
        print('typhoon  start...........................')



        try:
            data_num = Url_data().read_data('typhoon_list.txt')
            url_list = TestAPI.get_location(self.read_ymal["weather_typhoon_list"]).json()
            typhoon_list = ['data', 'typhoonList', 'resultinfo', "servertime"]
            key_query = self.key_check(typhoon_list, str(url_list))
            code = self.result_check.comparison_check(
                TestAPI.get_location(self.read_ymal["weather_typhoon_list"]).status_code, 200, '| 状态码:(%s/%s)')
            ZtyphoonList = self.result_check.comparison_check(len(url_list), 4, '| ZtyphoonList 字节长度:(%s/%s)')
            typhoonList = self.result_check.comparison_check(len(url_list["data"]["typhoonList"]), 5,
                                                             't| typhoonList 字节长度:(%s/%s)')
            resultinfo = self.result_check.comparison_check(url_list["resultinfo"], 'OK', '| resultinfo:(%s/%s)')
            servertime = self.result_check.comparison_none_check(url_list["servertime"], '| servertime:(%s)')
            resultcode = self.result_check.comparison_check(url_list["resultcode"], '0', '| resultcode:(%s/%s)')
            typhoon_list_data = key_query + code + ZtyphoonList + typhoonList + resultinfo + servertime + resultcode
            if typhoon_list_data != '':
                self.result_check.list_data.append('台风列表接口 |' + typhoon_list_data)
            else:
                pass
            for i in range(len(url_list["data"]["typhoonList"])):
                result = '%s,%s |' % (
                url_list["data"]["typhoonList"][i]["nameZh"], '20' + url_list["data"]["typhoonList"][i]["code"])
                typhoon_lists = ['nameZh', 'nameEn', 'code', "number"]
                key_info = self.key_check(typhoon_lists, str(url_list["data"]["typhoonList"][i]))
                typhoonList_l = self.result_check.comparison_check(len(url_list["data"]["typhoonList"][i]), 4,
                                                                   result + '| typhoonList 字节长度:(%s/%s)')
                nameZh = self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameZh"],
                                                            str(data_num[-i - 1][2]), '| nameZh:(%s/%s)')
                nameEn = self.result_check.comparison_check(url_list["data"]["typhoonList"][i]["nameEn"],
                                                            str(data_num[-i - 1][1]), '| nameEn:(%s/%s)')
                codes = self.result_check.comparison_in_check(url_list["data"]["typhoonList"][i]["code"],
                                                              str(data_num[-i - 1][3]), '| code:(%s/%s)')
                number = self.result_check.comparison_none_check(url_list["data"]["typhoonList"][i]["number"],
                                                                 '| number:(%s)')
                typhoon_list_datas = key_info + typhoonList_l + nameEn + nameZh + codes + number
                if typhoon_list_datas != '':
                    self.result_check.list_data.append(
                        '%s,%s |' % (data_num[-i - 1][2], '20' + str(data_num[-i - 1][3]) + typhoon_list_datas))
                else:
                    print('正确')
        except Exception as e:
            self.result_check.logger.warning(str(e))

    def test_weather_typhoon_check(self):
        import random
        global url_report
        numbers=random.randint(2001,2023)
        Url_data().write_weather_typhoon_data(numbers)
        try:
            sql_data = EasyMysql.query_all(self.read_ymal["minute_test"]["sql_typhoon_track"] % ('20'+str(numbers)))
            weather_url = Url_data().read_weather_typhoon_data(numbers)

            url_report = '%s,%s |' % (sql_data[0][3], '20' + str(numbers))
            list_key_datas = ['data', 'track', 'changeTrender', 'endTime', 'source', 'startTime',
                              'sustainedTime']
            key_query = self.key_check(list_key_datas, str(weather_url))
            number = self.result_check.comparison_check(len(weather_url["data"]["track"]), len(sql_data),
                                                        '| 数据条数:(%d/%d)')
            time_c = self.result_check.comparison_check(weather_url["data"]["changeTrender"][0]["time"],
                                                        int(str(Data_analysis.time_disposes(sql_data[0][5])) + '000'),
                                                        '| 起编时间:(%s/%s)')
            total_len = self.result_check.comparison_check(len(weather_url), 4,
                                                           '| 总字段长度:(%s/%s)')
            data = self.result_check.comparison_check(len(weather_url["data"]), 10,
                                                      '| data 字段长度:(%s/%s)')
            resultcode = self.result_check.comparison_check(weather_url["resultcode"], '0',
                                                            '| resultcode:(%s/%s)')
            resultinfo = self.result_check.comparison_check(weather_url["resultinfo"], 'OK',
                                                            '| resultinfo:(%s/%s)')
            endTime = self.result_check.comparison_none_check(weather_url["data"]["endTime"],
                                                              '| endTime:(%s)')
            source = self.result_check.comparison_none_check(weather_url["data"]["source"],
                                                             '| source:(%s)')
            startTime = self.result_check.comparison_none_check(weather_url["data"]["startTime"],
                                                                '| startTime:(%s)')
            sustainedTime = self.result_check.comparison_none_check(weather_url["data"]["sustainedTime"],
                                                                    '| sustainedTime:(%s)')
            self.typhoon_track_check(weather_url, sql_data)
            typhoon_result = number + time_c + total_len + data + resultcode + resultinfo + endTime + source + startTime + sustainedTime + key_query
            if typhoon_result != '':
                self.result_check.list_data.append('%s |' % url_report + typhoon_result)
            else:
                print(url_report +'检验通过')
        except Exception as e:
            print(e)
            self.result_check.logger.warning(e)

    def typhoon_track_check(self, weather_url, sql_data):
        for a in range(len(weather_url["data"]["track"])):
            url_report_time = url_report + sql_data[a][5]
            list_key_data = ['track', 'changeTrender', 'time', 'centralPressure', 'latitude', 'level',
                             'longitude',
                             'typhoonNameZh', "typhoonNameEn", "typhoonId", "windSpeed", "longitude"]
            key_track = self.key_check(list_key_data, str(weather_url["data"]))
            track = self.result_check.comparison_check(len(weather_url["data"]["track"][a]), 6,
                                                       '| track 字段长度:(%s/%s)')
            centralPressure = self.result_check.comparison_check(
                weather_url["data"]["track"][a]["centralPressure"], sql_data[a][11],
                '| centralPressure:(%s/%s)')
            latitude = self.result_check.comparison_check(weather_url["data"]["track"][a]["latitude"],
                                                          sql_data[a][8],
                                                          '| latitude:(%s/%s)')
            level = self.result_check.comparison_check(weather_url["data"]["track"][a]["level"], sql_data[a][9],
                                                       '| level:(%s/%s)')
            longitude = self.result_check.comparison_check(weather_url["data"]["track"][a]["longitude"],
                                                           sql_data[a][7],
                                                           '| longitude:(%s/%s)')
            windSpeed = self.result_check.comparison_check(weather_url["data"]["track"][a]["windSpeed"],
                                                           sql_data[a][10],
                                                           '| windSpeed speed:(%s/%s)')
            time_d = self.result_check.comparison_check(weather_url["data"]["track"][a]["time"], int(
                str(Data_analysis.time_disposes(sql_data[a][5])) + '000'),
                                                        '| time:(%s/%s)')
            typhoonId = self.result_check.comparison_check(weather_url["data"]["typhoonId"], sql_data[a][1],
                                                           '| typhoonId:(%s/%s)')
            typhoonNameEn = self.result_check.comparison_check(weather_url["data"]["typhoonNameEn"],
                                                               sql_data[a][2],
                                                               '| typhoonNameEn:(%s/%s)')
            typhoonNameZh = self.result_check.comparison_check(weather_url["data"]["typhoonNameZh"],
                                                               sql_data[a][3],
                                                               '| typhoonNameZh:(%s/%s)')
            typhoon_track = track + centralPressure + latitude + level + longitude + windSpeed + time_d + typhoonId + typhoonNameEn + typhoonNameZh + key_track
            if typhoon_track != '':
                self.result_check.list_data.append('%s |' % url_report_time + typhoon_track)
            else:
                print(url_report_time + '检查通过')
    def key_check(self,list_data,data):
        result_data = []
        for i in range(len(list_data)):
            if list_data[i] in data:
                pass
            else:
                result = '%s 不存在' % list_data[i]
                result_data.append(result)
        if result_data == []:
            return ''
        else:
            data = str(result_data).replace("[", ' ')
            data1 = data.replace("]", '')
            data2 = data1.replace(",", " | ")
            return data2

    def typhoon_start(self):
        global a
        a=0
        self.weather_typhoon_list_check()
        self.test_weather_typhoon_check()
        if a == 0:
            if self.result_check.list_data == []:
                a = 0
            else:
                a += 1
                self.weather_typhoon_list_check()
                self.test_weather_typhoon_check()
                self.result_check.all_wait_data()
                Test_mail("[vivo]-[广州]-[API]-[台风]-[第%d次]" % a, 'weather_typhoon').smtp_on()
                self.result_check.list_data.clear()
        elif a > 4:
            for i in range(5):
                if self.result_check.list_data == []:
                    a = 0
                    break
                else:
                    a += 1
                    self.result_check.list_data.append('***********************')
                    self.weather_typhoon_list_check()
                    self.test_weather_typhoon_check()
                    self.result_check.all_wait_data()
            Test_mail("[vivo]-[广州]-[API]-[台风列表/详情]-[第%d次]" % a, 'weather_typhoon').smtp_on()
            Data_analysis.data_delete('weather_typhoon')
            self.result_check.list_data.clear()
        elif  a >= 1 and a <= 4:
            if self.result_check.list_data == []:
                a = 0
            else:
                a+=1
                self.weather_typhoon_list_check()
                self.test_weather_typhoon_check()
                self.result_check.all_wait_data()
                Test_mail("[vivo]-[广州]-[API]-[台风]-[第%d次]"%a , 'weather_typhoon').smtp_on()
                self.result_check.list_data.clear()




if __name__ == '__main__':
    Typhoon_Minutes().typhoon_start()