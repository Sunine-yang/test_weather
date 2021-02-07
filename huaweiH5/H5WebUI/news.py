import time

from log.Log import logger
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_driver import UtilWebDriver
from util.load_page import load_short_page
from util.regular_deal import last_long


class NewsPage(FindElement):
    def __init__(self):
        super(NewsPage, self).__init__()
        self.driver = UtilWebDriver.get_driver()
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/scene.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4&source=zm&oriId=P4')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/scene.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space=A1&orild=P4&source=zm&oriId=P4')
        self.driver.implicitly_wait(10)
        time.sleep(2)

    # 直击天气 现场 logo图片
    def title_picture(self):
        try:
            pic_url = self.get_attr('xpath', '//*[@id="page_container"]/div[4]/img', what='src')

            pic_conf = ConfRead.conf_return('weather_icon_src.conf')
            pic = pic_conf.get('news_picture', 'picture_url')
        except BaseException:
            print('直接现场获取logo URL失败！')
            logger.info('直接现场获取logo URL失败！')
        else:
            print(f'直接现场获取logo URL成功，url为：{pic_url}')
            logger.info(f'直接现场获取logo URL成功，url为：{pic_url}')
            if pic_url == pic:
                return 1
            else:
                return 2

    def title_txt(self):
        try:
            txt = self.get_text('xpath', '//*[@id="page_container"]/div[5]/h3')
        except BaseException:
            print('直击现场title失败！')
            logger.info('直击现场title失败！')
        else:
            print(f'直击现场title获取成功，title为：{txt}')
            logger.info(f'直击现场title获取成功，title为：{txt}')

            if txt == '直击天气现场':
                return 1
            else:
                return 2

    def content_txt(self):
        try:
            content = self.get_text('xpath', '//*[@id="page_container"]/div[5]/p')
        except BaseException:
            print('直击现场 描述 获取失败！')
            logger.info('直击现场 描述 获取失败！')
        else:
            print(f'content获取成功，content为：{content}')
            logger.info(f'content获取成功，content为：{content}')
            if content == '天气变幻莫测，忽而狂风骤雨，忽而晴空万里。最美天气带你一起走进天气现场，捕捉每日发生在地球上的天气现象，领略大自然的神奇。' \
                          '以下图片均来自网络，如有侵权请联系删除。':
                return 1
            else:
                return 2

    def picture_content(self):
        try:
            load_short_page()
            # .jpg
            p1_src = last_long(self.get_attr('xpath', '//*[@id="box"]/div[1]/div/a/img', what='src'), 4)
            p2_src = last_long(self.get_attr('xpath', '//*[@id="box"]/div[19]/div/a/img', what='src'), 4)
            p3_src = last_long(self.get_attr('xpath', '//*[@id="box"]/div[28]/div/a/img', what='src'), 4)

            # 市 区 县 .
            txt1 = last_long(self.get_text('xpath', '//*[@id="box"]/div[1]/div/div[1]'), 1)
            txt2 = last_long(self.get_text('xpath', '//*[@id="box"]/div[6]/div/div[1]'), 1)
            txt3 = last_long(self.get_text('xpath', '//*[@id="box"]/div[19]/div/div[1]'), 1)
        except BaseException:
            print('图片url和地址获取失败！')
            logger.info('图片url和地址获取失败！')
        else:
            print(f'图片url获取成功，src1:{p1_src},src2:{p2_src},src3:{p3_src},txt1:{txt1},txt2：{txt2},txt3:{txt3}')
            logger.info(f'图片url获取成功，src1:{p1_src},src2:{p2_src},src3:{p3_src},txt1:{txt1},txt2：{txt2},txt3:{txt3}')
            num = 0

            if p1_src == '.jpg' and p2_src == '.jpg' and p3_src == '.jpg':
                num = num + 1

            if txt1 == '市' or '区' or '县' or '.' and txt2 == '市' or '区' or '县' or '.' and txt3 == '市' or '区' or '县' or '.':
                num = num + 1

            if num == 2:
                return 1
            else:
                return 2

if __name__ == '__main__':
    a = NewsPage()
    print(a.picture_content())
