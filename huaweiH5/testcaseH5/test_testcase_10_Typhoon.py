import unittest
# from unittestreport import rerun
from H5WebUI.typhoon import TyphoonPage
from log.Log import logger
from util.kill_driver import kill_driver


class TodayH5TestCase(unittest.TestCase):
    """※※※ 华为H5--- 台风专题 ※※※"""

    # @rerun(count=4, interval=2)
    @classmethod
    def setUpClass(cls):
        print('——————开始执行用例！——————')
        logger.info('——————开始执行用例！——————')
    #
    #
    # def setUp(self):
    #     # time.sleep(2)
    #     pass
    #
    # def tearDown(self):
    #     # time.sleep(2)
    #     pass
    def test_01_first_typhoon(self):
        """滚屏文字 台风简介  检查"""
        typhoon = TyphoonPage()
        self.assertEqual(1, typhoon.first_typhoon())

    def test_02_dynamic_typhoon(self):
        """台风动态 环高 间隔时间段台风资讯校验 """
        typhoon = TyphoonPage()
        self.assertEqual(1, typhoon.dynamic_typhoon())

    def test_03_video_one(self):
        """ 科普视频 检查 """
        typhoon = TyphoonPage()
        self.assertEqual(1, typhoon.video_one())

    def test_04_video_two(self):
        """ 气象视频 检查 """
        typhoon = TyphoonPage()
        self.assertTrue(1, typhoon.video_two())

    def test_05_news(self):
        """新闻资讯 检查"""
        typhoon = TyphoonPage()
        self.assertEqual(1, typhoon.news())

    def test_06_knowledge(self):
        """知识科普 检查"""
        typhoon = TyphoonPage()
        self.assertEqual(1, typhoon.knowledge())

    @classmethod
    def tearDownClass(cls):
        print('——————用例执行结束！——————')
        logger.info('——————用例执行结束！——————')
        kill_driver()


if __name__ == '__main__':
    unittest.main(verbosity=2)
