import unittest
# from unittestreport import rerun
from H5WebUI.aqi import AqiPage
from log.Log import logger


class AqiH5TestCase(unittest.TestCase):
    """※※※ 华为H5---空气质量 页面 ※※※"""

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
    #
    # def tearDown(self):
    #     # time.sleep(2)
    #     pass
    def test_01_aqi_card(self):
        """空气质量 主卡片 显示与正确性校验 """
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_card())

    def test_02_aqi_detail(self):
        """主卡片下各项数据 显示与正确性校验 """
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_detail())

    def test_03_hour_aqi(self):
        """ AQI逐小时精细化预报 显示与正确性校验 """
        aqi = AqiPage()
        self.assertEqual(1, aqi.hour_aqi())

    def test_04_day_aqi(self):
        """ 多天空气质量预报_逻辑正确性检查 """
        aqi = AqiPage()
        self.assertTrue(1, aqi.day_aqi())

    def test_05_aqi_top(self):
        """空气排名 显示校验"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_top())

    def test_06_aqi_top_more(self):
        """空气排名 更多 更多 底部版权 检查"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_top_more())

    def test_07_aqi_living_guide(self):
        """aqi 生活指南 检查"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_living_guide())

    def test_08_aqi_living_guide_page_two(self):
        """aqi 生活指南二级页面 检查"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_living_guide_page_two())

    def test_09_aqi_operate_wrapper(self):
        """aqi 生活资讯 显示校验"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_operate_wrapper())

    def test_10_aqi_operate_wrapper_more(self):
        """aqi 生活资讯 更多 页面 检查"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_operate_wrapper_more())

    def test_11_aqi_reptile_news(self):
        """aqi 天气快讯 检查"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_reptile_news())

    def test_12_aqi_reptile_news_more(self):
        """aqi 天气快讯 更多 页面 检查"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_reptile_news_more())

    def test_13_aqi_news_video(self):
        """aqi 天气纵览 显示检查"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_news_video())

    def test_14_aqi_news_video_more(self):
        """aqi 天气纵览 更多 页面 检查"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_news_video_more())

    def test_15_aqi_weather_news(self):
        """aqi 猜你喜欢 检查"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_weather_news())

    def test_16_aqi_weather_news_more(self):
        """aqi 猜你喜欢 更多页面 显示校验"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_weather_news_more())

    def test_17_aqi_copyright(self):
        """aqi 版权信息 校验"""
        aqi = AqiPage()
        self.assertEqual(1, aqi.aqi_copyright())


if __name__ == '__main__':
    unittest.main(verbosity=2)
