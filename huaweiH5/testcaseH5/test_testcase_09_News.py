import unittest
# from unittestreport import rerun
from H5WebUI.news import NewsPage
from log.Log import logger


class NewsH5TestCase(unittest.TestCase):
    """※※※ 华为H5---直击现场 页面 ※※※"""

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

    def test_01_title_picture(self):
        """检查直击天气现场 logo图片显示与正确性"""
        news = NewsPage()
        self.assertEqual(1, news.title_picture())

    def test_02_title_txt(self):
        """检查 直击现场 标题是否正确"""
        news = NewsPage()
        self.assertEqual(1, news.title_txt())

    def test_03_content_txt(self):
        """检查 直接现场 描述文字 正确性"""
        news = NewsPage()
        self.assertEqual(1, news.content_txt())

    def test_04_picture_content(self):
        """检查 底部图片内容显示是否正常"""
        news = NewsPage()
        self.assertEqual(1, news.picture_content())


if __name__ == '__main__':
    unittest.main(verbosity=2)
