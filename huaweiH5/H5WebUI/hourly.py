import datetime
import time
from common.common_page import Share
from log.Log import logger
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_driver import UtilWebDriver
from util.regular_deal import get_time, get_tmp, last_long, hourly_per, hourly_tmp, \
    hourly_wind, hourly_gust, hourly_vis


class HourlyPage(FindElement):
    def __init__(self):
        super(HourlyPage, self).__init__()
        self.driver = UtilWebDriver.get_driver()
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        # 天气文字描述 实况当前温度 天气预警信息 最高温度 最低温度
        time.sleep(2)
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/hourly.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/hourly.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4')
        self.driver.implicitly_wait(10)
        time.sleep(2)

    # 检查顶部天气预警横幅
    # def hourly_warn_top(self):
    #     try:
    #         today_data = Share().today_data()
    #         time.sleep(1)
    #         a = Share().warn_top(today_data[2])
    #     except BaseException:
    #         print('调用公共页面的检查顶部预警横幅失败！')
    #         logger.info('调用公共页面的检查顶部预警横幅失败！')
    #     else:
    #         print('调用公共页面的检查顶部预警横幅成功')
    #         logger.info('调用公共页面的检查顶部预警横幅成功')
    #         if a == 1:
    #             return 1
    #         else:
    #             return 2

    # 主卡片顶部信息,现在气温 与 实况实时气温
    def card_title(self):
        try:
            today_data = Share().today_data()
            time.sleep(1)
            # 逐小时预报
            title = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/h2')
            # 天气变化文字描述
            txt = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/p')
            # 现在的温度
            now_tmp = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(2)').get_attribute(
                    'textContent'))
        except BaseException:
            print('逐小时主卡片标题或天气变化文字描述或者当前温度 获取失败！')
            logger.info('逐小时主卡片标题或天气变化文字描述或者当前温度 获取失败！')
        else:
            print(f'逐小时主卡片标题显示为：{title},天气变化文字描述为：{txt}, 现在的气温为:{now_tmp}，对比温度为：{today_data[1]}')
            logger.info(f'逐小时主卡片标题显示为：{title},天气变化文字描述为：{txt}, 现在的气温为:{now_tmp}，对比温度为：{today_data[1]}')
            if title == '逐小时预报' and today_data[0] in txt and today_data[1] == now_tmp:
                return 1
            else:
                return 2

    # 判断温度显示与温度折线图对应关系
    def hour_list(self):
        """
        这个方法主要用于判断逐小时主卡片上的温度显示和温度与折线图之间是否呈对应关系

        温度越高，折线图的标点就越高
        在网页中，我发现有一个cr属性在控制折线图标点的高低，cr值越大，折线图的标点就越低
        所以：
        将原始数据，25个小时的温度和cr值分别一一对应起来做成键值对放在列表中
        再将25个小时的温度和cr分别放在两个列表中排序，然后以键值对的形式放在列表中
        然后把原始数据按照温度这个键值给它排个序
        最后来一波判断，看这两个列表中的字典内容是否一致

        :return:1 is True,2 is False
        """
        try:
            # 温度
            tmp1 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(2)').get_attribute(
                    'textContent'))
            tmp2 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(4)').get_attribute(
                    'textContent'))
            tmp3 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(6)').get_attribute(
                    'textContent'))
            tmp4 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(8)').get_attribute(
                    'textContent'))
            tmp5 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(10)').get_attribute(
                    'textContent'))
            tmp6 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(12)').get_attribute(
                    'textContent'))
            tmp7 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(14)').get_attribute(
                    'textContent'))
            tmp8 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(16)').get_attribute(
                    'textContent'))
            tmp9 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(18)').get_attribute(
                    'textContent'))
            tmp10 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(20)').get_attribute(
                    'textContent'))
            tmp11 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(22)').get_attribute(
                    'textContent'))
            tmp12 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(24)').get_attribute(
                    'textContent'))
            tmp13 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(26)').get_attribute(
                    'textContent'))
            tmp14 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(28)').get_attribute(
                    'textContent'))
            tmp15 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(30)').get_attribute(
                    'textContent'))
            tmp16 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(32)').get_attribute(
                    'textContent'))
            tmp17 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(34)').get_attribute(
                    'textContent'))
            tmp18 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(36)').get_attribute(
                    'textContent'))
            tmp19 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(38)').get_attribute(
                    'textContent'))
            tmp20 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(40)').get_attribute(
                    'textContent'))
            tmp21 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(42)').get_attribute(
                    'textContent'))
            tmp22 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(44)').get_attribute(
                    'textContent'))
            tmp23 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(46)').get_attribute(
                    'textContent'))
            tmp24 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(48)').get_attribute(
                    'textContent'))
            tmp25 = get_tmp(
                self.driver.find_element_by_css_selector('#hour_trend > svg > g > text:nth-child(50)').get_attribute(
                    'textContent'))

            # 浮点3
            spot1 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(1)').get_attribute(
                'cy')
            spot2 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(3)').get_attribute(
                'cy')
            spot3 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(5)').get_attribute(
                'cy')
            spot4 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(7)').get_attribute(
                'cy')
            spot5 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(9)').get_attribute(
                'cy')
            spot6 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(11)').get_attribute(
                'cy')
            spot7 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(13)').get_attribute(
                'cy')
            spot8 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(15)').get_attribute(
                'cy')
            spot9 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(17)').get_attribute(
                'cy')
            spot10 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(19)').get_attribute(
                'cy')
            spot11 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(21)').get_attribute(
                'cy')
            spot12 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(23)').get_attribute(
                'cy')
            spot13 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(25)').get_attribute(
                'cy')
            spot14 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(27)').get_attribute(
                'cy')
            spot15 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(29)').get_attribute(
                'cy')
            spot16 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(31)').get_attribute(
                'cy')
            spot17 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(33)').get_attribute(
                'cy')
            spot18 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(35)').get_attribute(
                'cy')
            spot19 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(37)').get_attribute(
                'cy')
            spot20 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(39)').get_attribute(
                'cy')
            spot21 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(41)').get_attribute(
                'cy')
            spot22 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(43)').get_attribute(
                'cy')
            spot23 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(45)').get_attribute(
                'cy')
            spot24 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(47)').get_attribute(
                'cy')
            spot25 = self.driver.find_element_by_css_selector(
                '#hour_trend > svg > g > circle:nth-child(49)').get_attribute(
                'cy')

            tmplist = [tmp1, tmp2, tmp3, tmp4, tmp5, tmp6, tmp7, tmp8, tmp9, tmp10, tmp11, tmp12, tmp13, tmp14, tmp15,
                       tmp16, tmp17, tmp18, tmp19, tmp20, tmp21, tmp22, tmp23, tmp24, tmp25]

            spotlist = [spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, spot10, spot11, spot12, spot13,
                        spot14, spot15, spot16, spot17, spot18, spot19, spot20, spot21, spot22, spot23, spot24, spot25]

            # 原始数据，放在字典，列表中
            dictlist1 = []
            for i, x, y in zip(range(1, 26), tmplist, spotlist):
                dictlist1.append({'tmp': x, 'spot': y})

            tmplist.sort()
            spotlist.sort(reverse=True)
            new_tmplist = tmplist
            new_spotlist = spotlist

            # 温度排序，点 排序，然后依次放到字典，列表中
            dictlist2 = []
            for i, x, y in zip(range(1, 26), new_tmplist, new_spotlist):
                dictlist2.append({'tmp': x, 'spot': y})

            # 按照温度，给原始数据排个序
            dictlist1.sort(key=lambda x: x["tmp"])

            num = 0
            for z, c in zip(dictlist1, dictlist2):
                if z == c:
                    num = num + 1

        except BaseException:
            print('判断温度显示与温度折线图对应关系失败，需要检查此模块代码！')
            logger.info('判断温度显示与温度折线图对应关系失败，需要检查此模块代码！')
        else:
            print(f'判断温度显示与温度折线图对应关系计数器需要为25，计数器实际为：{num}')
            logger.info(f'判断温度显示与温度折线图对应关系计数器需要为25，计数器实际为：{num}')
            if num == 25:
                return 1
            else:
                return 2

    # 判断底部时间是否显示正常
    def timelist(self):
        # 横部 时间列表
        # 现在
        tran_now = self.get_attr('xpath', '//*[@id="hour_list"]/li[1]/span', what='textContent')
        # 现在+1
        tran_time1 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[2]/span', what='textContent'))
        tran_time2 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[3]/span', what='textContent'))
        tran_time3 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[4]/span', what='textContent'))
        tran_time4 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[5]/span', what='textContent'))
        tran_time5 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[6]/span', what='textContent'))
        tran_time6 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[7]/span', what='textContent'))
        tran_time7 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[8]/span', what='textContent'))
        tran_time8 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[9]/span', what='textContent'))
        tran_time9 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[10]/span', what='textContent'))
        tran_time10 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[11]/span', what='textContent'))
        tran_time11 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[12]/span', what='textContent'))
        tran_time12 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[13]/span', what='textContent'))
        tran_time13 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[14]/span', what='textContent'))
        tran_time14 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[15]/span', what='textContent'))
        tran_time15 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[16]/span', what='textContent'))
        tran_time16 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[17]/span', what='textContent'))
        tran_time17 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[18]/span', what='textContent'))
        tran_time18 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[19]/span', what='textContent'))
        tran_time19 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[20]/span', what='textContent'))
        tran_time20 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[21]/span', what='textContent'))
        tran_time21 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[22]/span', what='textContent'))
        tran_time22 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[23]/span', what='textContent'))
        tran_time23 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[24]/span', what='textContent'))
        tran_time24 = get_time(self.get_attr('xpath', '//*[@id="hour_list"]/li[25]/span', what='textContent'))

        time1 = datetime.datetime.now() + datetime.timedelta(hours=1)
        time2 = datetime.datetime.now() + datetime.timedelta(hours=2)
        time3 = datetime.datetime.now() + datetime.timedelta(hours=3)
        time4 = datetime.datetime.now() + datetime.timedelta(hours=4)
        time5 = datetime.datetime.now() + datetime.timedelta(hours=5)
        time6 = datetime.datetime.now() + datetime.timedelta(hours=6)
        time7 = datetime.datetime.now() + datetime.timedelta(hours=7)
        time8 = datetime.datetime.now() + datetime.timedelta(hours=8)
        time9 = datetime.datetime.now() + datetime.timedelta(hours=9)
        time10 = datetime.datetime.now() + datetime.timedelta(hours=10)
        time11 = datetime.datetime.now() + datetime.timedelta(hours=11)
        time12 = datetime.datetime.now() + datetime.timedelta(hours=12)
        time13 = datetime.datetime.now() + datetime.timedelta(hours=13)
        time14 = datetime.datetime.now() + datetime.timedelta(hours=14)
        time15 = datetime.datetime.now() + datetime.timedelta(hours=15)
        time16 = datetime.datetime.now() + datetime.timedelta(hours=16)
        time17 = datetime.datetime.now() + datetime.timedelta(hours=17)
        time18 = datetime.datetime.now() + datetime.timedelta(hours=18)
        time19 = datetime.datetime.now() + datetime.timedelta(hours=19)
        time20 = datetime.datetime.now() + datetime.timedelta(hours=20)
        time21 = datetime.datetime.now() + datetime.timedelta(hours=21)
        time22 = datetime.datetime.now() + datetime.timedelta(hours=22)
        time23 = datetime.datetime.now() + datetime.timedelta(hours=23)
        time24 = datetime.datetime.now() + datetime.timedelta(hours=24)

        num = 0
        if tran_now == '现在':
            num += 1
            print(1)
        if str(tran_time1) == str(int(time1.strftime('%H'))):
            num += 1
            print(2)
        if str(tran_time2) == str(int(time2.strftime('%H'))):
            num += 1
            print(3)
        if str(tran_time3) == str(int(time3.strftime('%H'))):
            num += 1
            print(4)
        if str(tran_time4) == str(int(time4.strftime('%H'))):
            num += 1
            print(5)
        if str(tran_time5) == str(int(time5.strftime('%H'))):
            num += 1
            print(6)
        if str(tran_time6) == str(int(time6.strftime('%H'))):
            num += 1
            print(7)
        if str(tran_time7) == str(int(time7.strftime('%H'))):
            num += 1
            print(8)
        if str(tran_time8) == str(int(time8.strftime('%H'))):
            num += 1
            print(9)
        if str(tran_time9) == str(int(time9.strftime('%H'))):
            num += 1
            print(10)
        if str(tran_time10) == str(int(time10.strftime('%H'))):
            num += 1
            print(11)
        if str(tran_time11) == str(int(time11.strftime('%H'))):
            num += 1
            print(12)
        if str(tran_time12) == str(int(time12.strftime('%H'))):
            num += 1
            print(13)
        if str(tran_time13) == str(int(time13.strftime('%H'))):
            num += 1
            print(14)
        if str(tran_time14) == str(int(time14.strftime('%H'))):
            num += 1
            print(15)
        if str(tran_time15) == str(int(time15.strftime('%H'))):
            num += 1
            print(16)
        if str(tran_time16) == str(int(time16.strftime('%H'))):
            num += 1
            print(17)
        if str(tran_time17) == str(int(time17.strftime('%H'))):
            num += 1
            print(18)
        if str(tran_time18) == str(int(time18.strftime('%H'))):
            num += 1
            print(19)
        if str(tran_time19) == str(int(time19.strftime('%H'))):
            num += 1
            print(20)
        if str(tran_time20) == str(int(time20.strftime('%H'))):
            num += 1
            print(21)
        if str(tran_time21) == str(int(time21.strftime('%H'))):
            num += 1
            print(22)
        if str(tran_time22) == str(int(time22.strftime('%H'))):
            num += 1
            print(23)
        if str(tran_time23) == str(int(time23.strftime('%H'))):
            num += 1
            print(24)
        if str(tran_time24) == str(int(time24.strftime('%H'))):
            num += 1
            print(25)

        if num == 25:
            return 1
        else:
            return 2

    # 天气各项数据卡片图标检查
    def hourly_weather_item_icon(self):
        try:
            # 体感温度
            feel = self.get_attr('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[1]/span[1]/img', what='src')
            # 降水概率
            rainpro = self.get_attr('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[2]/span[1]/img', what='src')
            # 风
            wind = self.get_attr('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[3]/span[1]/img', what='src')
            # 湿度
            humidity = self.get_attr('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[4]/span[1]/img', what='src')
            # 风速
            gust = self.get_attr('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[1]/span[1]/img', what='src')
            # 露点
            dew_temp = self.get_attr('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[2]/span[1]/img', what='src')
            # 能见度
            vis = self.get_attr('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[3]/span[1]/img', what='src')
            # 云量
            cloud = self.get_attr('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[4]/span[1]/img', what='src')

        except BaseException:
            print('逐小时 数据卡片图标元素src获取失败！')
            logger.info('逐小时 数据卡片图标元素src获取失败！')
        else:
            print('天气各项数据卡片图标元素src获取成功！')
            logger.info('天气各项数据卡片图标元素src获取成功！')

            wea_icon_src = ConfRead.conf_return('weather_icon_src.conf')

            feel_conf = wea_icon_src.get('today_weather_item_icon', 'feel_src')
            print(f'读取的配置文件feel为：{feel_conf}')
            logger.info(f'读取的配置文件feel为：{feel_conf}')

            rainpro_conf = wea_icon_src.get('today_weather_item_icon', 'rainpro_src')
            print(f'读取的配置文件rainpro为：{rainpro_conf}')
            logger.info(f'读取的配置文件rainpro为：{rainpro_conf}')

            wind_conf = wea_icon_src.get('today_weather_item_icon', 'wind_src')
            print(f'读取的配置文件wind为：{wind_conf}')
            logger.info(f'读取的配置文件wind为：{wind_conf}')

            humidity_conf = wea_icon_src.get('today_weather_item_icon', 'humidity_src')
            print(f'读取的配置文件humidity为：{humidity_conf}')
            logger.info(f'读取的配置文件humidity为：{humidity_conf}')

            gust_conf = wea_icon_src.get('today_weather_item_icon', 'gust_src')
            print(f'读取的配置文件gust为：{gust_conf}')
            logger.info(f'读取的配置文件gust为：{gust_conf}')

            dew_temp_conf = wea_icon_src.get('today_weather_item_icon', 'dew_temp_src')
            print(f'读取的配置文件dew_temp为：{dew_temp_conf}')
            logger.info(f'读取的配置文件dew_temp为：{dew_temp_conf}')

            vis_conf = wea_icon_src.get('today_weather_item_icon', 'vis_src')
            print(f'读取的配置文件vis为：{vis_conf}')
            logger.info(f'读取的配置文件vis为：{vis_conf}')

            cloud_conf = wea_icon_src.get('today_weather_item_icon', 'cloud_src')
            print(f'读取的配置文件cloud为：{cloud_conf}')
            logger.info(f'读取的配置文件cloud为：{cloud_conf}')

            # 添加计数器
            num = 0

            if feel == feel_conf:
                num = num + 1
            if rainpro == rainpro_conf:
                num = num + 1
            if wind == wind_conf:
                num = num + 1
            if humidity == humidity_conf:
                num = num + 1
            if gust == gust_conf:
                num = num + 1
            if dew_temp == dew_temp_conf:
                num = num + 1
            if vis == vis_conf:
                num = num + 1
            if cloud == cloud_conf:
                num = num + 1

            print(f'doday_weather_item_icon计数器计数为：{num}')
            logger.info(f'today_weather_item_icon计数器计数为：{num}')

            if num == 8:
                return 1
            else:
                return 2

    # 天气各项数据卡片数据检查
    def hourly_weather_item_data(self):
        try:
            today_data = Share().today_data()
            time.sleep(1)
            tmp = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[1]/span[2]')
            # 体感温度纯数字
            tmp_data = hourly_tmp(tmp)
            # 体感温度符号 ℃
            tmp_last = last_long(tmp, 1)

            rain = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[2]/span[2]')
            # 降雨 纯数字
            rain_data = hourly_per(rain)
            # 降雨 符号 %
            rain_last = last_long(rain, 1)

            wind = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[3]/span[2]')
            # 风等级 纯数字
            wind_data = hourly_wind(wind)
            # 风 级
            wind_last = last_long(wind, 1)

            humidity = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[4]/span[2]')
            # 湿度 纯数字
            humidity_data = hourly_per(humidity)
            # 湿度 符号 %
            humidity_last = last_long(humidity, 1)

            gust = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[1]/span[2]')
            # 风速 纯数字
            gust_data = hourly_gust(gust)
            # 风速 单位 km/h
            gust_last = last_long(gust, 4)

            dew_temp = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[2]/span[2]')
            # 露点 纯数字
            dew_temp_data = hourly_tmp(dew_temp)
            # 露点 单位 ℃
            dew_temp_last = last_long(dew_temp, 1)

            vis = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[3]/span[2]')
            # 能见度 纯数字
            vis_data = hourly_vis(vis)
            # 能见度 单位km
            vis_last = last_long(vis, 2)

            cloud = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[4]/span[2]')
            # 云量 纯数字
            cloud_data = hourly_per(cloud)
            # 云量 符号 %
            cloud_last = last_long(cloud, 1)
        except BaseException:
            print('逐小时 天气数据获取失败！')
            logger.info('逐小时 天气数据获取失败！')

        else:
            print(f'逐小时 天气数据获取成功，体感温度：{tmp},'
                  f'降雨概率：{rain},'
                  f'风向：{wind},'
                  f'湿度：{humidity},'
                  f'风速：{gust},'
                  f'露点：{dew_temp},'
                  f'能见度：{vis},'
                  f'云量：{cloud}')
            logger.info(f'逐小时 天气数据获取成功，体感温度：{tmp},'
                        f'降雨概率：{rain},'
                        f'风向：{wind},'
                        f'湿度：{humidity},'
                        f'风速：{gust},'
                        f'露点：{dew_temp},'
                        f'能见度：{vis},'
                        f'云量：{cloud}')

            num = 0
            if today_data[1] - 5 <= tmp_data <= today_data[1] + 5:
                num = num + 1
            if 0 <= rain_data <= 100:
                num = num + 1
            if 0 <= wind_data <= 13:
                num = num + 1
            if 0 <= humidity_data <= 100:
                num = num + 1
            if 0 <= gust_data <= 220:
                num = num + 1
            if -20 <= dew_temp_data <= 35:
                num = num + 1
            if 0 <= vis_data <= 30:
                num = num + 1
            if 0 <= cloud_data <= 100:
                num = num + 1

            if tmp_last == '℃':
                num = num + 1
            if rain_last == '%':
                num = num + 1
            if wind_last == '级':
                num = num + 1
            if humidity_last == '%':
                num = num + 1
            if gust_last == 'km/h':
                num = num + 1
            if dew_temp_last == '℃':
                num = num + 1
            if vis_last == 'km':
                num = num + 1
            if cloud_last == '%':
                num = num + 1

            if num == 16:
                return 1
            else:
                return 2

    # 天气各项数据卡片文字描述检查
    def hourly_weather_item_txt(self):
        try:

            # 体感温度
            feel = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[1]/span[3]')

            # 降水概率
            rainpro = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[2]/span[3]')

            # 风
            wind_data = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[3]/span[3]')
            wind = last_long(wind_data, 1)

            # 湿度
            humidity = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[1]/li[4]/span[3]')

            # 阵风
            gust = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[1]/span[3]')

            # 露点温度
            dew_temp = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[2]/span[3]')

            # 能见度
            vis = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[3]/span[3]')

            # 云量
            cloud = self.get_text('xpath', '//*[@id="page_container"]/div[7]/ul[2]/li[4]/span[3]')


        except BaseException:
            print('天气各项数据卡片文字描述元素获取失败！')
            logger.info('天气各项数据卡片文字描述元素获取失败！')
        else:
            print('天气各项数据卡片文字描述元素获取成功！')
            print(f'体感温度：{feel},降水概率：{rainpro},风：{wind},湿度：{humidity},阵风：{gust},露点温度：{dew_temp},能见度：{vis},云量：{cloud}')
            logger.info(
                f'体感温度：{feel},降水概率：{rainpro},风：{wind},湿度：{humidity},阵风：{gust},露点温度：{dew_temp},能见度：{vis},云量：{cloud}')

            num = 0

            if feel == '体感温度':
                num = num + 1
            if rainpro == '降水概率':
                num = num + 1
            if wind == '风':
                num = num + 1
            if humidity == '湿度':
                num = num + 1
            if gust == '阵风':
                num = num + 1
            if dew_temp == '露点温度':
                num = num + 1
            if vis == '能见度':
                num = num + 1
            if cloud == '云量':
                num = num + 1

            if num == 8:
                return 1
            else:
                return 2

    # hourly 生活资讯
    def hourly_operate_wrapper(self):
        try:
            i = Share().operate_wrapper()
        except BaseException:
            print('从共用页面里->调用生活资讯页面失败！')
            logger.info('从共用页面里->调用生活资讯页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly 生活资讯 更多 页面
    def hourly_operate_wrapper_more(self):
        try:
            i = Share().operate_wrapper_more(300)
        except BaseException:
            print('从共用页面里->调用生活资讯 更多 页面失败！')
            logger.info('从共用页面里->调用生活资讯 更多 页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly周边景区
    def hourly_scenic(self):
        try:
            i = Share().scenic()
        except BaseException:
            print('从共用页面里->调用周边景区失败！')
            logger.info('从共用页面里->调用周边景区失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly周边景区点击景点切换城市
    def hourly_scenic_click(self):
        try:
            i = Share().scenic_click()
        except BaseException:
            print('从共用页面里->调用周边景区点击景点切换城市失败！')
            logger.info('从共用页面里->调用周边景区点击景点切换城市失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 周边景区二级页面
    def hourly_scenic_page_two(self):
        try:
            i = Share().scenic_page_two()
        except BaseException:
            print('从共用页面里->调用周边景区二级页面失败！')
            logger.info('从共用页面里->调用周边景区二级页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly生活指南
    def hourly_living_guide(self):
        try:
            i = Share().living_guide()
        except BaseException:
            print('从共用页面里->调用生活指南失败！')
            logger.info('从共用页面里->调用生活指南失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly生活指南二级页面
    def hourly_living_guide_page_two(self):
        try:
            i = Share().living_guide_page_two(400)
        except BaseException:
            print('从共用页面里->调用生活指南二级页面失败！')
            logger.info('从共用页面里->调用生活指南二级页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly 天气快讯
    def hourly_reptile_news(self):
        try:
            i = Share().reptile_news()
        except BaseException:
            print('从共用页面里->调用天气快讯页面失败！')
            logger.info('从共用页面里->调用天气快讯页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # today 天气快讯 更多页面
    def hourly_reptile_news_more(self):
        try:
            i = Share().reptile_news_more(400)
        except BaseException:
            print('从共用页面里->调用天气快讯 更多页面失败！')
            logger.info('从共用页面里->调用天气快讯 更多页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly 天气纵览
    def hourly_news_video(self):
        try:
            i = Share().news_video()
        except BaseException:
            print('从共用页面里->调用天气纵览页面失败！')
            logger.info('从共用页面里->调用天气纵览页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly 天气纵览 更多页面
    def hourly_news_video_more(self):
        try:
            i = Share().news_video_more(740)
        except BaseException:
            print('从共用页面里->调用天气纵览 更多页面失败！')
            logger.info('从共用页面里->调用天气纵览 更多页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly 猜你喜欢
    def hourly_weather_news(self):
        try:
            i = Share().weather_news()
        except BaseException:
            print('从共用页面里->调用猜你喜欢页面失败！')
            logger.info('从共用页面里->调用猜你喜欢页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # hourly 猜你喜欢 更多页面
    def hourly_weather_news_more(self):
        try:
            i = Share().weather_news_more(500)
        except BaseException:
            print('从共用页面里->调用猜你喜欢 更多页面失败！')
            logger.info('从共用页面里->调用猜你喜欢 更多页面失败！')
        else:
            if i == 1:
                return 1
            else:
                return 2

    # hourly版权信息
    def hourly_copyright(self):
        try:
            i = Share().copyright()
        except BaseException:
            print('从共用页面里->调用验证页面底部版权信息失败！')
            logger.info('从共用页面里->调用验证页面底部版权信息失败！')
        else:
            if i == 1:
                return 1
            else:
                return 2

    # # 页面跳转 实况天气 多天预报 生活指数 新闻资讯
    # def page_jump(self):
    #     try:
    #         today_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/img', what='src')
    #         today_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/span', what='textContent')
    #
    #         days_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/img', what='src')
    #         days_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/span', what='textContent')
    #
    #         comfor_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/img', what='src')
    #         comfor_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/span', what='textContent')
    #
    #         news_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/img', what='src')
    #         news_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/span', what='textContent')
    #     except BaseException:
    #         print('页面跳转 实况天气 多天预报 生活指数 新闻资讯 获取内容失败！')
    #         logger.info('页面跳转 实况天气 多天预报 生活指数 新闻资讯 获取内容失败！')
    #     else:
    #         num = 0
    #         if today_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_now.svg' \
    #                 and days_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_days.svg' \
    #                 and comfor_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_live.svg' \
    #                 and news_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_news.svg':
    #             num += 1
    #             print(1)
    #         if today_txt == '实况天气' and days_txt == '多天预报' and comfor_txt == '生活指数' and news_txt == '新闻资讯':
    #             num += 1
    #             print(2)
    #
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[1]/img')
    #         time.sleep(1)
    #         page_url = self.driver.current_url
    #         if 'today' in page_url:
    #             num += 1
    #             print(3)
    #         self.driver.back()
    #         time.sleep(1)
    #
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[2]/img')
    #         time.sleep(1)
    #         page_url = self.driver.current_url
    #         if 'days' in page_url:
    #             num += 1
    #             print(4)
    #         self.driver.back()
    #         time.sleep(1)
    #
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[3]/img')
    #         time.sleep(1)
    #         page_url = self.driver.current_url
    #         if 'comfor' in page_url:
    #             num += 1
    #             print(5)
    #         self.driver.back()
    #         time.sleep(1)
    #
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[4]/img')
    #         time.sleep(1)
    #         page_url = self.driver.current_url
    #         if 'news' in page_url:
    #             num += 1
    #             print(6)
    #         self.driver.back()
    #         time.sleep(1)
    #
    #         if num == 6:
    #             return 1
    #         else:
    #             return 2


if __name__ == '__main__':
    pass
    a = HourlyPage()
    # print(a.top_warn())
    # print(a.card_title())
    # print(a.hour_list())
    # print(a.hourly_weather_item_icon())
    # print(a.hourly_weather_item_data())
    # print(a.hourly_weather_item_txt())
    # print(a.hourly_operate_wrapper())
    # print(a.hourly_living_guide())
    # print(a.hourly_living_guide_page_two())
    # print(a.hourly_reptile_news())
    # print(a.hourly_news_video())
    # print(a.hourly_weather_news())
    # print(a.hourly_copyright())
    print(a.timelist())
