import time

from common.common_page import Share
from log.Log import logger
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_driver import UtilWebDriver


class DaysNinetyPage(FindElement):
    def __init__(self):
        # 继承find element类
        super(DaysNinetyPage, self).__init__()
        # 创建配置文件读取对象
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        # 调用单例模式的driver
        self.driver = UtilWebDriver.get_driver()
        # 打开实况界面
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/daysNinety.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
            '=A1&orild=P4&source=zm&oriId=P2')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/daysNinety.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
            '=A1&orild=P4&source=zm&oriId=P2')
        self.driver.implicitly_wait(10)
        time.sleep(2)

    # 90日 主卡片   —————————————— 等待改版重写 ————————————————
    def days_ninety_card(self):
        return 1

    # 90日 周边景区
    def days_ninety_scenic(self):
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

    # 90日 周边景区点击景点切换城市
    def days_ninety_scenic_click(self):
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

    # 90日 周边景区二级页面
    def days_ninety_scenic_page_two(self):
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

    # 90日 生活资讯
    def days_ninety_operate_wrapper(self):
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

    # 90日 生活资讯 更多 页面
    def days_ninety_operate_wrapper_more(self):
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

    # 90日 天气快讯
    def daysNinety_reptile_news(self):
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

    # 90日 天气快讯 更多 页面
    def daysNinety_reptile_news_more(self):
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

    # 90日 天气纵览
    def daysNinety_news_video(self):
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

    # 90日 天气纵览 更多 页面
    def daysNinety_news_video_more(self):
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

    # 90日 猜你喜欢
    def daysNinety_weather_news(self):
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

    # 90日 猜你喜欢 更多页面
    def daysNinety_weather_news_more(self):
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

    # 90日 版权信息
    def daysNinety_copyright(self):
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

    # 页面跳转 实况天气 小时天气 生活指数 新闻资讯
    def page_jump(self):
        try:
            today_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/img', what='src')
            today_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/span', what='textContent')

            hour_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/img', what='src')
            hour_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/span', what='textContent')

            comfor_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/img', what='src')
            comfor_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/span', what='textContent')

            news_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/img', what='src')
            news_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/span', what='textContent')
        except BaseException:
            print('页面跳转 实况天气 小时天气 生活指数 新闻资讯 获取内容失败！')
            logger.info('页面跳转 实况天气 小时天气 生活指数 新闻资讯 获取内容失败！')
        else:
            num = 0
            if today_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_now.svg' \
                    and hour_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_hourly.svg' \
                    and comfor_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_live.svg' \
                    and news_img == 'http://h5.zuimeitianqi.com/page/zh/res/img/page_btn/btn_page_news.svg':
                num += 1
                print(1)
            if today_txt == '实况天气' and hour_txt == '小时天气' and comfor_txt == '生活指数' and news_txt == '新闻资讯':
                num += 1
                print(2)

            self.click('xpath', '//*[@id="page_jump"]/ul/li[1]/img')
            time.sleep(1)
            page_url = self.driver.current_url
            if 'today' in page_url:
                num += 1
                print(3)
            self.driver.back()
            time.sleep(1)

            self.click('xpath', '//*[@id="page_jump"]/ul/li[2]/img')
            time.sleep(1)
            page_url = self.driver.current_url
            if 'hourly' in page_url:
                num += 1
                print(4)
            self.driver.back()
            time.sleep(1)

            self.click('xpath', '//*[@id="page_jump"]/ul/li[3]/img')
            time.sleep(1)
            page_url = self.driver.current_url
            if 'comfor' in page_url:
                num += 1
                print(5)
            self.driver.back()
            time.sleep(1)

            self.click('xpath', '//*[@id="page_jump"]/ul/li[4]/img')
            time.sleep(1)
            page_url = self.driver.current_url
            if 'news' in page_url:
                num += 1
                print(6)
            self.driver.back()
            time.sleep(1)

            if num == 6:
                return 1
            else:
                return 2

if __name__ == '__main__':
    a = DaysNinetyPage()
    print(a.daysNinety_news_video_more())
