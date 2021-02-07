import unittest
# from unittestreport import rerun
from H5WebUI.daysNinety import DaysNinetyPage
from log.Log import logger


class DaysNinety(unittest.TestCase):
    """※※※ 华为H5---90日 页面 ※※※"""

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
    #     # time.sleep(2)
    #     pass
    # def tearDown(self):
    #     # time.sleep(2)
    #     pass
    def test_01_days_ninety_card(self):
        """90日 主卡片 显示与正确性校验 """
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.days_ninety_card())

    def test_02_days_ninety_scenic(self):
        """90日 周边景区 显示与正确性校验 """
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.days_ninety_scenic())

    def test_03_days_ninety_scenic_click(self):
        """ 90日 周边景区点击景点切换城市 校验 """
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.days_ninety_scenic_click())

    def test_04_days_ninety_scenic_page_two(self):
        """ 90日 周边景区二级页面 检查 """
        days_ninety = DaysNinetyPage()
        self.assertTrue(1, days_ninety.days_ninety_scenic_page_two())

    def test_05_days_ninety_operate_wrapper(self):
        """90日 生活指南 显示校验"""
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.days_ninety_operate_wrapper())

    def test_06_days_ninety_operate_wrapper_more(self):
        """90日 生活指南二级页面 检查"""
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.days_ninety_operate_wrapper_more())

    def test_07_daysNinety_reptile_news(self):
        """90日 天气快讯 检查"""
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.daysNinety_reptile_news())

    def test_08_daysNinety_reptile_news_more(self):
        """90日 天气快讯 更多 页面 检查"""
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.daysNinety_reptile_news_more())

    def test_09_daysNinety_news_video(self):
        """90日 天气纵览 更多 页面 显示校验"""
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.daysNinety_news_video())

    def test_10_daysNinety_news_video_more(self):
        """90日 天气纵览 更多 页面 检查"""
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.daysNinety_news_video_more())

    def test_11_daysNinety_weather_news(self):
        """90日 猜你喜欢 检查"""
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.daysNinety_weather_news())

    def test_12_data_daysNinety_weather_news_more(self):
        """90日 猜你喜欢 更多页面 检查"""
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.daysNinety_weather_news_more())

    def test_13_daysNinety_copyright(self):
        """90日 版权信息 显示检查"""
        days_ninety = DaysNinetyPage()
        self.assertEqual(1, days_ninety.daysNinety_copyright())


if __name__ == '__main__':
    unittest.main(verbosity=2)
