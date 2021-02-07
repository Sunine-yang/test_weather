import time
from datetime import datetime

from selenium.webdriver import ActionChains
from util.check_chinese import contain_chinese, contain_chinese_one
from util.conf_read import ConfRead
from util.find_element import FindElement
from log.Log import logger
from util.load_page import load_long_page, load_page
from util.regular_deal import baidu_get_jpeg, weatherol_get_jpg, get_tmp_num, last_long, \
    common_last_tmp, common_first_tmp, get_scenic_name, last_five


class Share(FindElement):
    def __init__(self):
        # 继承find element类
        super(Share, self).__init__()
        # 创建配置文件读取对象
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        self.driver.implicitly_wait(10)

    # 生活指南
    def living_guide(self):
        try:
            # 生活指南
            title = self.get_text('xpath', '//*[@id="living_guide"]/div[1]/div[1]')

            page_one = self.driver.find_elements_by_class_name('living_title')[0].get_attribute('textContent')

            page_two = self.driver.find_elements_by_class_name('living_title')[1].get_attribute('textContent')

            page_three = self.driver.find_elements_by_class_name('living_title')[2].get_attribute('textContent')

        except BaseException:
            print('生活指南模块元素获取失败！')
            logger.info('生活指南模块元素获取失败！')
        else:
            print(f'生活指南模块元素获取成功，滚动页面page1为：{page_one},page2为：{page_two},page3为：{page_three}')
            logger.info(f'生活指南模块元素获取成功，滚动页面page1为：{page_one},page2为：{page_two},page3为：{page_three}')

            live_list = ['穿衣指数', '运动指数', '感冒指数', '洗车指数', '钓鱼指数', '防晒指数']
            num = 0
            if page_one in live_list:
                num = num + 1
                live_list.remove(page_one)
                if page_two in live_list:
                    num = num + 1

                    live_list.remove(page_two)
                    if page_three in live_list:
                        num = num + 1
                    else:
                        return 2
                else:
                    return 2
            else:
                return 2

            if title == '生活指南':
                num = num + 1

            if num == 4:
                return 1
            else:
                return 2

    # 生活指南二级页面
    def living_guide_page_two(self, long):
        try:
            live_more = self.find_element('xpath', '//*[@id="living_guide"]/div[1]/div[2]')
            a = ActionChains(self.driver).move_to_element(live_more).click(live_more)
            load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', long)
            a.perform()
            time.sleep(2)
            page_two_title = self.get_text('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/span[1]')


        except BaseException:
            print("打开生活指南二级页面失败！")
            logger.info('打开生活指南二级页面失败！')

        else:
            print(f'打开生活指南二级页面成功，页面title：{page_two_title}')
            logger.info(f'打开生活指南二级页面成功，页面title：{page_two_title}')

            if page_two_title == '舒适度指数':

                time.sleep(2)
                return 1
            else:

                time.sleep(2)
                return 2

    # 生活资讯
    def operate_wrapper(self):
        try:
            # 生活资讯title
            livenews_title = self.get_text('xpath', '//*[@id="operate_wrapper"]/div[1]/div[1]')
            # jpeg@
            img_1 = baidu_get_jpeg(self.get_attr('xpath', '//*[@id="operate_list"]/ul/li[1]/a/img', what='src'))
            img_2 = baidu_get_jpeg(
                self.get_attr('xpath', '//*[@id="operate_list"]/ul/li[2]/a/div[2]/img', what='src'))
            img_3 = baidu_get_jpeg(
                self.get_attr('xpath', '//*[@id="operate_list"]/ul/li[3]/a/div[2]/img', what='src'))

            # 判断是否中文
            txt_1 = self.get_text('xpath', '//*[@id="operate_list"]/ul/li[1]/a/div/span')
            txt_2 = self.get_text('xpath', '//*[@id="operate_list"]/ul/li[2]/a/div[1]/h3')
            txt_3 = self.get_text('xpath', '//*[@id="operate_list"]/ul/li[3]/a/div[1]/h3')

        except BaseException:
            print('生活资讯信息流图片地址和文字获取失败！')
            logger.info('生活资讯信息流图片地址和文字获取失败！')
        else:
            print(
                f'生活资讯信息流图片地址和文字获取成功，title为：{livenews_title}。图1：{img_1},文字：{txt_1}---图1：{img_2},文字{txt_2}---图3：{img_3},文字{txt_3}')
            logger.info(
                f'生活资讯信息流图片地址和文字获取成功，title为：{livenews_title}。图1：{img_1},文字：{txt_1}---图1：{img_2},文字{txt_2}---图3：{img_3},文字{txt_3}')

            num = 0

            if img_1 == 'jpeg@' or '.png@':
                num = num + 1
            if img_2 == 'jpeg@' or '.png@':
                num = num + 1
            if img_3 == 'jpeg@' or '.png@':
                num = num + 1

            if contain_chinese_one(txt_1) == 1:
                num = num + 1
            if contain_chinese_one(txt_2) == 1:
                num = num + 1
            if contain_chinese_one(txt_3) == 1:
                num = num + 1

            if livenews_title == '生活资讯' or '摄影技巧':
                num = num + 1

            if num == 7:
                return 1
            else:
                return 2

    # 生活资讯 更多 页面
    def operate_wrapper_more(self, long):
        num = 0
        button = self.driver.find_element('xpath', '//*[@id="operate_wrapper"]/div[1]/div[2]/a')
        time.sleep(1)
        action = ActionChains(self.driver).move_to_element(button)
        action.perform()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', long)
        button.click()
        time.sleep(1)

        p1 = baidu_get_jpeg(
            self.get_attr('xpath', '//*[@id="weather_news_list"]/li[1]/a/img', what='src'))

        if p1 == 'jpeg@' or '.png@':
            num = num + 1
            print(f'图片 链接关键字显示为：{p1}')
            logger.info(f'图片 链接关键字显示为：{p1}')

        t1 = self.get_text('xpath', '//*[@id="weather_news_list"]/li[1]/a/h3')
        t1_check = contain_chinese_one(t1)

        if t1_check == 1:
            num = num + 1
            print(f'信息流title 显示为：{t1}')
            logger.info(f'信息流title 显示为：{t1}')

        if num == 2:
            return 1
        else:
            return 2

    # 天气快讯
    def reptile_news(self):
        try:
            # 天气快讯title
            reptilenews_title = self.get_text('xpath', '//*[@id="reptile_news"]/div[1]/div[1]')
            # .jpg
            img_1 = weatherol_get_jpg(
                self.get_attr('xpath', '//*[@id="reptile_news_list"]/ul/li[1]/a/img', what='src'))
            img_2 = weatherol_get_jpg(
                self.get_attr('xpath', '//*[@id="reptile_news_list"]/ul/li[2]/a/div[2]/img', what='src'))
            img_3 = baidu_get_jpeg(
                self.get_attr('xpath', '//*[@id="reptile_news_list"]/ul/li[3]/a/div[2]/img', what='src'))

            # 判断是否中文
            txt_1 = self.get_text('xpath', '//*[@id="reptile_news_list"]/ul/li[1]/a/div/span')
            txt_2 = self.get_text('xpath', '//*[@id="reptile_news_list"]/ul/li[2]/a/div[1]/h3')
            txt_3 = self.get_text('xpath', '//*[@id="reptile_news_list"]/ul/li[3]/a/div[1]/h3')

        except BaseException:
            print('天气快讯信息流图片地址和文字获取失败！')
            logger.info('天气快讯信息流图片地址和文字获取失败！')
        else:
            print(
                f'天气快讯信息流图片地址和文字获取成功，title为：{reptilenews_title}。图1：{img_1},文字：{txt_1}---图1：{img_2},文字{txt_2}---图3：{img_3},文字{txt_3}')
            logger.info(
                f'天气快讯信息流图片地址和文字获取成功，title为：{reptilenews_title}。图1：{img_1},文字：{txt_1}---图1：{img_2},文字{txt_2}---图3：{img_3},文字{txt_3}')

            num = 0

            if img_1 == '.jpg' or 'gg==':
                num = num + 1
            if img_2 == '.jpg' or '.png':
                num = num + 1
            if img_3 == 'jpeg@' or '.png@':
                num = num + 1

            if contain_chinese(txt_1) == 1:
                num = num + 1
            if contain_chinese(txt_2) == 1:
                num = num + 1
            if contain_chinese(txt_3) == 1:
                num = num + 1

            if reptilenews_title == '天气快讯':
                num = num + 1

            if num == 7:
                return 1
            else:
                return 2

    # 天气快讯 更多 页面
    def reptile_news_more(self, long):
        num = 0
        button = self.driver.find_element('xpath', '//*[@id="reptile_news"]/div[1]/div[2]/a')
        time.sleep(1)
        action = ActionChains(self.driver).move_to_element(button)
        action.perform()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', long)
        button.click()
        time.sleep(1)

        p1 = last_long(
            self.get_attr('xpath', '//*[@id="weather_news_list"]/li[1]/a/img', what='src'), 3)
        p2 = last_long(
            self.get_attr('xpath', '//*[@id="weather_news_list"]/li[4]/a/div[2]/img', what='src'), 3)

        if p1 and p2 == 'peg' or 'jpg':
            num = num + 1
            print(f'图片 链接关键字显示为：{p1},{p2}')
            logger.info(f'图片 链接关键字显示为：{p1},{p2}')

        t1 = self.get_text('xpath', '//*[@id="weather_news_list"]/li[4]/a/div[1]/h3')
        t1_check = contain_chinese(t1)
        t2 = self.get_text('xpath', '//*[@id="weather_news_list"]/li[6]/a/div[1]/h3')
        t2_check = contain_chinese(t2)

        if t1_check and t2_check == 1:
            num = num + 1
            print(f'信息流title 显示为：{t1},{t2}')
            logger.info(f'信息流title 显示为：{t1},{t2}')

        if num == 2:
            return 1
        else:
            return 2

    # 天气纵览
    def news_video(self):
        try:
            # 天气纵览title
            newsvideo_title = self.get_text('xpath', '//*[@id="news_video"]/div[1]/div[1]')
            # 视频截图一级页面展示
            img_1 = weatherol_get_jpg(self.get_attr('xpath', '//*[@id="news_video"]/div[2]/img[1]', what='src'))
            # 视频播放按钮图标展示
            img_2 = self.get_attr('xpath', '//*[@id="news_video"]/div[2]/img[2]', what='src')
        except BaseException:
            print('天气纵览信息流元素获取失败!')
            logger.info('天气纵览信息流元素获取失败!')
        else:
            print(f'天气纵览信息流元素获取成功,天气纵览title为：{newsvideo_title}，视频展示：{img_1},播放图标展示：{img_2}')
            logger.info(f'天气纵览信息流元素获取成功,天气纵览title为：{newsvideo_title}，视频展示：{img_1},播放图标展示：{img_2}')

            num = 0
            if img_1 == '.jpg' or 'gg==':
                num = num + 1
                print(1)
            if img_2 == 'http://s1.zuimeitianqi.com/page/dist/res/img/btn_play.svg':
                num = num + 1
                print(2)
            if newsvideo_title == '天气纵览':
                num = num + 1
                print(3)
            if num == 3:
                return 1
            else:
                return 2

    # 天气纵览 更多 页面
    def news_video_more(self, long):
        num = 0
        button = self.driver.find_element('xpath', '//*[@id="news_video"]/div[1]/div[2]/a')
        action = ActionChains(self.driver).move_to_element(button)
        time.sleep(1)
        action.perform()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', long)
        button.click()
        time.sleep(1)

        # 天气预报 字段
        txt1 = last_long(self.get_text('xpath', '//*[@id="weatherbroadcast"]'), 4)
        # 美女天气 字段
        txt2 = self.get_text('xpath', '/html/body/article/div[4]/span')
        if '天气预报' in txt1:
            num = num + 1
        if txt2 == '美女主播':
            num = num + 1

        if num == 2:
            return 1
        else:
            return 2

    # 猜你喜欢
    def weather_news(self):
        # try:
        load_long_page()

        # 猜你喜欢title
        weathernews_title = self.get_text('xpath', '//*[@id="info_title"]/div/div[1]')
        # 推荐
        tab_1 = self.get_text('xpath', '//*[@id="info_tab_wrap"]/li[1]')
        print(tab_1)
        # 财经
        tab_2 = self.get_text('xpath', '//*[@id="info_tab_wrap"]/li[7]')
        print(tab_2)
        # 第一个大图校验jpeg@
        big_img = baidu_get_jpeg(self.get_attr('xpath', '//*[@id="weather_news_list"]/li[1]/a/img', what='src'))
        # 第一个大图文字校验
        big_txt = contain_chinese(self.get_text('xpath', '//*[@id="weather_news_list"]/li[1]/a/h3'))
        print(big_img)
        print(big_txt)

        # 更多资讯
        more = self.get_text('xpath', '//*[@id="news_more_btn"]/a')
        print(more)
        print(f'猜你喜欢信息流元素获取成功，title为：{weathernews_title},推荐返回结果为：{tab_1}，财经返回结果为：{tab_2}，更多资讯实际显示{more}')
        logger.info(f'猜你喜欢信息流元素获取成功，title为：{weathernews_title},推荐实际显示{tab_1}，财经实际显示为{tab_2}，更多资讯实际显示{more}')
        num = 0
        if weathernews_title == '猜你喜欢':
            num = num + 1
            print(1)
        if tab_1 == '推荐':
            num = num + 1
            print(2)
        if tab_2 == '财经':
            num = num + 1
            print(3)
        if big_img == 'jpeg@' or '.png@':
            num = num + 1
            print(4)
        if big_txt == 1:
            num = num + 1
            print(5)
        if more == '更多资讯':
            num = num + 1
            print(6)

        # except BaseException:
        #     print('猜你喜欢信息流元素获取失败！')
        #     logger.info('猜你喜欢信息流元素获取失败！')
        # else:
        if num == 6:
            return 1
        else:
            return 2

    # 猜你喜欢 更多 页面
    def weather_news_more(self, long):
        num = 0
        # 猜你喜欢 更多
        self.refresh_page()
        button = self.driver.find_element('xpath', '//*[@id="weather_news"]/div/div/div[2]/a')

        action = ActionChains(self.driver).move_to_element(button)
        action.perform()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', long)

        button.click()
        time.sleep(1)

        p1 = baidu_get_jpeg(
            self.get_attr('xpath', '//*[@id="weather_news_list"]/li[1]/a/img', what='src'))

        if p1 == 'jpeg@' or '.png@':
            num = num + 1
            print(f'图片 链接关键字显示为：{p1}')
            logger.info(f'图片 链接关键字显示为：{p1}')

        t1 = contain_chinese(self.get_text('xpath', '//*[@id="weather_news_list"]/li[1]/a/h3'))

        if t1 == 1:
            num = num + 1
            print(f'信息流title 显示为：{t1}')
            logger.info(f'信息流title 显示为：{t1}')

        if num == 2:
            return 1
        else:
            return 2

    # 版权信息
    def copyright(self):
        try:
            # load_long_page()
            # 最美天气
            zuimei = self.get_text('xpath', '//*[@id="zuimei"]/div/a')
            # 隐私声明
            privacy = self.get_text('xpath', '//*[@id="privacy"]')

            # 版权所有

            cop = self.get_text('xpath', '//*[@id="right"]/a/span[1]')
            # ©2015-2020
            year = self.get_text('xpath', '//*[@id="right"]/a/span[2]')
            # 最美天气
            cop_zuimei = self.get_text('xpath', '//*[@id="right"]/a/span[3]')

        except BaseException:
            print('页面底部版权信息获取失败！')
            logger.info('页面底部版权信息获取失败！')

        else:
            print(f'页面底部版权信息获取成功，{zuimei},{privacy},{cop},{year},{cop_zuimei}')
            logger.info(f'页面底部版权信息获取成功，{zuimei},{privacy},{cop},{year},{cop_zuimei}')

            num = 0

            if zuimei == '最美天气':
                num = num + 1
            if privacy == '隐私声明':
                num = num + 1
            if cop == '版权所有':
                num = num + 1
            if year == '©2015-2021':
                num = num + 1
            if cop_zuimei == '最美天气':
                num = num + 1

            button = self.driver.find_element('xpath', '//*[@id="privacy"]')
            action = ActionChains(self.driver).move_to_element(button)
            action.perform()
            time.sleep(1)

            button.click()
            time.sleep(1)

            self.find_element('xpath', '//*[@class="container"]/ul/li[1]').click()
            time.sleep(1)
            # 隐私声明
            c_title = self.get_text('xpath', '//*[@class="container"]/div/h2')

            self.find_element('xpath', '//*[@class="container"]/ul/li[2]').click()
            time.sleep(1)
            # PRIVACY POLICY
            e_title = self.get_text('xpath', '//*[@class="container"]/div[2]/h2')

            if c_title == '隐私声明':
                num = num + 1
                print(c_title)
                logger.info(c_title)
            if e_title == 'PRIVACY POLICY':
                num = num + 1
                print(e_title)
                logger.info(e_title)

            if num == 7:

                return 1
            else:

                return 2

    # 周边景区
    def scenic(self):
        try:
            # 周边景区
            title = self.get_text('xpath', '//*[@id="scenic_box"]/div/div[1]')
            title_num = 0
            if title == '周边景区':
                print(f'周边景区title显示为：{title}')
                logger.info(f'周边景区title显示为：{title}')
                title_num = title_num + 1

            # A 景区等级，取单位A
            a1 = last_long(self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[1]/a/div/span[1]/em'), 1)
            a2 = last_long(self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[2]/a/div/span[1]/em'), 1)
            a3 = last_long(self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[3]/a/div/span[1]/em'), 1)

            A_num = 0
            if a1 and a2 and a3 == 'A':
                print(f'景区等级为，1：{a1},2:{a2},3:{a3}')
                logger.info(f'景区等级为，1：{a1},2:{a2},3:{a3}')
                A_num = A_num + 1

            # 天气 文字描述
            word1 = self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[1]/a/span[1]')
            w1 = contain_chinese_one(word1)

            word2 = self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[2]/a/span[1]')
            w2 = contain_chinese_one(word2)

            word3 = self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[3]/a/span[1]')
            w3 = contain_chinese_one(word3)

            word_num = 0

            if w1 and w2 and w3 == 1:
                print(f'天气为：{word1},{word2},{word3}')
                logger.info(f'天气为：{word1},{word2},{word3}')
                word_num = word_num + 1

            tmp1 = self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[1]/a/span[2]')
            tmp2 = self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[2]/a/span[2]')
            tmp3 = self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[3]/a/span[2]')

            last_tmp1 = common_last_tmp(tmp1)
            last_tmp2 = common_last_tmp(tmp2)
            last_tmp3 = common_last_tmp(tmp3)

            first_tmp1 = common_first_tmp(tmp1)
            first_tmp2 = common_first_tmp(tmp2)
            first_tmp3 = common_first_tmp(tmp3)

            tmp = last_tmp1 + last_tmp2 + last_tmp3 + first_tmp1 + first_tmp2 + first_tmp3
            tmp_num = 0
            # 数字为Ture
            if isinstance(tmp, int):
                print(f'温度总和为：{tmp}')
                logger.info(f'温度总和为：{tmp}')
                tmp_num = tmp_num + 1

            # 摄氏度符号
            symbol1 = last_long(tmp1, 1)
            symbol2 = last_long(tmp2, 1)
            symbol3 = last_long(tmp3, 1)
            symbol_num = 0
            if symbol1 == '℃' and symbol2 == '℃' and symbol3 == '℃':
                print(f'三个摄氏度：{symbol1},{symbol2},{symbol3}')
                logger.info(f'三个摄氏度：{symbol1},{symbol2},{symbol3}')
                symbol_num = symbol_num + 1

            num = title_num + A_num + word_num + tmp_num + symbol_num
            print(f'num为：{num}')

        except BaseException:
            print('周边景区元素获取失败！')
            logger.info('周边景区元素获取失败！')

        else:
            print(f'周边景区元素获取成功，title显示为：{title},天气显示为：{word1}，{word2},{word3}，温度显示为:{tmp1},{tmp2},{tmp3}')
            logger.info(f'周边景区元素获取成功，title显示为：{title},天气显示为：{word1}，{word2},{word3}，温度显示为:{tmp1},{tmp2},{tmp3}')
            if num == 5:
                return 1
            else:
                return 2

    # 周边景区 点击景点切换城市
    def scenic_click(self):
        try:

            button_txt = get_scenic_name(self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[2]/a/div/span[2]'))
            load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 800)
            time.sleep(1)
            self.click('xpath', '//*[@id="scenic_box"]/dl/dd[2]/a')
            time.sleep(2)
            title = self.driver.title
            # time.sleep(2)
            # city_name = get_scenic_name(self.get_text('xpath', '//*[@id="city_name"]/span'))

            # self.driver.back()
            # time.sleep(1)
            # self.driver.back()
        except BaseException:
            print('从周边景区点击切换城市失败！')

        else:
            print(f'从周边景区点击切换城市成功，周边景区城市名称：{button_txt}，页面title为:{title}')
            if button_txt in title:
                return 1
            else:
                return 2

    # 周边景区二级页面
    def scenic_page_two(self):
        try:
            button = self.driver.find_element('xpath', '//*[@id="scenic_rg_more"]')
            action = ActionChains(self.driver).move_to_element(button)
            time.sleep(1)
            action.perform()
            time.sleep(1)

            button.click()
            time.sleep(1)
            page_url = self.driver.current_url

            time.sleep(2)
            name_txt = self.get_text('xpath', '//*[@id="scenic_box"]/dl/dd[10]/a/div/span[2]')
            name_check = contain_chinese_one(name_txt)
            button = self.get_text('xpath', '//*[@id="scenic_more"]')
            hot = self.get_text('xpath', '//*[@id="travel_box"]/div/div')

            # 信息流文字
            content_txt1 = self.get_text('xpath', '//*[@id="travel_list"]/li[1]/a/div[2]')
            con1_check = contain_chinese(content_txt1)
            content_txt2 = self.get_text('xpath', '//*[@id="travel_list"]/li[8]/a/div[2]')
            con2_check = contain_chinese(content_txt2)

        except BaseException:
            print("打开周边景区二级页面失败！")


        else:
            print(f'打开周边景区二级页面成功，页面为url：{page_url},第十条景区为：{name_txt}，按钮显示为：{button}，'
                  f'旅游热点显示为：{hot},信息流1：{content_txt1},信息流2{content_txt2}')

            num = 0

            if name_check == 1:
                num = num + 1
                print(1)
            if button == '点击查看更多':
                num = num + 1
                print(2)
            if hot == '旅游热点':
                num = num + 1
                print(3)
            if con1_check == 1:
                num = num + 1
                print(4)

            if con2_check == 1:
                num = num + 1
                print(5)

            if num == 5:
                return 1
            else:
                return 2

    # 节日节气
    def fes_news(self):
        try:
            # 节日节气 title
            title = self.get_text('xpath', '//*[@id="fes_solar_terms_box"]/div[1]/div[1]')
            # .jpg
            img_1 = weatherol_get_jpg(
                self.get_attr('xpath', '//*[@id="fes_solar_ul"]/li[1]/a/img', what='src'))
            img_2 = weatherol_get_jpg(
                self.get_attr('xpath', '//*[@id="fes_solar_ul"]/li[2]/a/div[2]/img', what='src'))
            img_3 = baidu_get_jpeg(
                self.get_attr('xpath', '//*[@id="fes_solar_ul"]/li[3]/a/div[2]/img', what='src'))

            # 判断是否中文
            txt_1 = self.get_text('xpath', '//*[@id="fes_solar_ul"]/li[1]/a/div/span')
            txt_2 = self.get_text('xpath', '//*[@id="fes_solar_ul"]/li[2]/a/div[1]/h3')
            txt_3 = self.get_text('xpath', '//*[@id="fes_solar_ul"]/li[3]/a/div[1]/h3')

        except BaseException:
            print('节日节气信息流图片地址和文字获取失败！')
            logger.info('节日节气信息流图片地址和文字获取失败！')
        else:
            print(
                f'节日节气信息流图片地址和文字获取成功，title为：{title}。图1：{img_1},文字：{txt_1}---图1：{img_2},文字{txt_2}---图3：{img_3},文字{txt_3}')
            logger.info(
                f'节日节气信息流图片地址和文字获取成功，title为：{title}。图1：{img_1},文字：{txt_1}---图1：{img_2},文字{txt_2}---图3：{img_3},文字{txt_3}')

            num = 0

            if img_1 == '.jpg' or 'gg==':
                num = num + 1
            if img_2 == '.jpg' or '.png' or 'gg==':
                num = num + 1
            if img_3 == 'jpeg@' or '.png@' or 'gg==':
                num = num + 1

            if contain_chinese(txt_1) == 1:
                num = num + 1
            if contain_chinese(txt_2) == 1:
                num = num + 1
            if contain_chinese(txt_3) == 1:
                num = num + 1

            if title == '节日节气':
                num = num + 1

            if num == 7:
                return 1
            else:
                return 2

    # 节日节气 更多 页面
    def fes_news_more(self):
        try:
            num = 0
            button = self.driver.find_element('xpath', '//*[@id="fes_more"]')
            time.sleep(1)
            action = ActionChains(self.driver).move_to_element(button)
            action.perform()
            time.sleep(1)

            button.click()
            time.sleep(1)

            p1 = last_long(
                self.get_attr('xpath', '//*[@id="weather_news_list"]/li[1]/a/div[2]/img', what='src'), 3)
            p2 = last_long(
                self.get_attr('xpath', '//*[@id="weather_news_list"]/li[7]/a/div[2]/img', what='src'), 3)

            if p1 and p2 == 'peg' or 'jpg':
                num = num + 1
                print(f'图片 链接关键字显示为：{p1},{p2}')
                logger.info(f'图片 链接关键字显示为：{p1},{p2}')

            t1 = self.get_text('xpath', '//*[@id="weather_news_list"]/li[2]/a/div[1]/h3')
            t1_check = contain_chinese(t1)
            t2 = self.get_text('xpath', '//*[@id="weather_news_list"]/li[5]/a/div[1]/h3')
            t2_check = contain_chinese(t2)

            if t1_check and t2_check == 1:
                num = num + 1
                print(f'信息流title 显示为：{t1},{t2}')
                logger.info(f'信息流title 显示为：{t1},{t2}')
        except BaseException:
            print('节日节气更多页面 元素获取失败！')
            logger.info('节日节气更多页面 元素获取失败！')
        else:
            if num == 2:
                return 1
            else:
                return 2

    # 图集二级页面 被调用
    def pic_page(self, pic, title_name):
        try:
            num = 0
            p_url = self.get_attr('xpath', '//*[@id="page_container"]/div[2]/img', what='src')
            title = self.get_text('xpath', '//*[@id="page_container"]/div[3]/h3')
            pic_conf = ConfRead.conf_return('weather_icon_src.conf')
            p_txt_conf = ConfRead.conf_return('pic_.conf')
            p_conf = pic_conf.get('news_picture', pic)
            p_txt = p_txt_conf.get('pic_text', pic)
            txt = self.get_text('xpath', '//*[@id="page_container"]/div[3]/p')

            print(title)
            print(txt)
            load_page('//*[@id="page_container"]/div[3]/h3', 1000)

            # .jpg
            p1_src = self.get_attr('xpath', '//*[@id="box"]/div[1]/div/a/img', what='src')
            p2_src = self.get_attr('xpath', '//*[@id="box"]/div[5]/div/a/img', what='src')
            p3_src = self.get_attr('xpath', '//*[@id="box"]/div[7]/div/a/img', what='src')

            # 省 市 区 县
            txt1 = self.get_text('xpath', '//*[@id="box"]/div[2]/div/div[1]')
            txt2 = self.get_text('xpath', '//*[@id="box"]/div[6]/div/div[1]')
            txt3 = self.get_text('xpath', '//*[@id="box"]/div[9]/div/div[1]')

            if title == title_name:
                num += 1
                print(100)
            if p_url == p_conf:
                num += 1
                print(200)
            if '.jpg' or '.png' in p1_src and p2_src and p3_src:
                num += 1
                print(300)
            if '省' or '市' or '区' or '县' in txt1 and txt2 and txt3:
                num += 1
                print(400)
            if txt == p_txt:
                num += 1
                print(500)
        except BaseException:
            print('图集二级页面 元素获取失败！')
            logger.info('图集二级页面 元素获取失败！')
        else:
            if num == 5:
                return 1
            else:
                return 2

    # 图集专题
    def pic(self):
        try:
            # 图集专题
            title = self.get_text('xpath', '//*[@id="pic_topic"]/div[1]/div[1]')
            print(title)
            # 四张图
            p1 = self.get_attr('xpath', '//*[@id="pic_topic_list"]/ul/li[1]/a/img', what='src')

            p2 = self.get_attr('xpath', '//*[@id="pic_topic_list"]/ul/li[2]/a/img', what='src')

            p3 = self.get_attr('xpath', '//*[@id="pic_topic_list"]/ul/li[3]/a/img', what='src')

            p4 = self.get_attr('xpath', '//*[@id="pic_topic_list"]/ul/li[4]/a/img', what='src')

            num = 0
            if last_long(p1, 3) and last_long(p2, 3) and last_long(p3, 3) and last_long(p4, 3) == 'jpg' or 'png':
                num += 1
                print(1)
            if title == '图集专题':
                num += 1
                print(2)
            # 第一个元素与其他三个不同，单独写
            load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 1200)
            self.click('xpath', '//*[@id="pic_topic_list"]/ul/li[1]/a')
            time.sleep(1)
            pic = self.get_attr('xpath', '//*[@id="page_container"]/div[4]/img', what='src')
            name = self.get_text('xpath', '//*[@id="page_container"]/div[5]/h3')
            txt = self.get_text('xpath', '//*[@id="page_container"]/div[5]/p')
            t1 = self.get_text('xpath', '//*[@id="box"]/div[3]/div/div[1]')
            t2 = self.get_text('xpath', '//*[@id="box"]/div[6]/div/div[1]')
            p1 = self.get_attr('xpath', '//*[@id="box"]/div[2]/div/a/img', what='src')
            p2 = self.get_attr('xpath', '//*[@id="box"]/div[4]/div/a/img', what='src')
            if pic == 'https://update.zuimeitianqi.com/2001/weafile/group/pic/20200422/1587537645685.jpg' and name == '直击天气现场' and \
                    txt == '天气变幻莫测，忽而狂风骤雨，忽而晴空万里。最美天气带你一起走进天气现场，捕捉每日发生在地球上的天气现象，领略大自然的神奇。以下图片均来自网络，如有侵权请联系删除。' and \
                    '省' or '市' or '区' or '县' in t1 and t2 and \
                    '.jpg' or '.png' in p1 and p2:
                num += 1
                print(3)
            self.driver.back()
            time.sleep(1)

            self.driver.refresh()
            time.sleep(3)

            self.click('xpath', '//*[@id="pic_topic_list"]/ul/li[2]/a')
            time.sleep(1)
            if self.pic_page('two', '生活日记') == 1:
                num += 1
                print(4)
            self.driver.back()
            time.sleep(1)

            self.driver.refresh()
            time.sleep(3)

            self.click('xpath', '//*[@id="pic_topic_list"]/ul/li[3]/a')
            time.sleep(1)
            if self.pic_page('three', '冬日里的暖色调') == 1:
                num += 1
                print(5)
            self.driver.back()
            time.sleep(1)

            self.driver.refresh()
            time.sleep(3)

            self.click('xpath', '//*[@id="pic_topic_list"]/ul/li[4]/a')
            time.sleep(1)
            if self.pic_page('four', '冬季随拍') == 1:
                num += 1
                print(6)
        except BaseException:
            print('图集专题 模块 元素获取失败!')
            logger.info('图集专题 模块 元素获取失败!')
        else:
            if num == 6:
                return 1
            else:
                return 2

    # 图集专题 更多 页面
    def pic_more(self):
        try:
            num = 0
            button = self.driver.find_element('xpath', '//*[@id="topic_more"]')
            time.sleep(1)
            action = ActionChains(self.driver).move_to_element(button)
            action.perform()
            time.sleep(1)

            button.click()
            time.sleep(1)

            # jpg or png
            p2 = self.get_attr('xpath', '//*[@id="topics_box"]/ul/li[2]/a/img', what='src')
            print(p2)
            logger.info(p2)
            p18 = self.get_attr('xpath', '//*[@id="topics_box"]/ul/li[18]/a/img', what='src')
            print(p18)
            logger.info(p18)
            p34 = self.get_attr('xpath', '//*[@id="topics_box"]/ul/li[34]/a/img', what='src')
            print(p34)
            logger.info(p34)

            if '.jpg' or '.png' in p2 and p18 and p34:
                num += 1
                print(1)
            self.click('xpath', '//*[@id="topics_box"]/ul/li[2]/a')
            time.sleep(1)

            print(self.get_text('xpath', '//*[@id="page_container"]/div[3]/h3'))
            if contain_chinese_one(self.get_text('xpath', '//*[@id="page_container"]/div[3]/h3')) == 1:
                num += 1
                print(2)
            print(self.get_text('xpath', '//*[@id="page_container"]/div[3]/p'))
            if contain_chinese(self.get_text('xpath', '//*[@id="page_container"]/div[3]/p')) == 1:
                num += 1
                print(3)
            if '.jpg' or '.png' in self.get_text('xpath', '//*[@id="box"]/div[3]/div/a/img'):
                num += 1
                print(4)
            if '省' or '市' or '区' or '县' in self.get_text('xpath', '//*[@id="box"]/div[2]/div/div[1]'):
                num += 1
                print(5)
            self.driver.back()
            time.sleep(1)
            self.click('xpath', '//*[@id="topics_box"]/ul/li[18]/a')
            time.sleep(1)

            print(self.get_text('xpath', '//*[@id="page_container"]/div[3]/h3'))
            if contain_chinese_one(self.get_text('xpath', '//*[@id="page_container"]/div[3]/h3')) == 1:
                num += 1
                print(6)
            print(self.get_text('xpath', '//*[@id="page_container"]/div[3]/p'))
            if contain_chinese(self.get_text('xpath', '//*[@id="page_container"]/div[3]/p')) == 1:
                num += 1
                print(7)
            if '.jpg' or '.png' in self.get_text('xpath', '//*[@id="box"]/div[3]/div/a/img'):
                num += 1
                print(8)
            if '省' or '市' or '区' or '县' in self.get_text('xpath', '//*[@id="box"]/div[2]/div/div[1]'):
                num += 1
                print(9)
            self.driver.back()
            time.sleep(1)
            self.click('xpath', '//*[@id="topics_box"]/ul/li[34]/a')
            time.sleep(1)

            print(self.get_text('xpath', '//*[@id="page_container"]/div[3]/h3'))
            if contain_chinese_one(self.get_text('xpath', '//*[@id="page_container"]/div[3]/h3')) == 1:
                num += 1
                print(10)
            print(self.get_text('xpath', '//*[@id="page_container"]/div[3]/p'))
            if contain_chinese(self.get_text('xpath', '//*[@id="page_container"]/div[3]/p')) == 1:
                num += 1
                print(11)
            if '.jpg' or '.png' in self.get_text('xpath', '//*[@id="box"]/div[3]/div/a/img'):
                num += 1
                print(12)
            if '省' or '市' or '区' or '县' in self.get_text('xpath', '//*[@id="box"]/div[2]/div/div[1]'):
                num += 1
                print(13)
        except BaseException:
            print('图集专题 更多 页面')
            logger.info('图集专题 更多 页面')
        else:
            if num == 13:
                return 1
            else:
                return 2

    # # 判断顶部横幅是否显示正常
    # def warn_top(self, warn):
    #     if warn == '':
    #         print('当前城市当前时间没有天气预警信息')
    #         logger.info('当前城市当前时间没有天气预警信息')
    #         return 1
    #     else:
    #         try:
    #             warn_contentself = self.get_text('xpath', '//*[@id="warn_content"]')
    #         except BaseException:
    #             print('没有找到顶部预警条状横幅！')
    #             logger.info('没有找到顶部预警条状横幅！')
    #             return 2
    #         else:
    #             print(f'顶部条状横幅显示正常，内容为：{warn_contentself}')
    #             logger.info(f'顶部条状横幅显示正常，内容为：{warn_contentself}')
    #             return 1

    # 需要在实况页面找的元素
    def today_data(self):
        try:
            self.driver.implicitly_wait(10)
            self.driver.get(
                f'http://h5.zuimeitianqi.com/page/zh/today.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
                '=A1&orild=P4&source=zm&oriId=P2')

            time.sleep(2)
            # 天气文字描述
            wea_txt = self.get_text('xpath', '//*[@id="wea_txt"]')

            # 实况当前温度
            tmp = int(self.get_text('xpath', '//*[@id="tmp"]'))

            # 天气预警信息
            warn = self.get_text('xpath', '//*[@id="warn_info"]')

            # 最低最高温度
            tmp1 = self.get_text('xpath', '//*[@id="tmp_section"]/span[1]')
            # 最高温度
            max_tmp = int(get_tmp_num(tmp1))
            tmp2 = self.get_text('xpath', '//*[@id="tmp_section"]/span[2]')
            # 最低温度
            min_tmp = int(get_tmp_num(tmp2))

        except BaseException:
            print('打开实况页面获取其他页面要用的元素失败！')
            logger.info('打开实况页面获取其他页面要用的元素失败！')

        else:

            data = [wea_txt, tmp, warn, max_tmp, min_tmp]
            self.driver.back()
            # self.driver.close()
            return data

    def little_game(self):
        # 小游戏中心 和 更多
        title = self.get_text('xpath', '//*[@id="game"]/div/div[1]')
        # 第一个
        one = self.get_attr('xpath', '//*[@id="game_list_item"]/li[1]/a/img', what='src')
        # 第四个
        four = self.get_attr('xpath', '//*[@id="game_list_item"]/li[4]/a/img', what='src')

        # 更多
        button = self.driver.find_element('xpath', '//*[@id="game"]/div/div[2]/a')
        time.sleep(1)
        action = ActionChains(self.driver).move_to_element(button)
        action.perform()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 100)

        button.click()
        time.sleep(1)

        txt = self.get_text('xpath',
                            '//*[@id="app"]/div/div/div[1]/div/div/div[2]/div/ul/li[1]/div/ul/li[2]/a/div/div[1]')
        toptxt = self.get_text('xpath', '//*[@id="app"]/div/div/div[2]/div/div/ul/li[4]')

        num = 0
        if title == '小游戏中心':
            num += 1
            print(1)
        if last_long(one, 3) == 'png':
            num += 1
            print(2)
        if last_long(four, 3) == 'png':
            num += 1
            print(3)
        if contain_chinese_one(txt) == 1:
            num += 1
            print(4)
        if contain_chinese_one(toptxt) == 1:
            num += 1
            print(5)
        if num == 5:
            return 1
        else:
            return 2

    # 日出日落
    def sun(self):

        try:
            # 日出时间
            sun_start = last_five(self.get_text('xpath', '//*[@id="sun_box"]/dl[1]/dd[1]/span[2]'))
            # 日落时间
            sun_finish = last_five(self.get_text('xpath', '//*[@id="sun_box"]/dl[1]/dd[2]/span[2]'))

            # 月出时间
            moon_start = last_five(self.get_text('xpath', '//*[@id="sun_box"]/dl[2]/dd[1]/span[2]'))
            # 月落时间
            moon_finish = last_five(self.get_text('xpath', '//*[@id="sun_box"]/dl[2]/dd[2]/span[2]'))

            # 日出 字段
            sun_up_txt = self.get_text('xpath', '//*[@id="sun_box"]/dl[1]/dd[1]/span[1]')
            # 日落 字段
            sun_down_txt = self.get_text('xpath', '//*[@id="sun_box"]/dl[1]/dd[2]/span[1]')

            # 月出 字段
            moon_up_txt = self.get_text('xpath', '//*[@id="sun_box"]/dl[2]/dd[1]/span[1]')
            # 月落 字段
            moon_down_txt = self.get_text('xpath', '//*[@id="sun_box"]/dl[2]/dd[2]/span[1]')

            # 转换为时间格式 - 日出 日落 月出 月落
            sun_start_time = datetime.strptime(sun_start, '%H:%M')
            sun_finish_time = datetime.strptime(sun_finish, '%H:%M')
            moon_start_time = datetime.strptime(moon_start, '%H:%M')
            moon_finish_time = datetime.strptime(moon_finish, '%H:%M')

            # 日落没 +1  都是当天出来当天下去 但是，南极应该+1，但是太极端了，算了算了不管了

            # 月落 +1
            moon_after_day = self.get_text('xpath', '//*[@id="sun_box"]/dl[2]/dd[2]/span[3]')
            # 月出 -1
            moon_before_day = self.get_text('xpath', '//*[@id="sun_box"]/dl[2]/dd[1]/span[3]')
        except BaseException:
            print('获取日出日落内元素失败！')
            logger.info('获取日出日落内元素失败！')
        else:
            print('获取日出日落内元素成功！')
            logger.info('获取日出日落内元素成功！')
            print(f'日出时间为：{sun_start_time},日落时间为：{sun_finish_time}')
            logger.info(f'日出时间为：{sun_start_time},日落时间为：{sun_finish_time}')
            print(f'月出时间为：{moon_start_time},月落时间为：{moon_finish_time}')
            logger.info(f'月出时间为：{moon_start_time},月落时间为：{moon_finish_time}')
            print(f'日出日落和月出月落字段显示为：{sun_up_txt}，{moon_up_txt},{sun_down_txt},{moon_down_txt}')
            logger.info(f'日出日落和月出月落字段显示为：{sun_up_txt}，{moon_up_txt},{sun_down_txt},{moon_down_txt}')

            num = 0

            if sun_start_time < sun_finish_time:
                num = num + 1
            if moon_after_day == '+1' or moon_before_day == '-1':
                num = num + 1
            else:
                if moon_start_time < moon_finish_time:
                    num = num + 1

            if sun_up_txt == '日出' and sun_down_txt == '日落':
                num = num + 1
            if moon_up_txt == '月出' and moon_down_txt == '月落':
                num = num + 1
            if num == 4:
                return 1
            else:
                return 2

    # 日出日落二级页面
    def sun_page_two(self):
        try:
            # 日出日落元素框，点击跳转
            self.click('xpath', '//*[@id="sun_box"]/dl[1]')
            time.sleep(2)
            # 获取跳转后的网址
            page_url = self.driver.current_url
        except BaseException:
            print('日出日落跳转页面失败！')
            logger.info('日出日落跳转页面失败！')
        else:
            print(f'日出日落跳转页面跳转成功,跳转后网址为：{page_url}')
            logger.info(f'日出日落跳转页面跳转成功,跳转后网址为：{page_url}')
            if 'sun' in page_url:
                time.sleep(2)
                return 1
            else:
                time.sleep(2)
                return 2


if __name__ == '__main__':
    print(Share().operate_wrapper())
