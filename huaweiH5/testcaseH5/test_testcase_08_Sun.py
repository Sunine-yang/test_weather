import unittest
# from unittestreport import rerun
from H5WebUI.sun import SunPage
from log.Log import logger


class SunH5TestCase(unittest.TestCase):
    """※※※ 华为H5---日出日落 页面 ※※※"""

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
    def test_01_sun_card(self):
        """日出日落主卡片 显示与正确性校验 """
        sun = SunPage()
        self.assertEqual(1, sun.sun_card())

    def test_02_moon_phase(self):
        """月相_显示与正确性校验 """
        sun = SunPage()
        self.assertEqual(1, sun.moon_phase())

    def test_03_sun_living_guide(self):
        """ sun 生活指南 显示与正确性校验 """
        sun = SunPage()
        self.assertEqual(1, sun.sun_living_guide())

    def test_04_sun_living_guide_page_two(self):
        """sun 生活指南二级页面 逻辑与显示校验"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_living_guide_page_two())

    def test_05_sun_operate_wrapper(self):
        """sun 摄影技巧 检查"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_operate_wrapper())

    def test_06_sun_operate_wrapper_more(self):
        """sun 摄影技巧 更多 页面 检查"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_operate_wrapper_more())

    def test_07_sun_reptile_news(self):
        """sun 天气快讯 检查"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_reptile_news())

    def test_08_sun_reptile_news_more(self):
        """sun 天气快讯 更多 页面 显示校验"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_reptile_news_more())

    def test_09_sun_news_video(self):
        """sun  天气纵览 显示是否正常检查"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_news_video())

    def test_10_sun_news_video_more(self):
        """sun 天气纵览 更多 页面 显示检查"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_news_video_more())

    def test_11_sun_weather_news(self):
        """sun 猜你喜欢 检查"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_weather_news())

    def test_12_sun_weather_news_more(self):
        """sun 猜你喜欢 更多 显示检查"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_weather_news_more())

    def test_13_sun_copyright(self):
        """sun 底部版权信息 检查"""
        sun = SunPage()
        self.assertEqual(1, sun.sun_copyright())


if __name__ == '__main__':
    unittest.main(verbosity=2)
