import datetime
import time

from common.common_page import Share
from log.Log import logger
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_driver import UtilWebDriver
from util.regular_deal import sun_come_deal, sun_left_deal, moon_come_deal, moon_left_deal, moon_left_day_deal, \
    last_long


class SunPage(FindElement):
    def __init__(self):
        super(SunPage, self).__init__()
        self.driver = UtilWebDriver.get_driver()
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/sun.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4'
            f'&source=zm&oriId=P6')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/sun.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4'
            f'&source=zm&oriId=P6')
        self.driver.implicitly_wait(10)
        # # 天气文字描述 实况当前温度 天气预警信息 最高温度 最低温度
        # today_data = Share().today_data()
        time.sleep(2)

    # 日出日落主卡片
    def sun_card(self):
        try:
            # 日出日落 标题
            title = self.get_attr('xpath', '//*[@id="moonhpase_box"]/span', what='textContent')

            # 日出日落字段 eg:日出时间清晨06:11 日落时间下午17:04 月出时间,中午13:05,月落时间,晚上22:38
            txt = self.get_attr('xpath', '//*[@id="sunrise_box"]', what='aria-label')

            sun_come = datetime.datetime.strptime(last_long(sun_come_deal(txt), 5), '%H:%M')
            sun_letf = datetime.datetime.strptime(last_long(sun_left_deal(txt), 5), '%H:%M')

            moon_come = datetime.datetime.strptime(last_long(moon_come_deal(txt), 5), '%H:%M')
            moon_left = datetime.datetime.strptime(last_long(moon_left_deal(txt), 5), '%H:%M')
            # 显示是否为明天
            moon_left_day = moon_left_day_deal(moon_left_deal(txt))
            moon_come_day = moon_left_day_deal(moon_come_deal(txt))
            print(txt)
            print(moon_come_day)
            # http://h5.zuimeitianqi.com/page/zh/res/img/wea_svg/ic_sunrise_color.svg
            src1 = self.get_attr('xpath', '//*[@id="sunIcon"]', what='src')
            # http://h5.zuimeitianqi.com/page/zh/res/img/wea_svg/ic_sunset_color.svg
            src2 = self.get_attr('xpath', '//*[@id="moonIcon"]', what='src')

            num = 0
            if title == '日出日落':
                num += 1
                print(1)
                print(f'标题为：{title}')
                logger.info(f'标题为：{title}')

            if sun_letf > sun_come:
                num += 1
                print(2)
                print(f'日出时间为：{sun_come},日落时间为：{sun_letf}')
                logger.info(f'日出时间为：{sun_come},日落时间为：{sun_letf}')
            if moon_left_day == '明天':
                num += 1
                print(3)
                print(f'是否明天？：{moon_left_day},月出时间：{moon_come},月落时间：{moon_left}')
                logger.info(f'是否明天？：{moon_left_day},月出时间：{moon_come},月落时间：{moon_left}')
            elif moon_come_day == '昨天':
                num += 1
                print(3)
            elif moon_left > moon_come:
                num += 1
                print(3)
                print(f'是否明天？：{moon_left_day},月出时间：{moon_come},月落时间：{moon_left}')
                logger.info(f'是否明天？：{moon_left_day},月出时间：{moon_come},月落时间：{moon_left}')

            if src1 == 'http://s1.zuimeitianqi.com/page/dist/res/img/wea_svg/ic_sunrise_color.svg' and src2 == 'http://s1.zuimeitianqi.com/page/dist/res/img/wea_svg/ic_sunset_color.svg':
                num += 1
                print(4)
                print(f'src1:{src1},src2:{src2}')
                logger.info(f'src1:{src1},src2:{src2}')
        except BaseException:
            print('日出日落主卡片内元素获取失败！')
            logger.info('日出日落主卡片内元素获取失败！')
        else:
            if num == 4:
                return 1
            else:
                return 2

    # 月相
    def moon_phase(self):
        num = 0
        # 月相
        title = self.get_text('xpath', '//*[@id="moon_phase_box"]/div[1]/div')
        # 图片 .png
        pic = last_long(self.get_attr('xpath', '//*[@id="moon_phase"]/div[1]/img', what='src'), 4)
        # 月相名称 月
        name = last_long(self.get_attr('xpath', '//*[@id="moon_phase"]/div[1]/span', what='textContent'), 1)
        # 天数 天 距离
        last_day = last_long(self.get_attr('xpath', '//*[@id="moon_phase"]/div[3]/span[2]', what='textContent'), 1)
        first_day = moon_left_day_deal(
            self.get_attr('xpath', '//*[@id="moon_phase"]/div[3]/span[2]', what='textContent'))

        if title == '月相':
            num += 1
            print(1)
        if pic == '.png':
            num += 1
            print(2)
        if name == '月':
            num += 1
            print(3)
        if last_day == '天':
            num += 1
            print(4)
        if first_day == '距离':
            num += 1
            print(5)

        if num == 5:
            return 1
        else:
            return 2

    # sun 生活指南
    def sun_living_guide(self):
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

    # sun 生活指南二级页面
    def sun_living_guide_page_two(self):
        try:
            i = Share().living_guide_page_two(380)
        except BaseException:
            print('从共用页面里->调用生活指南二级页面失败！')
            logger.info('从共用页面里->调用生活指南二级页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # sun 摄影技巧
    def sun_operate_wrapper(self):
        try:
            i = Share().operate_wrapper()
        except BaseException:
            print('从共用页面里->调用摄影技巧页面失败！')
            logger.info('从共用页面里->调用摄影技巧页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # sun 摄影技巧 更多 页面
    def sun_operate_wrapper_more(self):
        try:
            i = Share().operate_wrapper_more(300)
        except BaseException:
            print('从共用页面里->调用生活资讯 更多 页面失败！')
            logger.info('从共用页面里->调用生活资讯 更多 页面页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # sun 天气快讯
    def sun_reptile_news(self):
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

    # sun 天气快讯 更多 页面
    def sun_reptile_news_more(self):
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

    # sun  天气纵览
    def sun_news_video(self):
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

    # sun 天气纵览 更多 页面
    def sun_news_video_more(self):
        try:
            i = Share().news_video_more(650)
        except BaseException:
            print('从共用页面里->调用天气纵览 更多 页面失败！')
            logger.info('从共用页面里->调用天气纵览 更多 页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # sun 猜你喜欢
    def sun_weather_news(self):
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

        # today猜你喜欢 更多页面

    # sun 猜你喜欢 更多
    def sun_weather_news_more(self):
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

        # today版权信息

    # sun 底部版权信息
    def sun_copyright(self):
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
    print(SunPage().sun_news_video_more())
    # print(SunPage().moon_phase())
    # print(SunPage().sun_living_guide())
    # print(SunPage().sun_living_guide_page_two())
    # print(SunPage().sun_reptile_news())
    # print(SunPage().sun_reptile_news_more())
    # print(SunPage().sun_news_video())
    # print(SunPage().sun_news_video_more())
    # print(SunPage().sun_weather_news())
    # print(SunPage().sun_weather_news_more())
    # print(SunPage().sun_copyright())
