import unittest
# from unittestreport import rerun
from H5WebUI.days import DaysPage
from log.Log import logger


class DaysH5TestCase(unittest.TestCase):
    """※※※ 华为H5---15日 页面 ※※※"""

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
    #     # time.sleep(2)
    #
    # def tearDown(self):
    #     pass
    #     # time.sleep(2)

    # def test_01_days_warn_top(self):
    #     """顶部天气预警信息 横幅 显示与正确性校验 """
    #     days = DaysPage()
    #     self.assertEqual(1, days.days_warn_top())

    # def test_18_page_jump(self):
    #     """15日 页面跳转 实况天气 小时天气 生活指数 新闻资讯"""
    #     days = DaysPage()
    #     self.assertEqual(1, days.page_jump())

    def test_02_forecast_list_date(self):
        """判断主卡片，星期，日期，空气质量，天气状态图片，温度，天气情况，风 显示 15日主卡片"""
        days = DaysPage()
        self.assertEqual(1, days.forecast_list_date())

    def test_03_future_remind(self):
        """ 判断主卡片下 文字描述最近降雨情况 显示 校验 """
        days = DaysPage()
        self.assertEqual(1, days.future_remind())

    def test_04_future_remind_click(self):
        """ 判断主卡片下 文字描述最近降雨情况 点击后跳转情况 检查 """
        days = DaysPage()
        self.assertTrue(1, days.future_remind_click())

    def test_05_days_news_video(self):
        """15日 天气纵览 显示校验"""
        days = DaysPage()
        self.assertEqual(1, days.days_news_video())

    def test_06_days_news_video_more(self):
        """15日 天气纵览 更多 检查"""
        days = DaysPage()
        self.assertEqual(1, days.days_news_video_more())

    def test_07_days_operate_wrapper(self):
        """15日 生活资讯 检查"""
        days = DaysPage()
        self.assertEqual(1, days.days_operate_wrapper())

    def test_08_days_operate_wrapper_more(self):
        """15日 生活资讯 更多 检查"""
        days = DaysPage()
        self.assertEqual(1, days.days_operate_wrapper_more())

    def test_09_days_pic(self):
        """15日 图集专题 校验"""
        days = DaysPage()
        self.assertEqual(1, days.days_pic())

    def test_10_days_pic_more(self):
        """15日 图集专题 更多 检查"""
        days = DaysPage()
        self.assertEqual(1, days.days_pic_more())

    def test_11_days_living_guide(self):
        """15日 生活指南 检查"""
        days = DaysPage()
        self.assertEqual(1, days.days_living_guide())

    def test_12_days_living_guide_page_two(self):
        """15日 生活指南 二级 检查"""
        days = DaysPage()
        self.assertEqual(1, days.days_living_guide_page_two())

    def test_13_days_fes_news(self):
        """15日 节日节气 显示检查"""
        days = DaysPage()
        self.assertEqual(1, days.days_fes_news())

    def test_14_days_fes_news_more(self):
        """15日 节日节气 更多 页面 检查"""
        days = DaysPage()
        self.assertEqual(1, days.days_fes_news_more())

    def test_15_days_weather_news(self):
        """15日 猜你喜欢 检查"""
        days = DaysPage()
        self.assertEqual(1, days.days_weather_news())

    def test_16_days_weather_news_more(self):
        """15日 猜你喜欢 更多 显示校验"""
        days = DaysPage()
        self.assertEqual(1, days.days_weather_news_more())

    def test_17_days_copyright(self):
        """15日 底部版权信息 校验"""
        days = DaysPage()
        self.assertEqual(1, days.days_copyright())




if __name__ == '__main__':
    unittest.main(verbosity=2)
