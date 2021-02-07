import unittest
from H5WebUI.daily import DailyPage
# from unittestreport import rerun
from log.Log import logger


class DailyH5TestCase(unittest.TestCase):
    """※※※ 华为H5---每日页面 ※※※"""

    # @rerun(count=4, interval=2)
    @classmethod
    def setUpClass(cls):
        print('——————开始执行用例！——————')
        logger.info('——————开始执行用例！——————')

    @classmethod
    def tearDownClass(cls):
        print('——————用例执行结束！——————')
        logger.info('——————用例执行结束！——————')

    #
    # def setUp(self):
    #     pass
    #     # time.sleep(1)
    #
    # def tearDown(self):
    #     pass
    #     # time.sleep(1)

    # def test_01_daily_warn_top(self):
    #     """检查天气预警顶部横幅"""
    #     daily = DailyPage()
    #     self.assertEqual(1, daily.daily_warn_top())

    # def test_21_daily_copyright(self):
    # """每日 页面跳转 小时天气 多天预报 生活指数 新闻资讯"""
    #     daily = DailyPage()
    #     self.assertEqual(1, daily.page_jump())

    def test_02_daily_date_click(self):
        """检查 天数，日期，星期 """
        daily = DailyPage()
        self.assertEqual(1, daily.daily_date_click())

    def test_03_daily_display(self):
        """检查 白天夜间按钮 最低最高气温 随机一天的卡片信息检查 """
        daily = DailyPage()
        self.assertEqual(1, daily.daily_display())

    def test_04_daily_detail(self):
        """ 天气详情 图标 数据 文字描述 """
        daily = DailyPage()
        self.assertEqual(1, daily.daily_detail())

    def test_05_daily_rain(self):
        """降水 模块的显示正确性检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_rain())

    def test_06_daily_calendar(self):
        """今日运势 模块的显示正确性检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_calendar())

    def test_07_calendar_page_two(self):
        """今日运势 日历 二级页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.calendar_page_two())

    def test_08_constellation_page_two(self):
        """今日运势 星座 二级页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.constellation_page_two())

    def test_09_more_calendar(self):
        """今日运势 更多 页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.more_calendar())

    def test_10_daily_living_guide(self):
        """每日 生活指南 检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_living_guide())

    def test_11_daily_living_guide_page_two(self):
        """ 每日 生活指南 二级页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_living_guide_page_two())

    def test_12_daily_operate_wrapper(self):
        """每日 生活资讯 检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_operate_wrapper())

    def test_13_daily_operate_wrapper_more(self):
        """每日 生活资讯 更多页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_operate_wrapper_more())

    def test_14_daily_reptile_news(self):
        """每日 天气快讯 页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_reptile_news())

    def test_15_daily_reptile_news_more(self):
        """每日 天气快讯 更多 页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_reptile_news_more())

    def test_16_daily_news_video(self):
        """每日 天气纵览 页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_news_video())

    def test_17_daily_news_video_more(self):
        """每日 天气纵览 更多 页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_news_video_more())

    def test_18_daily_weather_news(self):
        """猜你喜欢 页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_weather_news())

    def test_19_daily_weather_news_more(self):
        """猜你喜欢 更多 页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_weather_news_more())

    def test_20_daily_copyright(self):
        """每日 版权信息 以及二级页面检查"""
        daily = DailyPage()
        self.assertEqual(1, daily.daily_copyright())

    def test_22_daily_sun(self):
        """每日 日出日落"""
        daily = DailyPage()
        self.assertEqual(1, daily.sun())

    def test_23_daily_sun_page_two(self):
        """每日 日出日落二级页面"""
        daily = DailyPage()
        self.assertEqual(1, daily.sun_page_two())


if __name__ == '__main__':
    unittest.main(verbosity=2)
