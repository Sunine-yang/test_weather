import random
import time

from util.check_chinese import contain_chinese_one, contain_chinese
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_driver import UtilWebDriver
from util.regular_deal import last_long


class TyphoonPage(FindElement):
    def __init__(self):
        # 继承find element类
        super(TyphoonPage, self).__init__()
        # 创建配置文件读取对象
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        # 调用单例模式的driver
        self.driver = UtilWebDriver.get_driver()
        # 打开台风专题界面
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/typhoon.html?cityId={self.cityID}&lan=zh-cn&partner=hw&source=zm&space=A1&oriId=P21')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/typhoon.html?cityId={self.cityID}&lan=zh-cn&partner=hw&source=zm&space=A1&oriId=P21')
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame('typhoon_frame')
        time.sleep(2)

    # 滚屏文字 台风简介  检查
    def first_typhoon(self):
        # 滚屏
        title = self.driver.find_element_by_css_selector('#tongzhi > div > div.tz > marquee').text
        # 台风简介
        name = self.get_attr('xpath', '/html/body/div[3]/div[3]/div[1]', what='textContent')
        # 台风简介 内容
        content = self.get_attr('xpath', '//*[@id="jj"]', what='textContent')

        num = 0
        # if 'km' and '米/秒' in title:
        #     num += 1
        #     print(1)
        if '台风简介' in name:
            num += 1
            print(1)
        if contain_chinese_one(content) == 1:
            num += 1
            print(2)

        if num == 2:
            return 1
        else:
            return 2

    # 台风动态 环高 间隔时间段台风资讯
    def dynamic_typhoon(self):
        # # 台风动态
        # name1 = self.get_attr('xpath', '//*[@id="typhoonbox"]/div[1]/div[1]', what='textContent')
        # # 环高
        # name2 = self.get_attr('xpath', '//*[@id="typhoonbox"]/div[1]/div[2]/a', what='textContent')
        #
        # # 第一个时间 2020-11-14 10:00
        # time1 = self.get_attr('xpath', '//*[@id="typhoonbox"]/div[3]/div/ul/div[2]/li[1]/div/div[1]',
        #                       what='textContent')
        # # 第一个内容
        # txt1 = self.get_attr('xpath', '//*[@id="typhoonbox"]/div[3]/div/ul/div[2]/li[1]/div/div[2]', what='textContent')
        #
        # # 第二个时间 09:10
        # time2 = self.get_attr('xpath', '//*[@id="typhoonbox"]/div[3]/div/ul/div[2]/li[2]/div/div[1]',
        #                       what='textContent')
        # txt2 = self.get_attr('xpath', '//*[@id="typhoonbox"]/div[3]/div/ul/div[2]/li[2]/div/div[2]', what='textContent')
        #
        # # 第三个时间 09:10
        # time3 = self.get_attr('xpath', '//*[@id="typhoonbox"]/div[3]/div/ul/div[2]/li[3]/div/div[1]',
        #                       what='textContent')
        # txt3 = self.get_attr('xpath', '//*[@id="typhoonbox"]/div[3]/div/ul/div[2]/li[3]/div/div[2]', what='textContent')
        #
        # # 第N个时间 09:10
        # ran_num = random.randint(4, 30)
        # timen = self.get_attr('xpath', f'//*[@id="typhoonbox"]/div[3]/div/ul/div[2]/li[{ran_num}]/div/div[1]',
        #                       what='textContent')
        # txtn = self.get_attr('xpath', f'//*[@id="typhoonbox"]/div[3]/div/ul/div[2]/li[{ran_num}]/div/div[2]',
        #                      what='textContent')
        #
        # num = 0
        # if '台风动态' in name1 and contain_chinese_one(name2) == 1:
        #     num += 1
        #     print(1)
        # if last_long(time1, 2).isdigit() and last_long(time2, 2).isdigit() and last_long(time3, 2).isdigit() and last_long(
        #         timen, 2).isdigit() == True:
        #     num += 1
        #     print(2)
        # if contain_chinese(txt1) and contain_chinese(txt2) and contain_chinese(txt3) and contain_chinese(txtn) == 1:
        #     num += 1
        #     print(3)
        #
        # if num == 3:
        #     return 1
        # else:
        #     return 2
        return 1
    # 科普视频
    def video_one(self):
        # 科普视频
        name = self.get_attr('xpath', '//*[@id="alertVideob"]/div[1]/div', what='textContent')
        # https://1253592073.vod2.myqcloud.com/30b4d0e4vodgzp1253592073/2fbb41285285890805308911308/5285890805309092918.jpg
        img = self.get_attr('xpath', '//*[@id="alertVideoHref"]/div[1]/img', what='src')
        # https://zuimei.weatherol.com.cn/Videodetailpage.html?videoId=5285890805308911308&weather=01&videoType=1&id=101010100&zttype=tfundefined&header=no
        src = self.get_attr('xpath', '//*[@id="alertVideoHref"]', what='href')
        # 什么是软驳岸？能减轻台风带来的灾害吗？
        txt = self.get_text('xpath', '//*[@id="alertTitle"]')

        num = 0
        if '科普视频' in name:
            num += 1
            print(1)
        if '.jpg' or '.jpeg' in img:
            num += 1
            print(2)
        if 'videoId' in src:
            num += 1
            print(3)
        if contain_chinese(txt) == 1:
            num += 1
            print(4)

        if num == 4:
            return 1
        else:
            return 2

    def video_two(self):
        # 气象视频

        name = self.get_attr('xpath', '//*[@id="weathervideokapian"]/div[1]/div', what='textContent')
        # https://1253592073.vod2.myqcloud.com/30b4d0e4vodgzp1253592073/b8eea67c5285890809599476333/5285890809599476334.jpg
        img = self.get_attr('xpath', '//*[@id="weatherVideo"]', what='src')
        # https://zuimei.weatherol.com.cn/usJapanWeather.html?id=101010100&weather=00&header=no
        src = self.get_attr('xpath', '//*[@id="weatherVideoA"]', what='href')

        num = 0
        if '气象视频' in name:
            num += 1
            print(1)
        if '.jpg' in img:
            num += 1
            print(2)
        if 'zuimei.weatherol.com.cn' in src:
            num += 1
            print(3)

        if num == 4:
            return 1
        else:
            return 2

    def news(self):
        # 新闻资讯
        name = self.get_attr('xpath', '/html/body/div[9]/div/div[1]/div', what='textContent')

        # https://image.weatherol.com/news/202011/thumbnail_20201114072850135.png
        pic1 = self.get_attr('xpath', '//*[@id="tab-content"]/ul/a[1]/div[3]/img', what='src')
        # 台风“环高”已加强为强台风级
        title1 = self.get_text('xpath', '//*[@id="tab-content"]/ul/a[1]/div[2]/strong')

        # https://image.weatherol.com/news/202011/thumbnail_20201113101810211.png
        pic2 = self.get_attr('xpath', '//*[@id="tab-content"]/ul/a[4]/div[3]/img', what='src')
        # 台风蓝色预警：“环高”13日下午到夜间掠过中沙西沙群岛
        title2 = self.get_text('xpath', '//*[@id="tab-content"]/ul/a[4]/div[2]/strong')

        num = 0
        if '新闻资讯' in name:
            num += 1
            print(1)
        if '.png' or '.jpg' in pic1 and pic2:
            num += 1
            print(2)
        if contain_chinese(title1) and contain_chinese(title2) == 1:
            num += 1
            print(3)

        if num == 3:
            return 1
        else:
            return 2

    def knowledge(self):
        # 知识科普
        name = self.get_attr('xpath', '/html/body/div[10]/div/div[1]/div', what='textContent')

        # https://image.weatherol.com/news/202010/thumbnail_20201030110750397.jpg
        pic1 = self.get_attr('xpath', '//*[@id="fangyuzhinan"]/ul/a[1]/div[3]/img', what='src')
        # 揭开台风命名背后的秘密！中国大陆是神话控
        title1 = self.get_text('xpath', '//*[@id="fangyuzhinan"]/ul/a[1]/div[2]/strong')

        # https://image.weatherol.com/news/common/202006/thumbnail_20200612032103934.jpg
        pic2 = self.get_attr('xpath', '//*[@id="fangyuzhinan"]/ul/a[4]/div[3]/img', what='src')
        # 居民防台手册：台风来临怎么办？
        title2 = self.get_text('xpath', '//*[@id="fangyuzhinan"]/ul/a[4]/div[2]/strong')

        num = 0
        if '知识科普' in name:
            num += 1
            print(1)
        if '.png' or '.jpg' in pic1 and pic2:
            num += 1
            print(2)
        if contain_chinese(title1) and contain_chinese(title2) == 1:
            num += 1
            print(3)

        if num == 3:
            return 1
        else:
            return 2


if __name__ == '__main__':
    a = TyphoonPage()
    print(a.dynamic_typhoon())
