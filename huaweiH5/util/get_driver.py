import time
from selenium import webdriver


# webdriver 驱动
class UtilWebDriver:
    # 系统开辟了一块内存空间，将None存储了进去，紧接着driver指向了当前这块内存
    driver = None

    # 定义一个类的方法
    @classmethod
    # 创建type参数用于调整到底是用firefox还是chrome
    def get_driver(cls, type='Chrome'):

        mobileEmulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        options.add_experimental_option('mobileEmulation', mobileEmulation)

        # 判断一波，看到底准备用哪个浏览器
        if cls.driver is None:
            if type == 'Firefox':
                # 初始化一个firefox实例：driver
                # 系统开辟一块内存空间，将webdriver.Firefox()存储进去，现在类的属性driver将指向webdriver.Firefox()的内存地址
                cls.driver = webdriver.Firefox()
                cls.driver.implicitly_wait(10)
            else:
                # 如果想要使用Chrome，将type修改即可
                cls.driver = webdriver.Chrome(
                    executable_path=
                    "C:\\Program Files\\Google\\Chrome\\Application"
                    "\\chromedriver.exe",
                    chrome_options=options)
                cls.driver.implicitly_wait(10)
        # 浏览器窗口比例
        # cls.driver.set_window_size(375, 850)
        cls.driver.maximize_window()
        # 返回一个实例
        return cls.driver

    # 继续搞一个类方法
    @classmethod
    # 这个方法不需要sleep固定的时间，一旦找到了需要找的元素，就可以停止等待继续执行下面的东西
    def wait_element_present(cls, how, what, timeout=30):
        # 循环30次，这个for循环最后用了sleep(1)，所以基本上可以达到一个最长等待30秒的效果
        for i in range(timeout):
            try:
                # 用find_element找元素，参数how表示find_element_by哪种类型，what表示这种类型的值是什么
                element = cls.driver.find_element(
                    how, what)  # 可以自定义用什么方式来找这个元素，比较灵活
                # 找到了就返回这个element对象
                return element
            # 没找到就抛出异常
            except ValueError as e:  # 参数有问题
                print(e)
            # 同上抛出异常
            except Exception as ex:  # 方法有问题或者属性有问题
                print(ex)
            # 每次循环等一秒，循环多少次基本就是等了多少秒
            finally:
                time.sleep(1)
        # 返回None
        return None


# 类的方法，和对象的方法有什么不同，对象是如何进行实例化的
if __name__ == '__main__':
    UtilWebDriver.get_driver().get(
        'http://h5.zuimeitianqi.com/page/zh/today.html?cityId=0101250712&lan=zh-cn&partner=hw&space=A1&orild=P4&source=zm&oriId=P2'
    )
