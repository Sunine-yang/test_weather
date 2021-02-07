import os
import unittest
import time

from common.HTMLTestRunner import HTMLTestRunner
from getpathInfo import report_Path
# from testcaseH5.test_testcase_02_Hourly import HourlyH5TestCase
# from testcaseH5.test_testcase_01_Today import TodayH5TestCase


class ExecuteSuite:

    # def allTests(self):
    #     suite = unittest.TestLoader().discover(  # 实例化测试套件
    #         start_dir=os.path.dirname(__file__),  # start_dir=该参数是discover()方法中的，后面的参数是需要批量执行的用例模块路径
    #         pattern='test_*.py',  # pattern=该参数是discover()方法中的，后面的参数是所有需要执行的用例前面是test_，后半部分用*号代替的.py文件
    #         top_level_dir=None)  # top_level_dir=该参数是discover()方法中的，固定格式：top_level_dir=None
    #     return suite  # 记住返回测试套件

    def suite_run(self):
        testsuite = unittest.TestSuite()
        # 将测试用例类，以类名的形式进行一个加载操作，生成一个加载好的测试用例类对象
        a = unittest.TestLoader().discover(  # 实例化测试套件
            start_dir=os.path.dirname(__file__),  # start_dir=该参数是discover()方法中的，后面的参数是需要批量执行的用例模块路径
            pattern='test_*.py',  # pattern=该参数是discover()方法中的，后面的参数是所有需要执行的用例前面是test_，后半部分用*号代替的.py文件
            top_level_dir=None)
        # 将加载好的测试用例类对象添加到测试套件中
        testsuite.addTest(test=a)
        # 创建一个可以获取当前日期的对象，格式是自定义的
        now = time.strftime("%Y-%m-%d_%H-%M-%S")
        # 创建报告文件，定义路径+当前时间+文件名
        log_file = report_Path() + now + "_hauweiH5_report.html"
        # 打开文件
        fp = open(log_file, 'w', encoding='utf-8')
        # 用第三方库HTMLTestRunner的run方法去执行这个测试套件
        runner = HTMLTestRunner(stream=fp, verbosity=2, title='最美天气---华为H5自动化测试报告')
        runner.run(testsuite)
        # 关闭文件
        fp.close()


if __name__ == '__main__':
    a = ExecuteSuite()
    a.suite_run()
