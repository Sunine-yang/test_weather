import datetime
import time

from selenium.webdriver import ActionChains
from common.common_page import Share
from util.check_chinese import contain_chinese, contain_chinese_one
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_date import week_deal
from util.get_driver import UtilWebDriver
from log.Log import logger
from util.load_page import load_page
from util.regular_deal import daily_day, daily_month


class AqiPage(FindElement):
    def __init__(self):
        # 继承find element类
        super(AqiPage, self).__init__()
        # 创建配置文件读取对象
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        # 调用单例模式的driver
        self.driver = UtilWebDriver.get_driver()
        # 打开life界面
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/aqi.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
            '=A1&orild=P4&source=zm&oriId=P2')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/aqi.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
            '=A1&orild=P4&source=zm&oriId=P2')
        self.driver.implicitly_wait(10)
        time.sleep(2)

    # 空气质量 主卡片
    def aqi_card(self):
        try:
            num = 0
            # 空气质量AQI
            title = self.get_attr('xpath', '//*[@id="aqi_title_box"]/span', what='textContent')
            print(title)
            # 文字
            aqi_content = self.get_attr('xpath', '//*[@id="aqi_msg"]/span[1]', what='textContent')
            print(aqi_content)
            # 数字
            aqi_data = int(self.get_attr('xpath', '//*[@id="aqi_msg"]/span[2]', what='textContent'))
            print(aqi_data)
            # 文字描述
            aqi_txt = self.get_text('xpath', '//*[@id="aqi_desc"]')
            print(aqi_txt)

            if 0 <= aqi_data <= 50 and '优' in aqi_content:
                num += 1
            elif 51 <= aqi_data <= 100 and '良' in aqi_content:
                num += 1
            elif 101 <= aqi_data <= 150 and '轻度' in aqi_content:
                num += 1
            elif 151 <= aqi_data <= 200 and '中度' in aqi_content:
                num += 1
            elif 201 <= aqi_data <= 300 and '重度' in aqi_content:
                num += 1
            elif 300 <= aqi_data <= 500 and '严重' in aqi_content:
                num += 1

            if contain_chinese(aqi_txt) == 1:
                num += 1
            if title == '空气质量AQI':
                num += 1

            print(f'标题为：{title},空气质量文字为：{aqi_content},指数为：{aqi_data},文字描述为：{aqi_txt}')
            logger.info(f'空气质量文字为：{aqi_content},指数为：{aqi_data},文字描述为：{aqi_txt}')
        except BaseException:
            print('空气质量主卡片数据获取失败！检查代码')
            logger.info('空气质量主卡片数据获取失败！检查代码')
        else:
            if num == 3:
                return 1
            else:
                return 2

    # 主卡片下各项数据
    def aqi_detail(self):
        num = 0
        pm1_data = int(self.get_attr('xpath', '//*[@id="aqi_list"]/li[1]/div[1]/span[1]', what='textContent'))
        pm1_name = self.get_text('xpath', '//*[@id="aqi_list"]/li[1]/div[2]')

        pm2_data = int(self.get_attr('xpath', '//*[@id="aqi_list"]/li[2]/div[1]/span[1]', what='textContent'))
        pm2_name = self.get_text('xpath', '//*[@id="aqi_list"]/li[2]/div[2]')

        co_data = float(self.get_attr('xpath', '//*[@id="aqi_list"]/li[3]/div[1]/span[1]', what='textContent'))
        co_name = self.get_text('xpath', '//*[@id="aqi_list"]/li[3]/div[2]')

        no_data = int(self.get_attr('xpath', '//*[@id="aqi_list"]/li[4]/div[1]/span[1]', what='textContent'))
        no_name = self.get_text('xpath', '//*[@id="aqi_list"]/li[4]/div[2]')

        so_data = int(self.get_attr('xpath', '//*[@id="aqi_list"]/li[5]/div[1]/span[1]', what='textContent'))
        so_name = self.get_text('xpath', '//*[@id="aqi_list"]/li[5]/div[2]')

        o_data = int(self.get_attr('xpath', '//*[@id="aqi_list"]/li[6]/div[1]/span[1]', what='textContent'))
        o_name = self.get_text('xpath', '//*[@id="aqi_list"]/li[6]/div[2]')
        print(
            f'{pm1_name}:{pm1_data},{pm2_name}:{pm2_data},{co_name}:{co_data},{no_name}:{no_data},{so_name}:{so_data}，{o_name}:{o_data}')
        logger.info(
            f'{pm1_name}:{pm1_data},{pm2_name}:{pm2_data},{co_name}:{co_data},{no_name}:{no_data},{so_name}:{so_data}，{o_name}:{o_data}')
        if pm1_data and pm2_data and co_data and no_data and so_data and o_data <= 500:
            num += 1
            print(1)
        if pm1_name == 'PM10' and pm2_name == 'PM2.5' and co_name == 'CO' and no_name == 'NO₂' and so_name == 'SO₂' and o_name == 'O₃':
            num += 1
            print(2)
        pm1c = self.get_text('xpath', '//*[@id="aqi_list"]/li[1]/div[3]')
        pm2c = self.get_text('xpath', '//*[@id="aqi_list"]/li[2]/div[3]')
        coc = self.get_text('xpath', '//*[@id="aqi_list"]/li[3]/div[3]')
        noc = self.get_text('xpath', '//*[@id="aqi_list"]/li[4]/div[3]')
        soc = self.get_text('xpath', '//*[@id="aqi_list"]/li[5]/div[3]')
        oc = self.get_text('xpath', '//*[@id="aqi_list"]/li[6]/div[3]')
        if pm1c == '可吸入颗粒' and pm2c == '细微颗粒' and coc == '一氧化碳' and noc == '二氧化氮' and soc == '二氧化硫' and oc == '臭氧':
            num += 1
            print(3)
        if num == 3:
            return 1
        else:
            return 2

    # AQI逐小时精细化预报
    def hour_aqi(self):
        try:
            num = 0
            # AQI逐小时精细化预报
            title = self.get_text('xpath', '//*[@id="hour_aqi"]/div[1]/div')

            # 文本
            txt = self.get_attr('xpath', '//*[@id="hour_aqi_list"]', what='aria-label')

            if title == 'AQI逐小时精细化预报':
                num += 1
            print(f'标题：{title},文本：{txt}')
            if '现在空气质量' and 'AQI' in txt:
                num += 1
        except BaseException:
            print('AQI逐小时精细化预报数据获取失败！')
            logger.info('AQI逐小时精细化预报数据获取失败！')
        else:
            if num == 2:
                return 1
            else:
                return 2

    # 多天空气质量预报
    def day_aqi(self):
        try:
            num = 0
            # 多天空气质量预报
            title = self.get_text('xpath', '//*[@id="forecast_aqi"]/div[1]/div')

            #
            time1 = datetime.datetime.now() + datetime.timedelta(days=1)
            time2 = datetime.datetime.now() + datetime.timedelta(days=2)
            time3 = datetime.datetime.now() + datetime.timedelta(days=3)
            time4 = datetime.datetime.now() + datetime.timedelta(days=4)
            time5 = datetime.datetime.now() + datetime.timedelta(days=5)

            month_now = str(daily_month(datetime.datetime.now().strftime('%m月%d日'))) + '/' + str(
                daily_day(datetime.datetime.now().strftime('%m月%d日')))
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

            # week_now = week_deal(datetime.datetime.now().isoweekday())
            week1 = week_deal(time1.isoweekday())
            week2 = week_deal(time2.isoweekday())
            week3 = week_deal(time3.isoweekday())
            week4 = week_deal(time4.isoweekday())
            week5 = week_deal(time5.isoweekday())

            page_month_now = self.get_attr('xpath', '//*[@id="forecast_list"]/li[1]/span[2]', what='textContent')
            page_month1 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[2]/span[2]', what='textContent')
            page_month2 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[3]/span[2]', what='textContent')
            page_month3 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[4]/span[2]', what='textContent')
            page_month4 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[5]/span[2]', what='textContent')
            page_month5 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[6]/span[2]', what='textContent')

            page_week_now = self.get_attr('xpath', '//*[@id="forecast_list"]/li[1]/span[1]', what='textContent')
            page_week1 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[2]/span[1]', what='textContent')
            page_week2 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[3]/span[1]', what='textContent')
            page_week3 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[4]/span[1]', what='textContent')
            page_week4 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[5]/span[1]', what='textContent')
            page_week5 = self.get_attr('xpath', '//*[@id="forecast_list"]/li[6]/span[1]', what='textContent')

            txt1 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="forecast_list"]/li[1]/span[3]/em', what='textContent'))
            txt2 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="forecast_list"]/li[2]/span[3]/em', what='textContent'))
            txt3 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="forecast_list"]/li[3]/span[3]/em', what='textContent'))
            txt4 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="forecast_list"]/li[4]/span[3]/em', what='textContent'))
            txt5 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="forecast_list"]/li[5]/span[3]/em', what='textContent'))
            txt6 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="forecast_list"]/li[6]/span[3]/em', what='textContent'))

            print(
                f'{page_month_now}:{page_week_now}--{page_month1}:{page_week1}--{page_month2}:{page_week2}--{page_month3}:{page_week3}--{page_month4}:{page_week4}--{page_month5}:{page_week5}')
            logger.info(
                f'{page_month_now}:{page_week_now}--{page_month1}:{page_week1}--{page_month2}:{page_week2}--{page_month3}:{page_week3}--{page_month4}:{page_week4}--{page_month5}:{page_week5}')

            if page_week_now == '今天' and page_week1 == week1 and page_week2 == week2 and page_week3 == week3 and page_week4 == week4 and page_week5 == week5:
                num += 1
                print(1)
            if page_month_now == month_now and page_month1 == month1 and page_month2 == month2 and page_month3 == month3 and page_month4 == month4 and page_month5 == month5:
                num += 1
                print(2)
            # print(page_month_now, month_now, page_month1, month1, page_month2, month2, page_month3, month3,
            # page_month4, month4, page_month5, month5)
            if txt1 and txt2 and txt3 and txt4 and txt5 and txt6 == 1:
                num += 1
                print(3)
            if title == '多天空气质量预报':
                num += 1
                print(4)
        except BaseException:
            print('多天空气质量预报信息获取失败！')
            logger.info('多天空气质量预报信息获取失败！')
        else:
            if num == 4:
                return 1
            else:
                return 2

    # 空气排名
    def aqi_top(self):
        try:
            num = 0
            title = self.get_text('xpath', '//*[@id="page_container"]/div[10]/div[1]/div[1]/div[1]')
            txt = self.get_text('xpath', '//*[@id="page_container"]/div[10]/div[1]/div[2]')
            # 排名
            index = self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dt/div[1]')
            # 城市
            city = self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dt/div[2]')
            # 等级
            stat = self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dt/div[3]')
            # AQI
            aqi = self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dt/div[4]')

            # 1
            num1 = int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[1]/div[1]'))
            # 2
            num2 = int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[2]/div[1]'))
            # 3
            num3 = int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[3]/div[1]'))

            # city and province

            c1 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="aqi_rank_list"]/dl/dd[1]/div[2]/span[1]', what='textContent'))
            c2 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="aqi_rank_list"]/dl/dd[1]/div[2]/span[2]', what='textContent'))
            c3 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="aqi_rank_list"]/dl/dd[2]/div[2]/span[1]', what='textContent'))
            c4 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="aqi_rank_list"]/dl/dd[2]/div[2]/span[2]', what='textContent'))
            c5 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="aqi_rank_list"]/dl/dd[3]/div[2]/span[1]', what='textContent'))
            c6 = contain_chinese_one(
                self.get_attr('xpath', '//*[@id="aqi_rank_list"]/dl/dd[3]/div[2]/span[2]', what='textContent'))

            t1 = contain_chinese_one(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[1]/div[3]'))
            t2 = contain_chinese_one(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[2]/div[3]'))
            t3 = contain_chinese_one(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[3]/div[3]'))

            n1 = int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[1]/div[4]'))
            n2 = int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[2]/div[4]'))
            n3 = int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[3]/div[4]'))

            print(f"城市省份：{c1},{c2},{c3},{c4},{c5},{c6}----{txt}")
            logger.info(f"城市省份：{c1},{c2},{c3},{c4},{c5},{c6}----{txt}")

            if title == '全国空气质量排名':
                num += 1
                print(1)
            if index == '排名' and city == '城市' and stat == '等级' and aqi == 'AQI':
                num += 1
                print(2)
            if num1 == 1 and num2 == 2 and num3 == 3:
                num += 1
                print(3)
            if c1 and c2 and c3 and c4 and c5 and c6 == 1:
                num += 1
                print(4)
            if t1 and t2 and t3 == 1:
                num += 1
                print(5)
            if n1 and n2 and n3 <= 500:
                num += 1
                print(6)
            if '击败了全国' and '目前城市排名' in txt:
                num += 1
                print(7)
        except BaseException:
            print('全国空气质量排名 数据获取失败！')
            logger.info('全国空气质量排名 数据获取失败！')
        else:
            if num == 7:
                return 1
            else:
                return 2

    # 空气排名 更多 更多 底部版权
    def aqi_top_more(self, long=400):
        # try:
        num = 0
        button = self.driver.find_element('xpath', '//*[@id="aqi_rg_more"]')
        action = ActionChains(self.driver).move_to_element(button)
        time.sleep(1)
        action.perform()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', long)
        button.click()
        time.sleep(1)

        index = self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dt/div[1]')
        city = self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dt/div[2]')
        stat = self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dt/div[3]')
        aqi = self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dt/div[4]')
        print(index, city, stat, aqi)
        if index == '排名' and city == '城市' and stat == '等级' and aqi == 'AQI':
            num += 1
            print(1)

        if int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[1]/div[1]')) == 1:
            num += 1
            print(2)
        if contain_chinese_one(
                self.get_attr('xpath', '//*[@id="aqi_rank_list"]/dl/dd[1]/div[2]/span[1]', what='textContent')) == 1:
            num += 1
            print(3)
        if contain_chinese_one(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[1]/div[3]')) == 1:
            num += 1
            print(4)
        if int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[1]/div[4]')) <= 500:
            num += 1
            print(5)

        if int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[300]/div[1]')) == 300:
            num += 1
            print(6)
        if contain_chinese_one(
                self.get_attr('xpath', '//*[@id="aqi_rank_list"]/dl/dd[300]/div[2]/span[1]', what='textContent')) == 1:
            num += 1
            print(7)
        if contain_chinese_one(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[300]/div[3]')) == 1:
            num += 1
            print(8)
        if int(self.get_text('xpath', '//*[@id="aqi_rank_list"]/dl/dd[300]/div[4]')) <= 500:
            num += 1
            print(9)

        if Share().copyright() == 1:
            num += 1
            print(10)
        # except BaseException:
        #     print('空气质量排名更多页面元素获取失败！')
        #     logger.info('空气质量排名更多页面元素获取失败！')
        # else:
        if num == 10:
            return 1
        else:
            return 2

    # aqi 生活指南
    def aqi_living_guide(self):
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

    # aqi 生活指南二级页面
    def aqi_living_guide_page_two(self):
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

    # aqi 生活资讯
    def aqi_operate_wrapper(self):
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

    # aqi 生活资讯 更多 页面
    def aqi_operate_wrapper_more(self):
        try:
            i = Share().operate_wrapper_more(450)
        except BaseException:
            print('从共用页面里->调用生活资讯 更多 页面失败！')
            logger.info('从共用页面里->调用生活资讯 更多 页面页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # aqi 天气快讯
    def aqi_reptile_news(self):
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

    # aqi 天气快讯 更多 页面
    def aqi_reptile_news_more(self):
        try:
            i = Share().reptile_news_more(400)
        except BaseException:
            print('从共用页面里->调用天气快讯 更多 页面页面失败！')
            logger.info('从共用页面里->调用天气快讯 更多 页面页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # aqi 天气纵览
    def aqi_news_video(self):
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

    #  aqi 天气纵览 更多 页面
    def aqi_news_video_more(self):
        try:
            i = Share().news_video_more(600)
        except BaseException:
            print('从共用页面里->调用天气纵览 更多 页面失败！')
            logger.info('从共用页面里->调用天气纵览 更多 页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # aqi 猜你喜欢
    def aqi_weather_news(self):
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

    # aqi 猜你喜欢 更多页面
    def aqi_weather_news_more(self):
        try:
            i = Share().weather_news_more(400)
        except BaseException:
            print('从共用页面里->调用猜你喜欢 更多页面失败！')
            logger.info('从共用页面里->调用猜你喜欢 更多页面失败！')
        else:
            if i == 1:
                return 1
            else:
                return 2

    # aqi 版权信息
    def aqi_copyright(self):
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


if __name__ == '__main__':
    a = AqiPage()
    a.aqi_news_video_more()
