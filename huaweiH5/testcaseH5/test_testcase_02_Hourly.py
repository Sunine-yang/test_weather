import unittest
from H5WebUI.hourly import HourlyPage
# from unittestreport import rerun

from log.Log import logger


class HourlyH5TestCase(unittest.TestCase):
    """※※※ 华为H5---逐小时页面 ※※※"""

    # @rerun(count=4, interval=2)
    @classmethod
    def setUpClass(cls):
        print('——————开始执行用例！——————')
        logger.info('——————开始执行用例！——————')

    @classmethod
    def tearDownClass(cls):
        print('——————用例执行结束！——————')
        logger.info('——————用例执行结束！——————')

    # def setUp(self):
    #     pass
    #     # time.sleep(2)
    #
    # def tearDown(self):
    #     pass
    #     # time.sleep(2)

    # def test_01_top_warn(self):
    #     """检查顶部天气预警横幅"""
    #     hourly = HourlyPage()
    #     self.assertEqual(1, hourly.hourly_warn_top())

    def test_02_card_title(self):
        """检查主卡片顶部信息,现在气温 与 实况实时气温"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.card_title())

    def test_03_hour_list(self):
        """判断温度显示与温度折线图对应关系"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hour_list())

    def test_04_timelist(self):
        """判断底部时间是否显示正常"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.timelist())

    def test_05_hourly_weather_item_icon(self):
        """天气各项数据卡片图标检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_weather_item_icon())

    def test_06_hourly_weather_item_data(self):
        """天气各项数据卡片数据检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_weather_item_data())

    def test_07_hourly_weather_item_txt(self):
        """天气各项数据卡片文字描述检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_weather_item_txt())

    def test_08_hourly_operate_wrapper(self):
        """生活资讯 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_operate_wrapper())

    def test_09_hourly_operate_wrapper_more(self):
        """生活资讯 更多 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_operate_wrapper_more())

    def test_10_hourly_scenic(self):
        """周边景区 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_scenic())

    def test_11_hourly_scenic_click(self):
        """周边景区点击景点切换城市 功能检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_scenic_click())

    def test_12_hourly_scenic_page_two(self):
        """周边景区二级页面 跳转及内容显示检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_scenic_page_two())

    def test_13_hourly_living_guide(self):
        """生活指南 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_living_guide())

    def test_14_hourly_living_guide_page_two(self):
        """生活指南 二级页面模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_living_guide_page_two())

    def test_15_hourly_reptile_news(self):
        """天气快讯 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_reptile_news())

    def test_16_hourly_reptile_news_more(self):
        """天气快讯 更多 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_reptile_news_more())

    def test_17_hourly_news_video(self):
        """天气纵览 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_news_video())

    def test_18_hourly_news_video_more(self):
        """天气纵览 更多 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_news_video_more())

    def test_19_hourly_weather_news(self):
        """猜你喜欢 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_weather_news())

    def test_20_hourly_weather_news_more(self):
        """猜你喜欢 更多 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_weather_news_more())

    def test_21_hourly_copyright(self):
        """版权信息 模块检查"""
        hourly = HourlyPage()
        self.assertEqual(1, hourly.hourly_copyright())

    # def test_22_page_jump(self):
    #     """页面跳转 实况天气 多天预报 生活指数 新闻资讯"""
    #     hourly = HourlyPage()
    #     self.assertEqual(1, hourly.page_jump())


if __name__ == '__main__':
    unittest.main(verbosity=2)
