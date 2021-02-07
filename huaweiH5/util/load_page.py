# 下拉页面
import time
from util.find_element import FindElement


def load_page(xpath, long):
    # 下拉页面
    find_element = FindElement()
    find_element.scroll_from_element('xpath',
                                     xpath,
                                     x=0,
                                     y=long)
    time.sleep(1)


def load_short_page():
    # 下拉页面
    find_element = FindElement()
    find_element.scroll_from_element('xpath',
                                     '//*[@id="page_container"]/div[5]/h3',
                                     x=0,
                                     y=1000)
    time.sleep(2)


def load_long_page():
    # 下拉页面
    find_element = FindElement()

    find_element.scroll_from_element('xpath',
                                     '//*[@id="float_fixed_advert"]/div/ul/li/a/img',
                                     x=0,
                                     y=4000)
    time.sleep(1)

