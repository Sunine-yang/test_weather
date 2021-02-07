import datetime
import time

from common.common_page import Share
from log.Log import logger
from util.check_chinese import contain_chinese_one, contain_chinese
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_date import week_deal
from util.get_driver import UtilWebDriver
from util.regular_deal import daily_month, daily_day, last_long, get_tmp


class DaysPage(FindElement):
    def __init__(self):
        super(DaysPage, self).__init__()
        self.driver = UtilWebDriver.get_driver()
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/days.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4'
            f'&source=zm&oriId=P6')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/days.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4'
            f'&source=zm&oriId=P6')
        self.driver.implicitly_wait(10)
        # # 天气文字描述 实况当前温度 天气预警信息 最高温度 最低温度
        # today_data = Share().today_data()
        time.sleep(2)

    # 顶部天气预警信息 横幅
    # def days_warn_top(self):
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

    # 判断主卡片，星期，日期，空气质量，天气状态图片，温度，天气情况，风 显示 15日主卡片
    def forecast_list_date(self):
        try:
            time0 = datetime.datetime.now() + datetime.timedelta(days=-1)
            time1 = datetime.datetime.now() + datetime.timedelta()
            time2 = datetime.datetime.now() + datetime.timedelta(days=1)
            time3 = datetime.datetime.now() + datetime.timedelta(days=2)
            time4 = datetime.datetime.now() + datetime.timedelta(days=3)
            time5 = datetime.datetime.now() + datetime.timedelta(days=4)
            time6 = datetime.datetime.now() + datetime.timedelta(days=5)
            time7 = datetime.datetime.now() + datetime.timedelta(days=6)
            time8 = datetime.datetime.now() + datetime.timedelta(days=7)
            time9 = datetime.datetime.now() + datetime.timedelta(days=8)
            time10 = datetime.datetime.now() + datetime.timedelta(days=9)
            time11 = datetime.datetime.now() + datetime.timedelta(days=10)
            time12 = datetime.datetime.now() + datetime.timedelta(days=11)
            time13 = datetime.datetime.now() + datetime.timedelta(days=12)
            time14 = datetime.datetime.now() + datetime.timedelta(days=13)
            time15 = datetime.datetime.now() + datetime.timedelta(days=14)

            # 星期 格式：星期一
            # week0 = week_deal(time0.isoweekday())
            # week1 = week_deal(time1.isoweekday())
            # week2 = week_deal(time2.isoweekday())
            week3 = week_deal(time3.isoweekday())
            week4 = week_deal(time4.isoweekday())
            week5 = week_deal(time5.isoweekday())
            week6 = week_deal(time6.isoweekday())
            week7 = week_deal(time7.isoweekday())
            week8 = week_deal(time8.isoweekday())
            week9 = week_deal(time9.isoweekday())
            week10 = week_deal(time10.isoweekday())
            week11 = week_deal(time11.isoweekday())
            week12 = week_deal(time12.isoweekday())
            week13 = week_deal(time13.isoweekday())
            week14 = week_deal(time14.isoweekday())
            week15 = week_deal(time15.isoweekday())

            # 16
            week_num = 0
            page_week0 = self.find_element('xpath', '//*[@id="forecast_list"]/li[1]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week1 = self.find_element('xpath', '//*[@id="forecast_list"]/li[2]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week2 = self.find_element('xpath', '//*[@id="forecast_list"]/li[3]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week3 = self.find_element('xpath', '//*[@id="forecast_list"]/li[4]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week4 = self.find_element('xpath', '//*[@id="forecast_list"]/li[5]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week5 = self.find_element('xpath', '//*[@id="forecast_list"]/li[6]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week6 = self.find_element('xpath', '//*[@id="forecast_list"]/li[7]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week7 = self.find_element('xpath', '//*[@id="forecast_list"]/li[8]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week8 = self.find_element('xpath', '//*[@id="forecast_list"]/li[9]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week9 = self.find_element('xpath', '//*[@id="forecast_list"]/li[10]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week10 = self.find_element('xpath', '//*[@id="forecast_list"]/li[11]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week11 = self.find_element('xpath', '//*[@id="forecast_list"]/li[12]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week12 = self.find_element('xpath', '//*[@id="forecast_list"]/li[13]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week13 = self.find_element('xpath', '//*[@id="forecast_list"]/li[14]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week14 = self.find_element('xpath', '//*[@id="forecast_list"]/li[15]/div[1]/span[1]').get_attribute(
                'textContent')
            page_week15 = self.find_element('xpath', '//*[@id="forecast_list"]/li[16]/div[1]/span[1]').get_attribute(
                'textContent')

            if page_week0 == '昨天':
                week_num += 1
            if page_week1 == '今天':
                week_num += 1
            if page_week2 == '明天':
                week_num += 1
            if page_week3 == week3:
                week_num += 1
            if page_week4 == week4:
                week_num += 1
            if page_week5 == week5:
                week_num += 1
            if page_week6 == week6:
                week_num += 1
            if page_week7 == week7:
                week_num += 1
            if page_week8 == week8:
                week_num += 1
            if page_week9 == week9:
                week_num += 1
            if page_week10 == week10:
                week_num += 1
            if page_week11 == week11:
                week_num += 1
            if page_week12 == week12:
                week_num += 1
            if page_week13 == week13:
                week_num += 1
            if page_week14 == week14:
                week_num += 1
            if page_week15 == week15:
                week_num += 1
            print('week_num16:' + str(week_num))
            logger.info('week_num16:' + str(week_num))

            # 16
            # 日月 格式：11/12
            month_num = 0
            month0 = str(daily_month(time0.strftime('%m月%d日'))) + '/' + str(
                daily_day(time0.strftime('%m月%d日')))
            month1 = str(daily_month(time1.strftime('%m月%d日'))) + '/' + str(
                daily_day(time1.strftime('%m月%d日')))
            month2 = str(daily_month(time2.strftime('%m月%d日'))) + '/' + str(
                daily_day(time2.strftime('%m月%d日')))
            month3 = str(daily_month(time3.strftime('%m月%d日'))) + '/' + str(
                daily_day(time3.strftime('%m月%d日')))
            month4 = str(daily_month(time4.strftime('%m月%d日'))) + '/' + str(
                daily_day(time4.strftime('%m月%d日')))
            month5 = str(daily_month(time5.strftime('%m月%d日'))) + '/' + str(
                daily_day(time5.strftime('%m月%d日')))
            month6 = str(daily_month(time6.strftime('%m月%d日'))) + '/' + str(
                daily_day(time6.strftime('%m月%d日')))
            month7 = str(daily_month(time7.strftime('%m月%d日'))) + '/' + str(
                daily_day(time7.strftime('%m月%d日')))
            month8 = str(daily_month(time8.strftime('%m月%d日'))) + '/' + str(
                daily_day(time8.strftime('%m月%d日')))
            month9 = str(daily_month(time9.strftime('%m月%d日'))) + '/' + str(
                daily_day(time9.strftime('%m月%d日')))
            month10 = str(daily_month(time10.strftime('%m月%d日'))) + '/' + str(
                daily_day(time10.strftime('%m月%d日')))
            month11 = str(daily_month(time11.strftime('%m月%d日'))) + '/' + str(
                daily_day(time11.strftime('%m月%d日')))
            month12 = str(daily_month(time12.strftime('%m月%d日'))) + '/' + str(
                daily_day(time12.strftime('%m月%d日')))
            month13 = str(daily_month(time13.strftime('%m月%d日'))) + '/' + str(
                daily_day(time13.strftime('%m月%d日')))
            month14 = str(daily_month(time14.strftime('%m月%d日'))) + '/' + str(
                daily_day(time14.strftime('%m月%d日')))
            month15 = str(daily_month(time15.strftime('%m月%d日'))) + '/' + str(
                daily_day(time15.strftime('%m月%d日')))

            page_date0 = self.find_element('xpath', '//*[@id="forecast_list"]/li[1]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date1 = self.find_element('xpath', '//*[@id="forecast_list"]/li[2]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date2 = self.find_element('xpath', '//*[@id="forecast_list"]/li[3]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date3 = self.find_element('xpath', '//*[@id="forecast_list"]/li[4]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date4 = self.find_element('xpath', '//*[@id="forecast_list"]/li[5]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date5 = self.find_element('xpath', '//*[@id="forecast_list"]/li[6]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date6 = self.find_element('xpath', '//*[@id="forecast_list"]/li[7]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date7 = self.find_element('xpath', '//*[@id="forecast_list"]/li[8]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date8 = self.find_element('xpath', '//*[@id="forecast_list"]/li[9]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date9 = self.find_element('xpath', '//*[@id="forecast_list"]/li[10]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date10 = self.find_element('xpath', '//*[@id="forecast_list"]/li[11]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date11 = self.find_element('xpath', '//*[@id="forecast_list"]/li[12]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date12 = self.find_element('xpath', '//*[@id="forecast_list"]/li[13]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date13 = self.find_element('xpath', '//*[@id="forecast_list"]/li[14]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date14 = self.find_element('xpath', '//*[@id="forecast_list"]/li[15]/div[1]/span[2]').get_attribute(
                'textContent')
            page_date15 = self.find_element('xpath', '//*[@id="forecast_list"]/li[16]/div[1]/span[2]').get_attribute(
                'textContent')

            if page_date0 == month0:
                month_num += 1
            if page_date1 == month1:
                month_num += 1
            if page_date2 == month2:
                month_num += 1
            if page_date3 == month3:
                month_num += 1
            if page_date4 == month4:
                month_num += 1
            if page_date5 == month5:
                month_num += 1
            if page_date6 == month6:
                month_num += 1
            if page_date7 == month7:
                month_num += 1
            if page_date8 == month8:
                month_num += 1
            if page_date9 == month9:
                month_num += 1
            if page_date10 == month10:
                month_num += 1
            if page_date11 == month11:
                month_num += 1
            if page_date12 == month12:
                month_num += 1
            if page_date13 == month13:
                month_num += 1
            if page_date14 == month14:
                month_num += 1
            if page_date15 == month15:
                month_num += 1

            print('month_num16:' + str(month_num))
            logger.info('month_num16:' + str(month_num))

            # 16
            # 两个天气图标
            icon_num = 0
            iconmax0 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[1]/div[1]/span[3]/img', what='src')
            iconmin0 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[1]/div[2]/span[1]/img', what='src')
            iconmax1 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[2]/div[1]/span[3]/img', what='src')
            iconmin1 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[2]/div[2]/span[1]/img', what='src')
            iconmax2 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[3]/div[1]/span[3]/img', what='src')
            iconmin2 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[3]/div[2]/span[1]/img', what='src')
            iconmax3 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[4]/div[1]/span[3]/img', what='src')
            iconmin3 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[4]/div[2]/span[1]/img', what='src')
            iconmax4 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[5]/div[1]/span[3]/img', what='src')
            iconmin4 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[5]/div[2]/span[1]/img', what='src')
            iconmax5 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[6]/div[1]/span[3]/img', what='src')
            iconmin5 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[6]/div[2]/span[1]/img', what='src')
            iconmax6 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[7]/div[1]/span[3]/img', what='src')
            iconmin6 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[7]/div[2]/span[1]/img', what='src')
            iconmax7 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[8]/div[1]/span[3]/img', what='src')
            iconmin7 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[8]/div[2]/span[1]/img', what='src')
            iconmax8 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[9]/div[1]/span[3]/img', what='src')
            iconmin8 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[9]/div[2]/span[1]/img', what='src')
            iconmax9 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[10]/div[1]/span[3]/img', what='src')
            iconmin9 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[10]/div[2]/span[1]/img', what='src')
            iconmax10 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[11]/div[1]/span[3]/img', what='src')
            iconmin10 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[11]/div[2]/span[1]/img', what='src')
            iconmax11 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[12]/div[1]/span[3]/img', what='src')
            iconmin11 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[12]/div[2]/span[1]/img', what='src')
            iconmax12 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[13]/div[1]/span[3]/img', what='src')
            iconmin12 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[13]/div[2]/span[1]/img', what='src')
            iconmax13 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[14]/div[1]/span[3]/img', what='src')
            iconmin13 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[14]/div[2]/span[1]/img', what='src')
            iconmax14 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[15]/div[1]/span[3]/img', what='src')
            iconmin14 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[15]/div[2]/span[1]/img', what='src')
            iconmax15 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[16]/div[1]/span[3]/img', what='src')
            iconmin15 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[16]/div[2]/span[1]/img', what='src')

            if '.svg' in iconmax0 and iconmin0:
                icon_num += 1
            if '.svg' in iconmax1 and iconmin1:
                icon_num += 1
            if '.svg' in iconmax2 and iconmin2:
                icon_num += 1
            if '.svg' in iconmax3 and iconmin3:
                icon_num += 1
            if '.svg' in iconmax4 and iconmin4:
                icon_num += 1
            if '.svg' in iconmax5 and iconmin5:
                icon_num += 1
            if '.svg' in iconmax6 and iconmin6:
                icon_num += 1
            if '.svg' in iconmax7 and iconmin7:
                icon_num += 1
            if '.svg' in iconmax8 and iconmin8:
                icon_num += 1
            if '.svg' in iconmax9 and iconmin9:
                icon_num += 1
            if '.svg' in iconmax10 and iconmin10:
                icon_num += 1
            if '.svg' in iconmax11 and iconmin11:
                icon_num += 1
            if '.svg' in iconmax12 and iconmin12:
                icon_num += 1
            if '.svg' in iconmax13 and iconmin13:
                icon_num += 1
            if '.svg' in iconmax14 and iconmin14:
                icon_num += 1
            if '.svg' in iconmax15 and iconmin15:
                icon_num += 1

            print('icon_num16:' + str(icon_num))
            logger.info('icon_num16:' + str(icon_num))

            # 16
            # 两个天气文字描述
            wea_num = 0
            tu0 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[1]/div[1]/span[4]', what='textContent')
            td0 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[1]/div[2]/span[2]', what='textContent')
            tu1 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[2]/div[1]/span[4]', what='textContent')
            td1 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[2]/div[2]/span[2]', what='textContent')
            tu2 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[3]/div[1]/span[4]', what='textContent')
            td2 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[3]/div[2]/span[2]', what='textContent')
            tu3 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[4]/div[1]/span[4]', what='textContent')
            td3 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[4]/div[2]/span[2]', what='textContent')
            tu4 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[5]/div[1]/span[4]', what='textContent')
            td4 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[5]/div[2]/span[2]', what='textContent')
            tu5 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[6]/div[1]/span[4]', what='textContent')
            td5 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[6]/div[2]/span[2]', what='textContent')
            tu6 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[7]/div[1]/span[4]', what='textContent')
            td6 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[7]/div[2]/span[2]', what='textContent')
            tu7 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[8]/div[1]/span[4]', what='textContent')
            td7 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[8]/div[2]/span[2]', what='textContent')
            tu8 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[9]/div[1]/span[4]', what='textContent')
            td8 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[9]/div[2]/span[2]', what='textContent')
            tu9 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[10]/div[1]/span[4]', what='textContent')
            td9 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[10]/div[2]/span[2]', what='textContent')
            tu10 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[11]/div[1]/span[4]', what='textContent')
            td10 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[11]/div[2]/span[2]', what='textContent')
            tu11 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[12]/div[1]/span[4]', what='textContent')
            td11 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[12]/div[2]/span[2]', what='textContent')
            tu12 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[13]/div[1]/span[4]', what='textContent')
            td12 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[13]/div[2]/span[2]', what='textContent')
            tu13 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[14]/div[1]/span[4]', what='textContent')
            td13 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[14]/div[2]/span[2]', what='textContent')
            tu14 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[15]/div[1]/span[4]', what='textContent')
            td14 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[15]/div[2]/span[2]', what='textContent')
            tu15 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[16]/div[1]/span[4]', what='textContent')
            td15 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[16]/div[2]/span[2]', what='textContent')

            if contain_chinese_one(tu0) and contain_chinese_one(td0) == 1:
                wea_num += 1
            if contain_chinese_one(tu1) and contain_chinese_one(td1) == 1:
                wea_num += 1
            if contain_chinese_one(tu2) and contain_chinese_one(td2) == 1:
                wea_num += 1
            if contain_chinese_one(tu3) and contain_chinese_one(td3) == 1:
                wea_num += 1
            if contain_chinese_one(tu4) and contain_chinese_one(td4) == 1:
                wea_num += 1
            if contain_chinese_one(tu5) and contain_chinese_one(td5) == 1:
                wea_num += 1
            if contain_chinese_one(tu6) and contain_chinese_one(td6) == 1:
                wea_num += 1
            if contain_chinese_one(tu7) and contain_chinese_one(td7) == 1:
                wea_num += 1
            if contain_chinese_one(tu8) and contain_chinese_one(td8) == 1:
                wea_num += 1
            if contain_chinese_one(tu9) and contain_chinese_one(td9) == 1:
                wea_num += 1
            if contain_chinese_one(tu10) and contain_chinese_one(td10) == 1:
                wea_num += 1
            if contain_chinese_one(tu11) and contain_chinese_one(td11) == 1:
                wea_num += 1
            if contain_chinese_one(tu12) and contain_chinese_one(td12) == 1:
                wea_num += 1
            if contain_chinese_one(tu13) and contain_chinese_one(td13) == 1:
                wea_num += 1
            if contain_chinese_one(tu14) and contain_chinese_one(td14) == 1:
                wea_num += 1
            if contain_chinese_one(tu15) and contain_chinese_one(td15) == 1:
                wea_num += 1

            print('wea_num16:' + str(wea_num))
            logger.info('wea_num16:' + str(wea_num))

            # 16
            # 风和风等级
            wind_num = 0
            wind0 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[1]/div[2]/span[3]', what='textContent')
            wind_level0 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[1]/div[2]/span[4]', what='textContent')
            wind1 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[2]/div[2]/span[3]', what='textContent')
            wind_level1 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[2]/div[2]/span[4]', what='textContent')
            wind2 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[3]/div[2]/span[3]', what='textContent')
            wind_level2 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[3]/div[2]/span[4]', what='textContent')
            wind3 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[4]/div[2]/span[3]', what='textContent')
            wind_level3 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[4]/div[2]/span[4]', what='textContent')
            wind4 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[5]/div[2]/span[3]', what='textContent')
            wind_level4 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[5]/div[2]/span[4]', what='textContent')
            wind5 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[6]/div[2]/span[3]', what='textContent')
            wind_level5 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[6]/div[2]/span[4]', what='textContent')
            wind6 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[7]/div[2]/span[3]', what='textContent')
            wind_level6 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[7]/div[2]/span[4]', what='textContent')
            wind7 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[8]/div[2]/span[3]', what='textContent')
            wind_level7 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[8]/div[2]/span[4]', what='textContent')
            wind8 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[9]/div[2]/span[3]', what='textContent')
            wind_level8 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[9]/div[2]/span[4]', what='textContent')
            wind9 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[10]/div[2]/span[3]', what='textContent')
            wind_level9 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[10]/div[2]/span[4]', what='textContent')
            wind10 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[11]/div[2]/span[3]', what='textContent')
            wind_level10 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[11]/div[2]/span[4]', what='textContent')
            wind11 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[12]/div[2]/span[3]', what='textContent')
            wind_level11 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[12]/div[2]/span[4]', what='textContent')
            wind12 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[13]/div[2]/span[3]', what='textContent')
            wind_level12 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[13]/div[2]/span[4]', what='textContent')
            wind13 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[14]/div[2]/span[3]', what='textContent')
            wind_level13 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[14]/div[2]/span[4]', what='textContent')
            wind14 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[15]/div[2]/span[3]', what='textContent')
            wind_level14 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[15]/div[2]/span[4]', what='textContent')
            wind15 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[16]/div[2]/span[3]', what='textContent')
            wind_level15 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[16]/div[2]/span[4]', what='textContent')

            if last_long(wind0, 1) == '风' and last_long(wind_level0, 1) == '级':
                wind_num += 1
            if last_long(wind1, 1) == '风' and last_long(wind_level1, 1) == '级':
                wind_num += 1
            if last_long(wind2, 1) == '风' and last_long(wind_level2, 1) == '级':
                wind_num += 1
            if last_long(wind3, 1) == '风' and last_long(wind_level3, 1) == '级':
                wind_num += 1
            if last_long(wind4, 1) == '风' and last_long(wind_level4, 1) == '级':
                wind_num += 1
            if last_long(wind5, 1) == '风' and last_long(wind_level5, 1) == '级':
                wind_num += 1
            if last_long(wind6, 1) == '风' and last_long(wind_level6, 1) == '级':
                wind_num += 1
            if last_long(wind7, 1) == '风' and last_long(wind_level7, 1) == '级':
                wind_num += 1
            if last_long(wind8, 1) == '风' and last_long(wind_level8, 1) == '级':
                wind_num += 1
            if last_long(wind9, 1) == '风' and last_long(wind_level9, 1) == '级':
                wind_num += 1
            if last_long(wind10, 1) == '风' and last_long(wind_level10, 1) == '级':
                wind_num += 1
            if last_long(wind11, 1) == '风' and last_long(wind_level11, 1) == '级':
                wind_num += 1
            if last_long(wind12, 1) == '风' and last_long(wind_level12, 1) == '级':
                wind_num += 1
            if last_long(wind13, 1) == '风' and last_long(wind_level13, 1) == '级':
                wind_num += 1
            if last_long(wind14, 1) == '风' and last_long(wind_level14, 1) == '级':
                wind_num += 1
            if last_long(wind15, 1) == '风' and last_long(wind_level15, 1) == '级':
                wind_num += 1

            print('wind_num16:' + str(wind_num))
            logger.info('wind_num16:' + str(wind_num))

            tmp_num = 0
            tmpmax0 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(3)').get_attribute(
                    'textContent'))
            tmpmax1 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(5)').get_attribute(
                    'textContent'))
            tmpmax2 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(7)').get_attribute(
                    'textContent'))
            tmpmax3 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(9)').get_attribute(
                    'textContent'))
            tmpmax4 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(11)').get_attribute(
                    'textContent'))
            tmpmax5 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(13)').get_attribute(
                    'textContent'))
            tmpmax6 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(15)').get_attribute(
                    'textContent'))
            tmpmax7 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(17)').get_attribute(
                    'textContent'))
            tmpmax8 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(19)').get_attribute(
                    'textContent'))
            tmpmax9 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(21)').get_attribute(
                    'textContent'))
            tmpmax10 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(23)').get_attribute(
                    'textContent'))
            tmpmax11 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(25)').get_attribute(
                    'textContent'))
            tmpmax12 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(27)').get_attribute(
                    'textContent'))
            tmpmax13 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(29)').get_attribute(
                    'textContent'))
            tmpmax14 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(31)').get_attribute(
                    'textContent'))
            tmpmax15 = get_tmp(
                self.driver.find_element_by_css_selector('#high_svg > svg > g > text:nth-child(33)').get_attribute(
                    'textContent'))

            tmpmin0 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(3)').get_attribute(
                    'textContent'))
            tmpmin1 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(5)').get_attribute(
                    'textContent'))
            tmpmin2 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(7)').get_attribute(
                    'textContent'))
            tmpmin3 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(9)').get_attribute(
                    'textContent'))
            tmpmin4 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(11)').get_attribute(
                    'textContent'))
            tmpmin5 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(13)').get_attribute(
                    'textContent'))
            tmpmin6 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(15)').get_attribute(
                    'textContent'))
            tmpmin7 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(17)').get_attribute(
                    'textContent'))
            tmpmin8 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(19)').get_attribute(
                    'textContent'))
            tmpmin9 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(21)').get_attribute(
                    'textContent'))
            tmpmin10 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(23)').get_attribute(
                    'textContent'))
            tmpmin11 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(25)').get_attribute(
                    'textContent'))
            tmpmin12 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(27)').get_attribute(
                    'textContent'))
            tmpmin13 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(29)').get_attribute(
                    'textContent'))
            tmpmin14 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(31)').get_attribute(
                    'textContent'))
            tmpmin15 = get_tmp(
                self.driver.find_element_by_css_selector('#low_svg > svg > g > text:nth-child(33)').get_attribute(
                    'textContent'))

            if tmpmax0 >= tmpmin0:
                tmp_num += 1
            if tmpmax1 >= tmpmin1:
                tmp_num += 1
            if tmpmax2 >= tmpmin2:
                tmp_num += 1
            if tmpmax3 >= tmpmin3:
                tmp_num += 1
            if tmpmax4 >= tmpmin4:
                tmp_num += 1
            if tmpmax5 >= tmpmin5:
                tmp_num += 1
            if tmpmax6 >= tmpmin6:
                tmp_num += 1
            if tmpmax7 >= tmpmin7:
                tmp_num += 1
            if tmpmax8 >= tmpmin8:
                tmp_num += 1
            if tmpmax9 >= tmpmin9:
                tmp_num += 1
            if tmpmax10 >= tmpmin10:
                tmp_num += 1
            if tmpmax11 >= tmpmin11:
                tmp_num += 1
            if tmpmax12 >= tmpmin12:
                tmp_num += 1
            if tmpmax13 >= tmpmin13:
                tmp_num += 1
            if tmpmax14 >= tmpmin14:
                tmp_num += 1
            if tmpmax15 >= tmpmin15:
                tmp_num += 1

            print('tmp_num16:' + str(tmp_num))
            logger.info('tmp_num16:' + str(tmp_num))

        except BaseException:
            print('15日 主卡片内容获取失败！')
            logger.info('15日 主卡片内容获取失败！')
        else:
            if wind_num + wea_num + icon_num + month_num + week_num + tmp_num == 96:
                return 1
            else:
                return 2

    # 判断主卡片下 文字描述最近降雨情况 显示
    def future_remind(self):
        try:
            num = 0
            txt = self.get_text('xpath', '//*[@id="page_container"]/div[6]/div/div[1]')
            txtlast = last_long(txt, 2)
            if txtlast == '降水':
                num += 1
                print(1)
            print(txt)
            logger.info(f'显示为：{txt}')

            date1 = int(self.find_element('xpath',
                                          '//*[@id="page_container"]/div[6]/div/div[2]/ul/li[1]/span[1]').get_attribute(
                'textContent'))
            date2 = int(self.find_element('xpath',
                                          '//*[@id="page_container"]/div[6]/div/div[2]/ul/li[2]/span[1]').get_attribute(
                'textContent'))
            date3 = int(self.find_element('xpath',
                                          '//*[@id="page_container"]/div[6]/div/div[2]/ul/li[3]/span[1]').get_attribute(
                'textContent'))
            if 1 <= date1 and date2 and date3 <= 31:
                num += 1
                print(2)
            print(date1, date2, date3)
            logger.info(f'{date1},{date2},{date3}')

            month1 = self.find_element('xpath',
                                       '//*[@id="page_container"]/div[6]/div/div[2]/ul/li[1]/span[2]').get_attribute(
                'textContent')
            month2 = self.find_element('xpath',
                                       '//*[@id="page_container"]/div[6]/div/div[2]/ul/li[2]/span[2]').get_attribute(
                'textContent')
            month3 = self.find_element('xpath',
                                       '//*[@id="page_container"]/div[6]/div/div[2]/ul/li[3]/span[2]').get_attribute(
                'textContent')

            if last_long(month1, 1) and last_long(month2, 1) and last_long(month3, 1) == '月':
                num += 1
                print(3)
            print(month1, month2, month3)
            logger.info(f'{month1},{month2},{month3}')

            if 1 <= int(daily_month(month1)) and int(daily_month(month2)) and int(daily_month(month3)) <= 12:
                num += 1
                print(4)
        except BaseException:
            print('15日主卡片下文字降雨预报内容获取失败！')
            logger.info('15日主卡片下文字降雨预报内容获取失败！')
        else:
            if num == 4:
                return 1
            else:
                return 2

    # 判断主卡片下 文字描述最近降雨情况 点击后跳转情况
    def future_remind_click(self):
        try:
            num = 0
            self.find_element('xpath', '//*[@id="page_container"]/div[6]/div').click()
            time.sleep(1)
            # 二级页面
            title = self.get_text('xpath', '//*[@id="page_container"]/div[1]/div/div[1]')
            now_year = datetime.datetime.now().strftime('%Y年%m月')

            page_month = self.get_attr('xpath', '//*[@id="page_container"]/div[1]/div/div[1]', what='textContent')
            now_month = datetime.datetime.now().strftime('%m月%d日')

            page_week = self.get_attr('xpath', '//*[@id="page_container"]/div[3]/div/div[1]/span[2]',
                                      what='textContent')
            now_week = week_deal(datetime.datetime.now().isoweekday())

            if title == now_year and page_month == now_month and page_week == now_week:
                num += 1
                print(1)

            t1 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="calendar_content"]/div[1]/span[1]', what='textContent'))
            t2 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="calendar_content"]/div[1]/span[2]', what='textContent'))
            t3 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="calendar_content"]/div[2]/div[1]/span[2]', what='textContent'))
            t4 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="calendar_content"]/div[2]/div[2]/span[2]', what='textContent'))
            p1 = self.get_attr('xpath', '//*[@id="calendar_content"]/div[2]/div[1]/span[1]/img', what='src')
            p2 = self.get_attr('xpath', '//*[@id="calendar_content"]/div[2]/div[2]/span[1]/img', what='src')
            if t1 and t2 and t3 and t4 == 1:
                num += 1
                print(2)
            if p1 == 'http://h5.zuimeitianqi.com/page/zh/res/img/ic_luck_good.svg' and p2 == 'http://h5.zuimeitianqi.com/page/zh/res/img/ic_luck_bad.svg':
                num += 1
                print(3)

            title1 = self.get_attr('xpath', '//*[@id="page_container"]/div[5]/div[1]/span[1]', what='textContent')
            content1 = self.get_attr('xpath', '//*[@id="page_container"]/div[5]/div[1]/span[2]', what='textContent')
            content2 = self.get_attr('xpath', '//*[@id="time"]/span', what='textContent')

            if title1 == '变化趋势' and contain_chinese(content1) == 1 and content2 == '降水':
                num += 1
                print(4)

            self.click('xpath', '//*[@id="calendar_content"]')
            time.sleep(1)
            url = self.driver.current_url()
            if 'lhl.zxcs.linghit.com' in url:
                num += 1
                self.driver.back()
                time.sleep(1)
                print(5)
            if Share().operate_wrapper == 1:
                num += 1
                print(6)
            time.sleep(1)
            if Share().operate_wrapper_more == 1:
                num += 1
                print(7)
            self.driver.back()
            time.sleep(1)
            if Share().news_video() == 1:
                num += 1
                print(8)
            time.sleep(1)
            if Share().news_video_more == 1:
                num += 1
                print(9)
            self.driver.back()
            time.sleep(1)
            if Share().weather_news() == 1:
                num += 1
                print(10)
            time.sleep(1)
            if Share().weather_news_more(200) == 1:
                num += 1
                print(11)
            self.driver.back()
            time.sleep(1)
            if Share().copyright() == 1:
                num += 1
                print(12)
        except BaseException:
            print('15日 降水 二级页面内容 获取失败！')
            logger.info('15日 降水 二级页面内容 获取失败！')
        else:
            if num == 12:
                return 1
            else:
                return 2

    # 15日 天气纵览
    def days_news_video(self):
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

    # 15日 天气纵览 更多
    def days_news_video_more(self):
        try:
            i = Share().news_video_more(500)
        except BaseException:
            print('从共用页面里->调用天气纵览更多页面失败！')
            logger.info('从共用页面里->调用天气纵览更多页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 15日 生活资讯
    def days_operate_wrapper(self):
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

    # 15日 生活资讯 更多
    def days_operate_wrapper_more(self):
        try:
            i = Share().operate_wrapper_more(500)
        except BaseException:
            print('从共用页面里->调用生活资讯更多页面失败！')
            logger.info('从共用页面里->调用生活资讯更多页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 15日 图集专题
    def days_pic(self):
        try:
            i = Share().pic()
        except BaseException:
            print('从共用页面里->15日 图集专题 页面失败！')
            logger.info('从共用页面里->15日 图集专题 页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 15日 图集专题 更多
    def days_pic_more(self):
        try:
            i = Share().pic_more()
        except BaseException:
            print('从共用页面里->调用15日 图集专题 更多页面失败！')
            logger.info('从共用页面里->调用15日 图集专题 更多页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 15日 生活指南
    def days_living_guide(self):
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

    # 15日 生活指南 二级
    def days_living_guide_page_two(self):
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

    # 15日 节日节气
    def days_fes_news(self):
        try:
            i = Share().fes_news()
        except BaseException:
            print('从共用页面里->调用节日节气页面失败！')
            logger.info('从共用页面里->调用节日节气页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 15日 节日节气 更多 页面
    def days_fes_news_more(self):
        try:
            i = Share().fes_news_more()
        except BaseException:
            print('从共用页面里->调用15日 节日节气 更多 页面失败！')
            logger.info('从共用页面里->调用15日 节日节气 更多 页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 15日 猜你喜欢
    def days_weather_news(self):
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

    # 15日 猜你喜欢 更多
    def days_weather_news_more(self):
        try:
            i = Share().weather_news_more(500)
        except BaseException:
            print('从共用页面里->调用猜你喜欢更多页面失败！')
            logger.info('从共用页面里->调用猜你喜欢更多页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # 15日 底部版权信息
    def days_copyright(self):
        try:
            i = Share().copyright()
        except BaseException:
            print('从共用页面里->调用版权信息页面失败！')
            logger.info('从共用页面里->调用版权信息页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # # 页面跳转 实况天气 小时天气 生活指数 新闻资讯
    # def page_jump(self):
    #     try:
    #         today_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/img', what='src')
    #         today_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/span', what='textContent')
    #
    #         hour_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/img', what='src')
    #         hour_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/span', what='textContent')
    #
    #         comfor_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/img', what='src')
    #         comfor_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/span', what='textContent')
    #
    #         news_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/img', what='src')
    #         news_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/span', what='textContent')
    #     except BaseException:
    #         print('页面跳转 实况天气 小时天气 生活指数 新闻资讯 获取内容失败！')
    #         logger.info('页面跳转 实况天气 小时天气 生活指数 新闻资讯 获取内容失败！')
    #     else:
    #         num = 0
    #         if today_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_now.svg' \
    #                 and hour_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_hourly.svg' \
    #                 and comfor_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_live.svg' \
    #                 and news_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_news.svg':
    #             num += 1
    #             print(1)
    #         if today_txt == '实况天气' and hour_txt == '小时天气' and comfor_txt == '生活指数' and news_txt == '新闻资讯':
    #             num += 1
    #             print(2)
    #
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[1]/img')
    #         time.sleep(3)
    #         page_url = self.driver.current_url
    #         if 'today' in page_url:
    #             num += 1
    #             print(3)
    #         self.driver.back()
    #         time.sleep(1)
    #
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[2]/img')
    #         time.sleep(3)
    #         page_url = self.driver.current_url
    #         if 'hourly' in page_url:
    #             num += 1
    #             print(4)
    #         self.driver.back()
    #         time.sleep(1)
    #
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[3]/img')
    #         time.sleep(3)
    #         page_url = self.driver.current_url
    #         if 'comfor' in page_url:
    #             num += 1
    #             print(5)
    #         self.driver.back()
    #         time.sleep(1)
    #
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[4]/img')
    #         time.sleep(3)
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
    a = DaysPage()
    # print(a.future_remind_click())
    print(a.days_pic())

