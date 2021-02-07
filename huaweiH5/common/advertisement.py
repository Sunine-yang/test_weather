import time
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_driver import UtilWebDriver


class Advertisement(FindElement):
    def __init__(self):
        # 继承find element类
        super(Advertisement, self).__init__()
        self.driver = UtilWebDriver.get_driver()
        # 创建配置文件读取对象
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/today.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
            '=A1&orild=P4&source=zm&oriId=P2')
        time.sleep(2)
        self.driver.implicitly_wait(10)

    def advertisement_page(self):
        self.driver.switch_to.frame(self.find_element('xpath', '//*[@id="top_js_list"]/div/div/iframe'))
        pic = self.get_attr('xpath', '//*[@id="img_0_1"]', what='src')
        print(pic)

if __name__ == '__main__':
    a = Advertisement()
    a.advertisement_page()