import unittest
from H5WebUI.life import LifePage
from log.Log import logger


class LifeH5TestCase(unittest.TestCase):
    """※※※ 华为H5---生活指数 页面 ※※※"""

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
    #     time.sleep(2)
    #     pass
    def test_01_life_card(self):
        """生活指数 主卡片 显示与正确性校验 """
        life = LifePage()
        self.assertEqual(1, life.life_card())

    def test_02_life_list(self):
        """生活指数 列表 显示与正确性校验 """
        life = LifePage()
        self.assertEqual(1, life.life_list())

    def test_03_spot_card(self):
        """ 运动健康 显示与正确性校验 """
        life = LifePage()
        self.assertEqual(1, life.spot_card())

    def test_04_life_operate_wrapper(self):
        """ life 生活资讯  检查 """
        life = LifePage()
        self.assertTrue(1, life.life_operate_wrapper())

    def test_05_life_operate_wrapper_more(self):
        """life 生活资讯 更多 页面 校验"""
        life = LifePage()
        self.assertEqual(1, life.life_operate_wrapper_more())

    def test_06_life_reptile_news(self):
        """life 天气快讯 检查"""
        life = LifePage()
        self.assertEqual(1, life.life_reptile_news())

    def test_07_life_reptile_news_more(self):
        """life 天气快讯 更多 页面 检查"""
        life = LifePage()
        self.assertEqual(1, life.life_reptile_news_more())

    def test_08_life_news_video(self):
        """life 天气纵览 检查"""
        life = LifePage()
        self.assertEqual(1, life.life_news_video())

    def test_09_life_news_video_more(self):
        """life 天气纵览 更多 页面 显示校验"""
        life = LifePage()
        self.assertEqual(1, life.life_news_video_more())

    def test_10_life_weather_news(self):
        """life 猜你喜欢 检查"""
        life = LifePage()
        self.assertEqual(1, life.life_weather_news())

    def test_11_life_weather_news_more(self):
        """life 猜你喜欢 更多页面 检查"""
        life = LifePage()
        self.assertEqual(1, life.life_weather_news_more())

    def test_12_life_copyright(self):
        """life 版权信息 检查"""
        life = LifePage()
        self.assertEqual(1, life.life_copyright())

    def test_13_life_list_click(self):
        """life 生活指数 列表 点击跳转 检查"""
        life = LifePage()
        self.assertEqual(1, life.life_list_click())


if __name__ == '__main__':
    unittest.main(verbosity=2)
