# 基础页面,基本find_element功能工具
# 添加页面的基本功能
# find_element, input, type, get_txt, get_attribute


from selenium.webdriver.support.select import Select
from util.get_driver import UtilWebDriver
from selenium.webdriver.common.touch_actions import TouchActions


class FindElement:
    def __init__(self):
        self.driver = UtilWebDriver.get_driver()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, *locator, value):
        a = self.driver.find_element(*locator)
        a.clear()
        a.send_keys(value)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def get_attr(self, *locator, what):
        return self.driver.find_element(*locator).get_attribute(what)

    def get_pro(self, *locator):
        return self.driver.find_element(*locator).get_property()

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def select(self, *locator, value):
        Select(self.driver.find_element_by_xpath(*locator)).select_by_index(value)

    def alter_text(self):
        a = self.driver.switch_to_alert()
        assert_text = a.text
        a.accept()
        return assert_text

    def refresh_page(self):
        return self.driver.refresh()

    def select_by_text(self, *locator, value):
        Select(self.find_element(*locator)).select_by_visible_text(value)

    # xoffset    x轴偏移量
    # yoffset    y轴偏移量
    # speed      速度
    def flick_element(self, *locator, x, y, s):
        button = self.driver.find_element(*locator)
        Action = TouchActions(self.driver)
        Action.flick_element(button, x, y, s).perform()

    # 向下滑动为负数，向上滑动为正数
    def scroll_from_element(self, *locator, x, y):
        button = self.driver.find_element(*locator)
        Action = TouchActions(self.driver)
        Action.scroll_from_element(button, x, y).perform()

    def init_page(self, url):
        self.driver.get(url)


if __name__ == '__main__':
    pass
