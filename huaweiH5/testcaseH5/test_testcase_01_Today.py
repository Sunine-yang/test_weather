import unittest

from H5WebUI.today import TodayPage
from log.Log import logger


# from unittestreport import rerun


class TodayH5TestCase(unittest.TestCase):
    """※※※ 华为H5---实况页面 ※※※"""

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
    #     # time.sleep(2)
    #     pass
    #
    # def tearDown(self):
    #     # time.sleep(2)
    #     pass

    # def test_09_warn(self):
    #     """天气预警信息 显示与顶部滚动横幅显示校验"""
    #     today = TodayPage()
    #     self.assertEqual(1, today.warn())

    # def test_33_game(self):
    #     """小游戏 和 小游戏更多页面 检查"""
    #     today = TodayPage()
    #     self.assertEqual(1, today.game())

    # def test_32_page_jump(self):
    #     """页面跳转 小时天气 多天预报 生活指数 新闻资讯"""
    #     today = TodayPage()
    #     self.assertEqual(1, today.page_jump())

    def test_01_cityname(self):
        """城市名称_显示与正确性校验 """
        today = TodayPage()
        self.assertEqual(1, today.cityname())

    def test_02_date(self):
        """当前日期_显示与正确性校验 """
        today = TodayPage()
        self.assertEqual(1, today.date())

    def test_03_weekday(self):
        """ 星期几_显示与正确性校验 """
        today = TodayPage()
        self.assertEqual(1, today.weekday())

    def test_04_range_tmp(self):
        """ 最低最高温度_逻辑正确性检查 """
        today = TodayPage()
        self.assertTrue(1, today.range_tmp())

    def test_05_tmp(self):
        """当前实况温度 逻辑与显示校验"""
        today = TodayPage()
        self.assertEqual(1, today.tmp())

    def test_06_api(self):
        """空气质量 数值合理性检查"""
        today = TodayPage()
        self.assertEqual(1, today.api())

    def test_07_api_word(self):
        """空气质量 数值与文字描述是否相匹配检查"""
        today = TodayPage()
        self.assertEqual(1, today.api_word())

    def test_08_wea_txt_icon(self):
        """天气状况 文字描述与图标是否匹配检查"""
        today = TodayPage()
        self.assertEqual(1, today.wea_txt_icon())

    def test_10_warn_page_two(self):
        """天气预警信息 二级页面内容显示是否正常检查"""
        today = TodayPage()
        self.assertEqual(1, today.warn_page_two())

    def test_11_hum_tmp(self):
        """实况温度与温度文字 描述是否相匹配"""
        today = TodayPage()
        self.assertEqual(1, today.hum_tmp())

    def test_12_data_sources(self):
        """天气数据来源 中国气象检查"""
        today = TodayPage()
        self.assertEqual(1, today.data_sources())

    def test_13_weather_item_icon(self):
        """天气各项数据卡片 图标显示检查"""
        today = TodayPage()
        self.assertEqual(1, today.weather_item_icon())

    def test_14_weather_item_data(self):
        """天气各项数据卡片 数据显示及合理性检查"""
        today = TodayPage()
        self.assertEqual(1, today.weather_item_data())

    def test_15_weather_item_txt(self):
        """天气各项数据卡片 文字描述检查"""
        today = TodayPage()
        self.assertEqual(1, today.weather_item_txt())

    def test_16_sun(self):
        """日出日落 逻辑以及显示校验"""
        today = TodayPage()
        self.assertEqual(1, today.sun())

    def test_17_sun_page_two(self):
        """日出日落 二级页面跳转校验"""
        today = TodayPage()
        self.assertEqual(1, today.sun_page_two())

    def test_18_radar(self):
        """分钟预报 模块是否显示校验"""
        today = TodayPage()
        self.assertEqual(1, today.radar())

    def test_19_radar_page_two(self):
        """分钟预报 二级页面跳转及内容显示校验"""
        today = TodayPage()
        self.assertEqual(1, today.radar_page_two())

    def test_20_living_guide(self):
        """生活指南 模块内容显示正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_living_guide())

    def test_21_living_guide_page_two(self):
        """生活指南 二级页面跳转正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_living_guide_page_two())

    def test_22_operate_wrapper(self):
        """生活资讯 模块内容及显示正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_operate_wrapper())

    def test_23_operate_wrapper_more(self):
        """生活资讯 更多页面 模块内容及显示正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_operate_wrapper_more())

    def test_24_reptile_news(self):
        """天气快讯 模块内容及显示正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_reptile_news())

    def test_25_reptile_news_more(self):
        """天气快讯 更多页面 模块内容及显示正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_reptile_news_more())

    def test_26_news_video(self):
        """天气纵览 模块内容以及显示正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_news_video())

    def test_27_news_video_more(self):
        """天气纵览 更多页面 模块内容以及显示正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_news_video_more())

    def test_28_today_weather_news(self):
        """猜你喜欢 模块正确性及显示正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_weather_news())

    def test_29_today_weather_news_more(self):
        """猜你喜欢 更多页面 模块正确性及显示正确性校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_weather_news_more())

    def test_30_today_copyright(self):
        """版权信息 最底部版权信息显示及内容校验"""
        today = TodayPage()
        self.assertEqual(1, today.today_copyright())

    def test_31_change_city(self):
        """实况书卡片 搜索切换城市功能 """
        today = TodayPage()
        self.assertEqual(1, today.change_city())


if __name__ == '__main__':
    unittest.main(verbosity=2)
