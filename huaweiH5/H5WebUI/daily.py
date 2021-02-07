import random
import time
import datetime

from selenium.webdriver import ActionChains

from common.common_page import Share
from log.Log import logger

from util.check_chinese import contain_chinese_one, contain_chinese
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_date import week_deal
from util.get_driver import UtilWebDriver
from util.load_page import load_page
from util.regular_deal import daily_date, last_long, daily_month, daily_day, hourly_tmp, hourly_wind, hourly_per, \
    daily_rain, baidu_get_jpeg


class DailyPage(FindElement):
    def __init__(self):
        super(DailyPage, self).__init__()
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID

        self.cityID = cityData.get('citydata', 'cityId')
        self.driver = UtilWebDriver.get_driver()

        time.sleep(2)
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/daily.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4'
            f'&source=zm&oriId=P14')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/daily.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4'
            f'&source=zm&oriId=P14')
        time.sleep(2)

    # 检查天气预警顶部横幅
    # def daily_warn_top(self):
    #     try:
    #         today_data = Share().today_data()
    #         time.sleep(1)
    #         i = Share().warn_top(today_data[2])
    #     except BaseException:
    #         print('从共用页面里->调用天气预警顶部横幅失败！')
    #         logger.info('从共用页面里->调用天气预警顶部横幅失败！')
    #     else:
    #         if i == 1:
    #             return 1
    #         if i == 2:
    #             return 2

    # 检查 天数，日期，星期  每日 主卡片
    def daily_date_click(self):
        # 完整日期

        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[1]').click()
        time.sleep(1)
        date0 = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')
        print(date0)
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        time.sleep(1)
        date1 = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')
        print(date1)
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        time.sleep(1)
        date3 = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')
        print(date3)
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        time.sleep(1)
        date5 = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')
        print(date5)
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        time.sleep(1)
        date7 = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')
        print(date7)
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        time.sleep(1)
        date9 = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')
        print(date9)
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        time.sleep(1)
        date11 = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')
        print(date11)
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        time.sleep(1)
        date13 = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')
        print(date13)
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        self.find_element('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]').click()
        time.sleep(1)
        date15 = self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')
        print(date15)

        # 页面展示日月 选取1，3，5...
        date_month0 = str(daily_month(daily_date(date0))) + '-' + str(daily_day(daily_date(date0)))
        date_month_now = str(daily_month(daily_date(date1))) + '-' + str(daily_day(daily_date(date1)))
        date_month1 = str(daily_month(daily_date(date3))) + '-' + str(daily_day(daily_date(date3)))
        date_month3 = str(daily_month(daily_date(date5))) + '-' + str(daily_day(daily_date(date5)))
        date_month5 = str(daily_month(daily_date(date7))) + '-' + str(daily_day(daily_date(date7)))
        date_month7 = str(daily_month(daily_date(date9))) + '-' + str(daily_day(daily_date(date9)))
        date_month9 = str(daily_month(daily_date(date11))) + '-' + str(daily_day(daily_date(date11)))
        date_month11 = str(daily_month(daily_date(date13))) + '-' + str(daily_day(daily_date(date13)))
        date_month13 = str(daily_month(daily_date(date15))) + '-' + str(daily_day(daily_date(date15)))

        # 页面展示星期 选取1，3，5....
        date_week0 = last_long(date0, 3)
        date_week_now = last_long(date1, 3)
        date_week1 = last_long(date3, 3)
        date_week3 = last_long(date5, 3)
        date_week5 = last_long(date7, 3)
        date_week7 = last_long(date9, 3)
        date_week9 = last_long(date11, 3)
        date_week11 = last_long(date13, 3)
        date_week13 = last_long(date15, 3)

        # 现在+ 2days datetime 函数获取，准备断言\\\

        time0 = datetime.datetime.now() + datetime.timedelta(days=-1)
        time1 = datetime.datetime.now() + datetime.timedelta(days=2)
        time3 = datetime.datetime.now() + datetime.timedelta(days=4)
        time5 = datetime.datetime.now() + datetime.timedelta(days=6)
        time7 = datetime.datetime.now() + datetime.timedelta(days=8)
        time9 = datetime.datetime.now() + datetime.timedelta(days=10)
        time11 = datetime.datetime.now() + datetime.timedelta(days=12)
        time13 = datetime.datetime.now() + datetime.timedelta(days=14)

        # datetime 日月
        month_now = str(daily_month(datetime.datetime.now().strftime('%m月%d日'))) + '-' + str(
            daily_day(datetime.datetime.now().strftime('%m月%d日')))
        month0 = str(daily_month(time0.strftime('%m月%d日'))) + '-' + str(
            daily_day(time0.strftime('%m月%d日')))
        month1 = str(daily_month(time1.strftime('%m月%d日'))) + '-' + str(
            daily_day(time1.strftime('%m月%d日')))
        month3 = str(daily_month(time3.strftime('%m月%d日'))) + '-' + str(
            daily_day(time3.strftime('%m月%d日')))
        month5 = str(daily_month(time5.strftime('%m月%d日'))) + '-' + str(
            daily_day(time5.strftime('%m月%d日')))
        month7 = str(daily_month(time7.strftime('%m月%d日'))) + '-' + str(
            daily_day(time7.strftime('%m月%d日')))
        month9 = str(daily_month(time9.strftime('%m月%d日'))) + '-' + str(
            daily_day(time9.strftime('%m月%d日')))
        month11 = str(daily_month(time11.strftime('%m月%d日'))) + '-' + str(
            daily_day(time11.strftime('%m月%d日')))
        month13 = str(daily_month(time13.strftime('%m月%d日'))) + '-' + str(
            daily_day(time13.strftime('%m月%d日')))

        # datetime 星期
        week_now = week_deal(datetime.datetime.now().isoweekday())
        week0 = week_deal(time0.isoweekday())
        week1 = week_deal(time1.isoweekday())
        week3 = week_deal(time3.isoweekday())
        week5 = week_deal(time5.isoweekday())
        week7 = week_deal(time7.isoweekday())
        week9 = week_deal(time9.isoweekday())
        week11 = week_deal(time11.isoweekday())
        week13 = week_deal(time13.isoweekday())
        print(week_now, week0, week1)

        num = 0
        print(month_now, date_month_now, week_now, date_week_now, num)

        if month_now == date_month_now and week_now == date_week_now:
            num = num + 1

        print(num, month0, date_month0, week0, date_week0)

        if month0 == date_month0 and week0 == date_week0:
            num = num + 1
        print(num, month1, date_month1, week1, date_week1)

        if month1 == date_month1 and week1 == date_week1:
            num = num + 1
        print(num, month3, date_month3, week3, date_week3)

        if month3 == date_month3 and week3 == date_week3:
            num = num + 1
        print(num, month5, date_month5, week5, date_week5)

        if month5 == date_month5 and week5 == date_week5:
            num = num + 1
        print(num, month7, date_month7, week7, date_week7)

        if month7 == date_month7 and week7 == date_week7:
            num = num + 1
        print(num, month9, date_month9, week9, date_week9)

        if month9 == date_month9 and week9 == date_week9:
            num = num + 1
        print(num, month11, date_month11, week11, date_week11)

        if month11 == date_month11 and week11 == date_week11:
            num = num + 1
        print(num, month13, date_month13, week13, date_week13)

        if month13 == date_month13 and week13 == date_week13:
            num = num + 1

        if num == 9:
            return 1
        else:
            return 2

    # 检查 白天夜间按钮 最低最高气温 随机一天的卡片信息检查
    def daily_display(self):
        try:
            today_data = Share().today_data()
            time.sleep(1)
            night = self.find_element('xpath', '//*[@id="weather_card"]/div/div[2]/ul/li[2]')
            day = self.find_element('xpath', '//*[@id="weather_card"]/div/div[2]/ul/li[1]')
            night.click()
            time.sleep(1)
            # 温度
            tmp1 = self.find_element('xpath', '//*[@id="move_box"]/li[2]/div/div[1]/span[1]').get_attribute(
                'textContent')
            # ℃
            tmp_unit1 = self.find_element('xpath', '//*[@id="move_box"]/li[2]/div/div[1]/span[2]').get_attribute(
                'textContent')
            # 图标显示 .svg
            pic_url1 = last_long(
                self.get_attr('xpath', '//*[@id="move_box"]/li[2]/div/div[2]/div[1]/span[1]/img', what='src'), 4)
            # 天气 文字
            wea_txt1 = self.find_element('xpath', '//*[@id="move_box"]/li[2]/div/div[2]/div[1]/span[2]').get_attribute(
                'textContent')
            wea_txt1_check = contain_chinese_one(wea_txt1)

            num = 0
            if int(tmp1) == int(today_data[
                                    4]) and tmp_unit1 == '℃' and pic_url1 == '.svg' and wea_txt1_check == 1:
                num = num + 1
            print(num, tmp1, today_data[4], tmp_unit1, pic_url1, wea_txt1)

            day.click()
            time.sleep(1)
            # 温度
            tmp2 = self.find_element('xpath', '//*[@id="move_box"]/li[1]/div/div[1]/span[1]').get_attribute(
                'textContent')
            # ℃
            tmp_unit2 = self.find_element('xpath', '//*[@id="move_box"]/li[2]/div/div[1]/span[2]').get_attribute(
                'textContent')
            # 图标显示 .svg
            pic_url2 = last_long(
                self.get_attr('xpath', '//*[@id="move_box"]/li[2]/div/div[2]/div[1]/span[1]/img', what='src'), 4)
            # 天气 文字
            wea_txt2 = self.find_element('xpath', '//*[@id="move_box"]/li[2]/div/div[2]/div[1]/span[2]').get_attribute(
                'textContent')
            wea_txt2_check = contain_chinese_one(wea_txt2)

            if int(tmp2) == int(today_data[
                                    3]) and tmp_unit2 == '℃' and pic_url2 == '.svg' and wea_txt2_check == 1:
                num = num + 1
            print(num, tmp2, today_data[3], tmp_unit2, pic_url2, wea_txt2)

            for i in range(random.randint(1, 14)):
                self.click('xpath', '//*[@id="weather_card"]/div/div[1]/div[3]')
            time.sleep(1)
            # 温度
            tmp3 = self.find_element('xpath', '//*[@id="move_box"]/li[2]/div/div[1]/span[1]').get_attribute(
                'textContent')

            # ℃
            tmp_unit3 = self.find_element('xpath', '//*[@id="move_box"]/li[2]/div/div[1]/span[2]').get_attribute(
                'textContent')
            # 图标显示 .svg
            pic_url3 = last_long(
                self.get_attr('xpath', '//*[@id="move_box"]/li[2]/div/div[2]/div[1]/span[1]/img', what='src'), 4)
            # 天气 文字
            wea_txt3 = self.find_element('xpath', '//*[@id="move_box"]/li[2]/div/div[2]/div[1]/span[2]').get_attribute(
                'textContent')
            wea_txt3_check = contain_chinese_one(wea_txt3)

            print(num, tmp3, tmp_unit3, pic_url3, wea_txt3)
            if -50 <= int(tmp3) <= 50 and tmp_unit3 == '℃' and pic_url3 == '.svg' and wea_txt3_check == 1:
                num = num + 1
        except BaseException:
            print('检查 白天夜间按钮 最低最高气温 随机一天的卡片信息检查失败！检查代码!')
            logger.info('检查 白天夜间按钮 最低最高气温 随机一天的卡片信息检查失败！检查代码!')
        else:
            print(f'检查 白天夜间按钮 最低最高气温 随机一天的卡片信息检查成功，白天温度：{tmp2}，夜间温度：{tmp1}，'
                  f'天气状况等：{wea_txt3}，{wea_txt1}，src:{pic_url1},{pic_url2},{pic_url3}')
            if num == 3:
                return 1
            else:
                return 2

    # 天气详情 图标 数据 文字描述
    def daily_detail(self):
        try:
            today_data = Share().today_data()
            time.sleep(1)

            icon1 = self.get_attr('xpath', '//*[@id="weather_card"]/div/ul/li[1]/div/img', what='src')

            icon2 = self.get_attr('xpath', '//*[@id="weather_card"]/div/ul/li[2]/div/img', what='src')

            icon3 = self.get_attr('xpath', '//*[@id="weather_card"]/div/ul/li[3]/div/img', what='src')

            icon4 = self.get_attr('xpath', '//*[@id="weather_card"]/div/ul/li[4]/div/img', what='src')

            txt1 = self.get_text('xpath', '//*[@id="weather_card"]/div/ul/li[1]/div/span[2]')

            txt2 = last_long(self.get_text('xpath', '//*[@id="weather_card"]/div/ul/li[2]/div/span[2]'), 1)

            txt3 = last_long(self.get_text('xpath', '//*[@id="weather_card"]/div/ul/li[3]/div/span[2]'), 1)

            txt4 = self.get_text('xpath', '//*[@id="weather_card"]/div/ul/li[4]/div/span[2]')

            num = 0
            tmp = self.get_text('xpath', '//*[@id="weather_card"]/div/ul/li[1]/div/span[1]')
            # 体感温度纯数字
            tmp_data = hourly_tmp(tmp)
            # 体感温度符号 ℃
            tmp_last = last_long(tmp, 1)

            wind = self.get_text('xpath', '//*[@id="weather_card"]/div/ul/li[2]/div/span[1]')
            # 风等级 纯数字
            wind_data = hourly_wind(wind)
            # 风 级
            wind_last = last_long(wind, 1)

            gust = self.get_text('xpath', '//*[@id="weather_card"]/div/ul/li[3]/div/span[1]')
            # 风速 纯数字
            gust_data = hourly_wind(gust)
            # 风 级
            gust_last = last_long(gust, 1)

            cloud = self.get_text('xpath', '//*[@id="weather_card"]/div/ul/li[4]/div/span[1]')
            # 云量 纯数字
            cloud_data = hourly_per(cloud)
            # 云量 符号 %
            cloud_last = last_long(cloud, 1)

            if 0 <= cloud_data <= 100:
                num = num + 1
                print(1)
            if 0 <= wind_data <= 13:
                num = num + 1
                print(2)
            if 0 <= gust_data <= 13:
                num = num + 1
                print(3)
            if today_data[4] - 5 <= tmp_data <= today_data[3] + 5:
                num = num + 1
                print(4)
            if tmp_last == '℃':
                num = num + 1
                print(5)
            if wind_last == '级':
                num = num + 1
                print(6)
            if gust_last == '级':
                num = num + 1
                print(7)
            if cloud_last == '%':
                num = num + 1
                print(8)

            if txt1 == '体感温度':
                num = num + 1
                print(9)
            if txt2 == '风':
                num = num + 1
                print(10)
            if txt3 == '风':
                num = num + 1
                print(11)
            if txt4 == '云量':
                num = num + 1
                print(12)

            if icon1 == 'http://s1.zuimeitianqi.com/page/dist/res/img/wea_light_item_icon/ic_today_sendible.svg':
                num = num + 1
                print(13)
            if icon2 == 'http://s1.zuimeitianqi.com/page/dist/res/img/wea_light_item_icon/ic_today_wind.svg':
                num = num + 1
                print(14)
            if icon3 == 'http://s1.zuimeitianqi.com/page/dist/res/img/wea_light_item_icon/ic_today_gust.svg':
                num = num + 1
                print(15)
            if icon4 == 'http://s1.zuimeitianqi.com/page/dist/res/img/wea_light_item_icon/ic_today_cloud.svg':
                num = num + 1
                print(16)



        except BaseException:
            print('每日 天气详情卡片元素获取失败！')
            logger.info('每日 天气详情卡片元素获取失败！')

        else:
            print(f'每日 天气详情卡片元素获取成功,下方描述：{txt1},{txt2},{txt3},{txt4},数据：{tmp},{wind},{gust},{cloud}')
            logger.info(
                f'每日 天气详情卡片元素获取成功，title为：下方描述：{txt1},{txt2},{txt3},{txt4},数据：{tmp},{wind},{gust},{cloud}')
            if num == 16:
                return 1
            else:
                return 2

    # 降水
    def daily_rain(self):
        try:
            num = 0
            # 降水
            title = self.get_text('xpath', '//*[@id="prec_box"]/div[1]/div')
            if title == '降水':
                num = num + 1
            # 总降水量:
            txt1 = self.get_text('xpath', '//*[@id="prec_box"]/ul/li[1]/span[1]')
            if txt1 == '总降水量:':
                num = num + 1
            # 概率:
            txt2 = self.get_text('xpath', '//*[@id="prec_box"]/ul/li[2]/span[1]')
            if txt2 == '概率:':
                num = num + 1
            # 雷暴概率:
            txt3 = self.get_text('xpath', '//*[@id="prec_box"]/ul/li[3]/span[1]')
            if txt3 == '雷暴概率:':
                num = num + 1
            # 降雨
            txt4 = self.get_text('xpath', '//*[@id="prec_box"]/div[2]/div[1]/div[2]/span[2]')
            if txt4 == '降雨':
                num = num + 1
            # 降雪
            txt5 = self.get_text('xpath', '//*[@id="prec_box"]/div[2]/div[2]/div[2]/span[2]')
            if txt5 == '降雪':
                num = num + 1
            # 结冰
            txt6 = self.get_text('xpath', '//*[@id="prec_box"]/div[2]/div[3]/div[2]/span[2]')
            if txt6 == '结冰':
                num = num + 1

            date1 = self.get_text('xpath', '//*[@id="prec_box"]/ul/li[1]/span[2]')
            date1_first = daily_rain(date1)
            date1_last = last_long(date1, 2)
            if 0 <= date1_first <= 300 and date1_last == 'mm':
                num = num + 1

            date2 = self.get_text('xpath', '//*[@id="prec_box"]/ul/li[2]/span[2]')
            date2_first = hourly_per(date2)
            date2_last = last_long(date2, 1)
            if 0 <= date2_first <= 100 and date2_last == '%':
                num = num + 1

            date3 = self.get_text('xpath', '//*[@id="prec_box"]/ul/li[3]/span[2]')
            date3_first = hourly_per(date3)
            date3_last = last_long(date3, 1)
            if 0 <= date3_first <= 100 and date3_last == '%':
                num = num + 1

            date4 = self.get_text('xpath', '//*[@id="prec_box"]/div[2]/div[1]/div[2]/span[1]')
            date4_first = daily_rain(date4)
            date4_last = last_long(date4, 2)
            if 0 <= date4_first <= 300 and date4_last == 'mm':
                num = num + 1

            date5 = self.get_text('xpath', '//*[@id="prec_box"]/div[2]/div[2]/div[2]/span[1]')
            date5_first = daily_rain(date5)
            date5_last = last_long(date5, 2)
            if 0 <= date5_first <= 300 and date5_last == 'mm':
                num = num + 1

            date6 = self.get_text('xpath', '//*[@id="prec_box"]/div[2]/div[3]/div[2]/span[1]')
            date6_first = daily_rain(date6)
            date6_last = last_long(date6, 2)
            if 0 <= date6_first <= 300 and date6_last == 'mm':
                num = num + 1
        except BaseException:
            print('每日 降水 数据获取失败！检查代码！')
            logger.info('每日 降水 数据获取失败！检查代码！')
        else:
            print(f'每日 降水 数据获取成功，数据为：{date1},{date2},{date3},{date4},{date5},{date6}')
            if num == 13:
                return 1
            else:
                return 2

    # 今日运势
    def daily_calendar(self):
        try:
            num = 0
            # 今日运势
            title = self.get_text('xpath', '//*[@id="calendar_box"]/div[1]/div[1]')
            if title == '今日运势':
                print(1)
                num = num + 1
                print(f'今日运势title：{title}')
                logger.info(f'今日运势title：{title}')
            # 日期
            date = int(self.get_text('xpath', '//*[@id="calendar_content"]/div[1]/span[1]'))

            if date == daily_day(self.get_text('xpath', '//*[@id="weather_card"]/div/div[1]/div[2]')):
                print(2)
                num = num + 1
                print(f'今日运势 日期为：{date}')
                logger.info(f'今日运势 日期为：{date}')
            # 宜 图片 src
            good_src = self.get_attr('xpath', '//*[@id="calendar_content"]/div[2]/div[1]/span[1]/img', what='src')
            if good_src == 'http://s1.zuimeitianqi.com/page/dist/res/img/ic_luck_good.svg':
                print(3)
                num = num + 1
                print(f'宜 图片地址：{good_src}')
                logger.info(f'宜 图片地址：{good_src}')
            # 忌 图片 src
            bad_src = self.get_attr('xpath', '//*[@id="calendar_content"]/div[2]/div[2]/span[1]/img', what='src')
            if bad_src == 'http://s1.zuimeitianqi.com/page/dist/res/img/ic_luck_bad.svg':
                print(4)
                num = num + 1
                print(f'忌 图片地址：{bad_src}')
                logger.info(f'忌 图片地址：{bad_src}')
            # 宜 文字内容
            good_txt = self.get_text('xpath', '//*[@id="calendar_content"]/div[2]/div[1]/span[2]')
            good_txt_check = contain_chinese_one(good_txt)

            if good_txt_check == 1:
                num = num + 1
                print(5)
                print(f'宜 文字内容为：{good_txt}')
                logger.info(f'宜 文字内容为：{good_txt}')
            # 忌 文字内容
            bad_txt = self.get_text('xpath', '//*[@id="calendar_content"]/div[2]/div[2]/span[2]')
            bad_txt_check = contain_chinese_one(bad_txt)
            if bad_txt_check == 1:
                num = num + 1
                print(6)
                print(f'宜 文字内容为：{bad_txt}')
                logger.info(f'宜 文字内容为：{bad_txt}')
            # 第一个星座名字 座
            constellation1_txt = last_long(self.get_text('xpath', '//*[@id="star_move"]/ul/li[1]/a/div/div/div['
                                                                  '1]/span[1]'), 1)

            # 第二个星座名字 座
            constellation2_txt = last_long(self.get_text('xpath', '//*[@id="star_move"]/ul/li[2]/a/div/div/div['
                                                                  '1]/span[1]'), 1)

            if constellation1_txt and constellation2_txt == '座':
                num = num + 1
                print(7)
                print(f'星座名显示正常，最后一个字显示为：{constellation1_txt},{constellation2_txt}')
                logger.info(f'星座名显示正常，最后一个字显示为：{constellation1_txt},{constellation2_txt}')

            # .png
            constellation1_pic = last_long(
                self.get_attr('xpath', '//*[@id="star_move"]/ul/li[1]/a/div/img', what='src'), 4)
            constellation2_pic = last_long(
                self.get_attr('xpath', '//*[@id="star_move"]/ul/li[2]/a/div/img', what='src'), 4)
            constellation_last_pic = last_long(
                self.get_attr('xpath', '//*[@id="star_move"]/ul/li[12]/a/div/img', what='src'), 4)
            if constellation1_pic and constellation2_pic and constellation_last_pic == '.png':
                num = num + 1
                print(8)
                print(f'图片显示正常，图片后缀为：{constellation1_pic},{constellation2_pic},{constellation_last_pic}')
                logger.info(f'图片显示正常，图片后缀为：{constellation1_pic},{constellation2_pic},{constellation_last_pic}')

            # 今日运势
            today1 = self.get_text('xpath', '//*[@id="star_move"]/ul/li[1]/a/div/div/div[2]/span')
            today2 = self.get_text('xpath', '//*[@id="star_move"]/ul/li[2]/a/div/div/div[2]/span')
            if today1 and today2 == '今日运势':
                print(9)
                num = num + 1
                print(f'星星：{today1},{today2}')
                logger.info(f'星星：{today1},{today2}')

            # 信息流图片 jpeg@
            information1_pic = baidu_get_jpeg(
                self.get_attr('xpath', '//*[@id="star_ul"]/li[1]/a/div[2]/img', what='src'))
            # 信息流 标题...
            information1_txt = contain_chinese_one(self.get_text('xpath', '//*[@id="star_ul"]/li[1]/a/div[1]/h3'))

            information2_pic = baidu_get_jpeg(
                self.get_attr('xpath', '//*[@id="star_ul"]/li[2]/a/div[2]/img', what='src'))
            information2_txt = contain_chinese_one(self.get_text('xpath', '//*[@id="star_ul"]/li[2]/a/div[1]/h3'))

            if information1_pic and information2_pic == 'jpeg@' or '.png@':
                num = num + 1
                print(10)
                print(f'信息流图片显示正常：{information1_pic},{information2_pic}')
                logger.info(f'信息流图片显示正常：{information1_pic},{information2_pic}')
            if information1_txt and information2_txt == 1:
                print(11)
                num = num + 1
                print(f'信息流标题显示正常，{information1_txt}, {information2_txt}')
                print(num)
        except BaseException:
            print('今日运势模块 获取页面元素失败！检查代码！')
            logger.info('今日运势模块 获取页面元素失败！检查代码！')

        else:
            print('今日运势模块 获取页面元素成功')
            logger.info('今日运势模块 获取页面元素成功')

            if num == 11:
                return 1
            else:
                return 2

    # 今日运势 日历 二级页面
    def calendar_page_two(self):
        try:
            # 日历 模块
            num = 0
            load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 600)
            date = self.get_text('xpath', '//*[@id="calendar_content"]/div[1]/span[1]')
            calendar = self.find_element('xpath', '//*[@id="calendar_content"]/div[1]/span[1]')
            calendar.click()
            time.sleep(2)
            ct1 = self.get_text('xpath', '//*[@id="wrapper"]/div/article/div/div[2]/div[2]/ul/li[2]/a/div[3]/span')
            ct2 = self.get_text('xpath', '//*[@id="wrapper"]/div/article/div/div[2]/div[2]/ul/li[4]/a/div[3]/span')
            if ct1 == '八字合婚':
                num = num + 1
                print(f'显示内容为：{ct1}')
                logger.info(f'显示内容为：{ct1}')
            if ct2 == '月老姻缘':
                num = num + 1
                print(f'显示内容为：{ct2}')
                logger.info(f'显示内容为：{ct2}')

            ct_date = self.get_text('xpath', '//*[@id="wrapper"]/div/article/div/div[2]/div[1]/div[1]/span')
            if int(date) == int(ct_date):
                num = num + 1

                print(f'显示日期为：{ct_date}')
                logger.info(f'显示日期为：{ct_date}')
        except BaseException:
            print('今日运势 阳历 二级页面 打开或元素获取失败！')
            logger.info('今日运势 阳历 二级页面 打开或元素获取失败！')
        else:
            if num == 3:
                return 1
            else:
                return 2

    # 今日运势 星座 二级页面
    def constellation_page_two(self):
        # try:
        num = 0
        button = self.driver.find_element('xpath', '//*[@id="star_card"]')
        action = ActionChains(self.driver).move_to_element(button)
        time.sleep(1)
        action.perform()
        time.sleep(1)
        # load_page('//*[@id="star_card"]', 100)
        button.click()
        time.sleep(1)

        # 今日运势
        today = self.get_text('xpath', '//*[@id="page_content"]/div[3]/div[1]/ul/li[1]')
        if today == '今日运势':
            num = num + 1
            print(f'今日运势显示为：{today}')
            logger.info(f'今日运势显示为：{today}')
            print(1)
        pic = self.get_attr('xpath', '//*[@id="header"]/img[2]', what='src')
        if pic == 'http://s1.zuimeitianqi.com/page/dist/res/img/constellation/bg_top.png':
            num = num + 1
            print(f'顶部 图片 src为:{pic}')
            logger.info(f'顶部 图片 src为:{pic}')
            print(2)
        work_txt = self.find_element('xpath', '//*[@id="index_box"]/ul[1]/li[4]/div[1]/span[2]').get_attribute(
            'textContent')
        if work_txt == '工作指数':
            num = num + 1
            print(f'工作指数显示为：{work_txt}')
            logger.info(f'工作指数显示为：{work_txt}')
            print(3)

        load_page('//*[@id="index_box"]/ul[1]/li[1]/div[1]/span[2]', 1000)
        last_txt = self.get_text('xpath', '//*[@id="operate_wrapper"]/div[1]/div')
        if last_txt == '星座资讯':
            num = num + 1
            print(f'星座资讯显示为：{last_txt}')
            logger.info(f'星座资讯显示为：{last_txt}')
            print(4)
        pic1 = baidu_get_jpeg(self.get_attr('xpath', '//*[@id="operate_list"]/ul/li[4]/a/img', what='src'))
        pic2 = baidu_get_jpeg(self.get_attr('xpath', '//*[@id="operate_list"]/ul/li[7]/a/img', what='src'))
        if pic1 and pic2 == 'jpeg@' or '.png@':
            num = num + 1
            print(f'信息流图片显示地址关键字：{pic1},{pic2}')
            logger.info(f'信息流图片显示地址关键字：{pic1},{pic2}')
            print(5)
        t1 = self.get_text('xpath', '//*[@id="operate_list"]/ul/li[2]/a/div/span')

        if contain_chinese(t1) == 1:
            num = num + 1
            print(f'信息流文字判断:{t1}')
            logger.info(f'信息流文字判断:{t1}')
            print(6)
        print(num)
        # except BaseException:
        #     print('今日运势 星座 二级页面打开页面或获取元素失败!')
        #     logger.info('今日运势 星座 二级页面打开页面或获取元素失败!')
        # else:
        if num == 6:
            return 1
        else:
            return 2

    # 今日运势 更多
    def more_calendar(self):
        num = 0
        button = self.driver.find_element('xpath', '//*[@id="star_more"]')
        action = ActionChains(self.driver).move_to_element(button)
        time.sleep(1)
        action.perform()
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 400)
        time.sleep(1)
        load_page('//*[@id="star_more"]', 100)
        button.click()
        time.sleep(2)

        p1 = baidu_get_jpeg(self.get_attr('xpath', '//*[@id="weather_news_list"]/li[1]/a/img', what='src'))

        if p1 == 'jpeg@' or '.png@':
            num = num + 1
            print(f'图片 链接关键字显示为：{p1}')
            logger.info(f'图片 链接关键字显示为：{p1},')

        t1 = self.get_text('xpath', '//*[@id="weather_news_list"]/li[1]/a/h3')
        t1_check = contain_chinese(t1)

        if t1_check == 1:
            num = num + 1
            print(f'信息流title 显示为：{t1}')
            logger.info(f'信息流title 显示为：{t1}')

        if num == 2:
            return 1
        else:
            return 2

    # 每日 生活指南
    def daily_living_guide(self):
        try:
            i = Share().living_guide()
        except BaseException:
            print('从共用页面里->调用生活指南页面失败！')
            logger.info('从共用页面里->调用生活指南页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 每日 生活指南二级页面
    def daily_living_guide_page_two(self):
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

    # 每日 生活资讯
    def daily_operate_wrapper(self):
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

    # 每日 生活资讯 更多
    def daily_operate_wrapper_more(self):
        try:
            i = Share().operate_wrapper_more(400)
        except BaseException:
            print('从共用页面里->调用每日 生活资讯 更多失败！')
            logger.info('从共用页面里->调用每日 生活资讯 更多失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 每日 天气快讯
    def daily_reptile_news(self):
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

    # 每日 天气快讯 更多
    def daily_reptile_news_more(self):
        try:
            i = Share().reptile_news_more(450)
        except BaseException:
            print('从共用页面里->调用每日 天气快讯 更多失败！')
            logger.info('从共用页面里->调用每日 天气快讯 更多失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 每日 天气纵览
    def daily_news_video(self):
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

    # 每日 天气纵览 更多
    def daily_news_video_more(self):
        try:
            i = Share().news_video_more(700)
        except BaseException:
            print('从共用页面里->调用每日 天气纵览 更多失败！')
            logger.info('从共用页面里->调用每日 天气纵览 更多失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 每日 猜你喜欢
    def daily_weather_news(self):

        i = Share().weather_news()

        if i == 1:
            return 1
        if i == 2:
            return 2

    # 每日 猜你喜欢 更多
    def daily_weather_news_more(self):

        i = Share().weather_news_more(400)

        if i == 1:
            return 1
        if i == 2:
            return 2

    # 每日 版权信息
    def daily_copyright(self):

        i = Share().copyright()

        if i == 1:
            return 1
        if i == 2:
            return 2

    # 页面跳转 小时天气 多天预报 生活指数 新闻资讯
    # def page_jump(self):
    #     # try:
    #     # load_page('//*[@id="weather_news"]/div/div/div[2]/a', 50)
    #     hourly_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/img', what='src')
    #     hourly_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/span', what='textContent')
    #
    #     days_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/img', what='src')
    #     days_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/span', what='textContent')
    #
    #     comfor_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/img', what='src')
    #     comfor_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/span', what='textContent')
    #
    #     news_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/img', what='src')
    #     news_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/span', what='textContent')
    #     # except BaseException:
    #     #     print('页面跳转 小时天气 多天预报 生活指数 新闻资讯 获取内容失败！')
    #     #     logger.info('页面跳转 小时天气 多天预报 生活指数 新闻资讯 获取内容失败！')
    #     # else:
    #     num = 0
    #     if hourly_img == 'http://s1.zuimeitianqi.com/page/dist/res/img/page_btn/btn_page_hourly.svg' \
    #             and days_img == 'http://s1.zuimeitianqi.com/page/dist/res/img/page_btn/btn_page_days.svg' \
    #             and comfor_img == 'http://s1.zuimeitianqi.com/page/dist/res/img/page_btn/btn_page_live.svg' \
    #             and news_img == 'http://s1.zuimeitianqi.com/page/dist/res/img/page_btn/btn_page_news.svg':
    #         num += 1
    #         print(1)
    #     if hourly_txt == '小时天气' and days_txt == '多天预报' and comfor_txt == '生活指数' and news_txt == '新闻资讯':
    #         num += 1
    #         print(2)
    #
    #     self.click('xpath', '//*[@id="page_jump"]/ul/li[1]/img')
    #     time.sleep(3)
    #     page_url = self.driver.current_url
    #     if 'hourly' in page_url:
    #         num += 1
    #         print(3)
    #     print(page_url)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #     load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 100)
    #     self.click('xpath', '//*[@id="page_jump"]/ul/li[2]/img')
    #     time.sleep(3)
    #     page_url1 = self.driver.current_url
    #     if 'days' in page_url1:
    #         num += 1
    #         print(4)
    #     print(page_url1)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #     load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 100)
    #     self.click('xpath', '//*[@id="page_jump"]/ul/li[3]/img')
    #     time.sleep(3)
    #     page_url2 = self.driver.current_url
    #     if 'comfor' in page_url2:
    #         num += 1
    #         print(5)
    #     print(page_url2)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #     load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 100)
    #     self.click('xpath', '//*[@id="page_jump"]/ul/li[4]/img')
    #     time.sleep(3)
    #     page_url3 = self.driver.current_url
    #     if 'news' in page_url3:
    #         num += 1
    #         print(6)
    #     print(page_url3)
    #     if num == 6:
    #         return 1
    #     else:
    #         return 2

    # 日出日落
    def sun(self):
        i = Share().sun()
        if i == 1:
            return 1
        else:
            return 2

        # 日出日落二级页面

    def sun_page_two(self):
        i = Share().sun_page_two()
        if i == 1:
            return 1
        else:
            return 2


if __name__ == '__main__':
    # print(DailyPage().calendar_page_two())
    print(DailyPage().sun_page_two())
