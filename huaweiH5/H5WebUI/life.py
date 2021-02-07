import datetime
import time
from common.common_page import Share
from util.check_chinese import contain_chinese_one
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_driver import UtilWebDriver
from log.Log import logger
from util.load_page import load_page
from util.regular_deal import last_long


class LifePage(FindElement):
    def __init__(self):
        # 继承find element类
        super(LifePage, self).__init__()
        # 创建配置文件读取对象
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        # 调用单例模式的driver
        self.driver = UtilWebDriver.get_driver()
        # 打开life界面
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/comfor.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
            '=A1&orild=P4&source=zm&oriId=P2')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/comfor.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
            '=A1&orild=P4&source=zm&oriId=P2')
        self.driver.implicitly_wait(10)
        time.sleep(2)

    # 生活指数 主卡片
    def life_card(self):
        # 今天
        today = self.get_attr('xpath', '//*[@id="index_tab"]/li[1]/span[1]', what='textContent')
        date1 = self.get_attr('xpath', '//*[@id="index_tab"]/li[1]/span[2]', what='textContent')
        # 明天
        tomorrow = self.get_attr('xpath', '//*[@id="index_tab"]/li[2]/span[1]', what='textContent')
        date2 = self.get_attr('xpath', '//*[@id="index_tab"]/li[2]/span[2]', what='textContent')
        # 后天
        tomorrowtomorrow = self.get_attr('xpath', '//*[@id="index_tab"]/li[3]/span[1]', what='textContent')
        date3 = self.get_attr('xpath', '//*[@id="index_tab"]/li[3]/span[2]', what='textContent')

        real_date1 = datetime.datetime.now().strftime('%m/%d')
        real_date2 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%m/%d')
        real_date3 = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime('%m/%d')
        print(today + ':' + date1)
        print(tomorrow + ':' + date2)
        print(tomorrowtomorrow + ':' + date3)
        # 日期 2
        date_num = 0
        if today == '今天' and tomorrow == '明天' and tomorrowtomorrow == '后天':
            date_num += 1
        if date1 == real_date1 and date2 == real_date2 and date3 == real_date3:
            date_num += 1

        # 三个全为  舒适度指数
        title1 = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/span[1]', what='textContent')
        title2 = self.get_attr('xpath', '//*[@id="index_slide"]/div[2]/div[1]/div/span[1]', what='textContent')
        title3 = self.get_attr('xpath', '//*[@id="index_slide"]/div[3]/div[1]/div/span[1]', what='textContent')

        # 舒适级别
        level1 = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/span[2]', what='textContent')
        level2 = self.get_attr('xpath', '//*[@id="index_slide"]/div[2]/div[1]/div/span[2]', what='textContent')
        level3 = self.get_attr('xpath', '//*[@id="index_slide"]/div[3]/div[1]/div/span[2]', what='textContent')

        # 内容
        content1 = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/div', what='textContent')
        content2 = self.get_attr('xpath', '//*[@id="index_slide"]/div[2]/div[1]/div/div', what='textContent')
        content3 = self.get_attr('xpath', '//*[@id="index_slide"]/div[3]/div[1]/div/div', what='textContent')

        print(title1 + '----' + level1 + ':' + content1)
        print(title2 + '----' + level2 + ':' + content2)
        print(title3 + '----' + level3 + ':' + content3)
        # 三张图 http://h5.zuimeitianqi.com/page/zh/res/img/lifeindex_banner/ic_lifeindex_banner_comfort.svg
        pic1 = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[2]/img', what='src')
        pic2 = self.get_attr('xpath', '//*[@id="index_slide"]/div[2]/div[2]/img', what='src')
        pic3 = self.get_attr('xpath', '//*[@id="index_slide"]/div[3]/div[2]/img', what='src')

        # 5
        txt_num = 0
        if title1 and title2 and title3 == '舒适度指数':
            txt_num += 1
        if level1 == '舒适' and content1 == '温度合适、湿度适中，人体感觉最为舒适。':
            txt_num += 1
        elif level1 == '较舒适' and content1 == '人体感觉略偏凉，较为舒适，老人和小孩请注意添加衣物。' or '人体感觉偏暖，较为舒适，适当增加空气流动。':
            txt_num += 1
        elif level1 == '不舒适' and content1 == '人体感觉较冷，不舒适，请注意保暖。' or '人体感觉偏热，不舒适，可适当降温。':
            txt_num += 1
        elif level1 == '极不舒适' and content1 == '人体感觉寒冷，极不适应，注意保暖防寒，防止冻伤。' or '人体感觉很热，极不适应，注意防暑降温，以防中暑。':
            txt_num += 1

        if level2 == '舒适' and content2 == '温度合适、湿度适中，人体感觉最为舒适。':
            txt_num += 1
        elif level2 == '较舒适' and content2 == '人体感觉略偏凉，较为舒适，老人和小孩请注意添加衣物。' or '人体感觉偏暖，较为舒适，适当增加空气流动。':
            txt_num += 1
        elif level2 == '不舒适' and content2 == '人体感觉较冷，不舒适，请注意保暖。' or '人体感觉偏热，不舒适，可适当降温。':
            txt_num += 1
        elif level2 == '极不舒适' and content2 == '人体感觉寒冷，极不适应，注意保暖防寒，防止冻伤。' or '人体感觉很热，极不适应，注意防暑降温，以防中暑。':
            txt_num += 1

        if level3 == '舒适' and content3 == '温度合适、湿度适中，人体感觉最为舒适。':
            txt_num += 1
        elif level3 == '较舒适' and content3 == '人体感觉略偏凉，较为舒适，老人和小孩请注意添加衣物。' or '人体感觉偏暖，较为舒适，适当增加空气流动。':
            txt_num += 1
        elif level3 == '不舒适' and content3 == '人体感觉较冷，不舒适，请注意保暖。' or '人体感觉偏热，不舒适，可适当降温。':
            txt_num += 1
        elif level3 == '极不舒适' and content3 == '人体感觉寒冷，极不适应，注意保暖防寒，防止冻伤。' or '人体感觉很热，极不适应，注意防暑降温，以防中暑。':
            txt_num += 1

        if pic1 and pic2 and pic3 == 'http://s1.zuimeitianqi.com/page/dist/res/img/lifeindex_banner/ic_lifeindex_banner_comfort.svg':
            txt_num += 1

        if date_num + txt_num == 7:
            return 1
        else:
            return 2

    # 生活指数 列表
    def life_list(self):
        num = 0
        # 生活指数
        title = self.get_text('xpath', '//*[@id="life_index"]/div/div')
        if title == '生活指数':
            num += 1
            print(1)
        print(title)
        # 穿衣指数
        dress_icon = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[1]/em/img', what='src')
        dress_name = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[1]/div/span[1]', what='textContent')
        dress_txt = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[1]/div/span[2]', what='textContent')
        if dress_icon == 'http://s1.zuimeitianqi.com/page/dist/res/img/lifeindex/ic_lifeindex_dress.svg' and dress_name == '穿衣指数' and contain_chinese_one(dress_txt) == 1:
            num += 1
            print(2)
        print(dress_name, dress_txt)
        # 运动指数
        spot_icon = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[2]/em/img', what='src')
        spot_name = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[2]/div/span[1]', what='textContent')
        spot_txt = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[2]/div/span[2]', what='textContent')
        if spot_icon == 'http://s1.zuimeitianqi.com/page/dist/res/img/lifeindex/ic_lifeindex_sport.svg' and spot_name == '运动指数' and contain_chinese_one(spot_txt) == 1:
            num += 1
            print(3)
        print(spot_name, spot_txt)
        # 感冒指数
        cold_icon = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[3]/em/img', what='src')
        cold_name = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[3]/div/span[1]', what='textContent')
        cold_txt = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[3]/div/span[2]', what='textContent')
        if cold_icon == 'http://s1.zuimeitianqi.com/page/dist/res/img/lifeindex/ic_lifeindex_cold.svg' and cold_name == '感冒指数' and contain_chinese_one(cold_txt) == 1:
            num += 1
            print(4)
        print(cold_name, cold_txt)
        # 洗车指数
        car_icon = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[4]/em/img', what='src')
        car_name = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[4]/div/span[1]', what='textContent')
        car_txt = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[4]/div/span[2]', what='textContent')
        if car_icon == 'http://s1.zuimeitianqi.com/page/dist/res/img/lifeindex/ic_lifeindex_carwash.svg' and car_name == '洗车指数' and contain_chinese_one(car_txt) == 1:
            num += 1
            print(5)
        print(car_name, car_txt)
        # 钓鱼指数
        fish_icon = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[5]/em/img', what='src')
        fish_name = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[5]/div/span[1]', what='textContent')
        fish_txt = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[5]/div/span[2]', what='textContent')
        if fish_icon == 'http://s1.zuimeitianqi.com/page/dist/res/img/lifeindex/ic_lifeindex_fishing.svg' and fish_name == '钓鱼指数' and contain_chinese_one(fish_txt) == 1:
            num += 1
            print(6)
        print(fish_name, fish_txt)
        # 防晒指数
        antisun_icon = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[6]/em/img', what='src')
        antisun_name = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[6]/div/span[1]', what='textContent')
        antisun_txt = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[6]/div/span[2]', what='textContent')
        if antisun_icon == 'http://s1.zuimeitianqi.com/page/dist/res/img/lifeindex/ic_lifeindex_sunscreen.svg' and antisun_name == '防晒指数' and contain_chinese_one(antisun_txt) == 1:
            num += 1
            print(7)
        print(antisun_icon, antisun_name)

        if num == 7:
            return 1
        else:
            return 2

    # 运动健康
    def spot_card(self):
        num = 0
        # 运动健康
        title = self.get_text('xpath', '//*[@id="sport_health"]/div[1]/div')
        if title == '运动健康':
            num += 1
        print(title)
        print(num)
        # 晨练预报
        morning_name = self.get_attr('xpath', '//*[@id="radar_list"]/li[1]/span[1]', what='textContent')
        morning_data = self.get_attr('xpath', '//*[@id="radar_list"]/li[1]/span[2]', what='textContent')
        if morning_name == '晨练预报' and last_long(morning_data, 2) == '适宜':
            num += 1
        print(morning_name, morning_data)
        print(num)
        # 钓鱼预报
        top_fish = self.get_attr('xpath', '//*[@id="life_index"]/dl/dd[5]/div/span[2]', what='textContent')
        fish_name = self.get_attr('xpath', '//*[@id="radar_list"]/li[2]/span[1]', what='textContent')
        fish_data = self.get_attr('xpath', '//*[@id="radar_list"]/li[2]/span[2]', what='textContent')
        if fish_name == '钓鱼预报' and last_long(fish_data, 2) == '适宜':
            num += 1
        if top_fish == '不宜' and fish_data == '不适宜':
            num += 1
        elif top_fish == '适宜' and fish_data == '适宜':
            num += 1
        elif top_fish == '较适宜' and fish_data == '较适宜':
            num += 1
        print(fish_name, fish_data+'----' + top_fish)
        print(num)
        # 骑单车预报
        bicycle_name = self.get_attr('xpath', '//*[@id="radar_list"]/li[3]/span[1]', what='textContent')
        bicycle_data = self.get_attr('xpath', '//*[@id="radar_list"]/li[3]/span[2]', what='textContent')
        if bicycle_name == '骑单车预报' and last_long(bicycle_data, 2) == '适宜':
            num += 1
        print(bicycle_name, bicycle_data)
        print(num)
        # 跑步预报
        run_name = self.get_attr('xpath', '//*[@id="radar_list"]/li[4]/span[1]', what='textContent')
        run_data = self.get_attr('xpath', '//*[@id="radar_list"]/li[4]/span[2]', what='textContent')
        if run_name == '跑步预报' and last_long(run_data, 2) == '适宜':
            num += 1
        print(run_name, run_data)
        print(num)
        # 划船预报
        ship_name = self.get_attr('xpath', '//*[@id="radar_list"]/li[5]/span[1]', what='textContent')
        ship_data = self.get_attr('xpath', '//*[@id="radar_list"]/li[5]/span[2]', what='textContent')
        if ship_name == '划船预报' and last_long(ship_data, 2) == '适宜':
            num += 1
        print(ship_name, ship_data)
        print(num)
        # 放风筝预报
        kite_name = self.get_attr('xpath', '//*[@id="radar_list"]/li[6]/span[1]', what='textContent')
        kite_data = self.get_attr('xpath', '//*[@id="radar_list"]/li[6]/span[2]', what='textContent')
        if kite_name == '放风筝预报' and last_long(kite_data, 2) == '适宜':
            num += 1
        print(kite_name, kite_data)
        print(num)
        print('num为：' + str(num))

        if num == 8:
            return 1
        else:
            return 2

    # life 生活资讯
    def life_operate_wrapper(self):
        try:
            i = Share().operate_wrapper()
        except BaseException:
            print('从共用页面里->调用生活资讯页面失败！')
            logger.info('从共用页面里->调用生活资讯页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # life 生活资讯 更多 页面
    def life_operate_wrapper_more(self):
        try:
            i = Share().operate_wrapper_more(450)
        except BaseException:
            print('从共用页面里->调用生活资讯 更多 页面失败！')
            logger.info('从共用页面里->调用生活资讯 更多 页面页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # life 天气快讯
    def life_reptile_news(self):
        try:
            i = Share().reptile_news()
        except BaseException:
            print('从共用页面里->调用天气快讯页面失败！')
            logger.info('从共用页面里->调用天气快讯页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # life 天气快讯 更多 页面
    def life_reptile_news_more(self):
        try:
            i = Share().reptile_news_more(400)
        except BaseException:
            print('从共用页面里->调用天气快讯 更多 页面页面失败！')
            logger.info('从共用页面里->调用天气快讯 更多 页面页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # life 天气纵览
    def life_news_video(self):
        try:
            i = Share().news_video()
        except BaseException:
            print('从共用页面里->调用天气纵览页面失败！')
            logger.info('从共用页面里->调用天气纵览页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    #  life 天气纵览 更多 页面
    def life_news_video_more(self):
        try:
            i = Share().news_video_more(650)
        except BaseException:
            print('从共用页面里->调用天气纵览 更多 页面失败！')
            logger.info('从共用页面里->调用天气纵览 更多 页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # life 猜你喜欢
    def life_weather_news(self):
        try:
            i = Share().weather_news()
        except BaseException:
            print('从共用页面里->调用猜你喜欢页面失败！')
            logger.info('从共用页面里->调用猜你喜欢页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # life 猜你喜欢 更多页面
    def life_weather_news_more(self):
        try:
            i = Share().weather_news_more(450)
        except BaseException:
            print('从共用页面里->调用猜你喜欢 更多页面失败！')
            logger.info('从共用页面里->调用猜你喜欢 更多页面失败！')
        else:
            if i == 1:
                return 1
            else:
                return 2

    # life 版权信息
    def life_copyright(self):
        try:
            i = Share().copyright()
        except BaseException:
            print('从共用页面里->调用验证页面底部版权信息失败！')
            logger.info('从共用页面里->调用验证页面底部版权信息失败！')
        else:
            if i == 1:
                return 1
            else:
                return 2

    # life 生活指数 列表 点击跳转
    def life_list_click(self):
        num = 0

        # 穿衣指数
        self.click('xpath', '//*[@id="life_index"]/dl/dd[1]/div/span[1]')
        time.sleep(1)
        title_dress = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/span[1]', what='textContent')
        if title_dress == '穿衣指数':
            num += 1
        print(title_dress)
        self.driver.back()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 100)
        # 运动指数
        self.click('xpath', '//*[@id="life_index"]/dl/dd[2]/div/span[1]')
        time.sleep(1)
        title_spot = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/span[1]', what='textContent')
        if title_spot == '运动指数':
            num += 1
        print(title_spot)
        self.driver.back()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 100)
        # 感冒指数
        self.click('xpath', '//*[@id="life_index"]/dl/dd[3]/div/span[1]')
        time.sleep(1)
        title_cold = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/span[1]', what='textContent')
        if title_cold == '感冒指数':
            num += 1
        print(title_cold)
        self.driver.back()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 100)
        # 洗车指数
        self.click('xpath', '//*[@id="life_index"]/dl/dd[4]/div/span[1]')
        time.sleep(1)
        title_car = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/span[1]', what='textContent')
        if title_car == '洗车指数':
            num += 1
        print(title_car)
        self.driver.back()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 100)
        # 钓鱼指数
        self.click('xpath', '//*[@id="life_index"]/dl/dd[5]/div/span[1]')
        time.sleep(1)
        title_fish = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/span[1]', what='textContent')
        if title_fish == '钓鱼指数':
            num += 1
        print(title_fish)
        self.driver.back()
        time.sleep(1)
        load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 100)
        # 防晒指数
        self.click('xpath', '//*[@id="life_index"]/dl/dd[6]/div/span[1]')
        time.sleep(1)
        title_antisun = self.get_attr('xpath', '//*[@id="index_slide"]/div[1]/div[1]/div/span[1]', what='textContent')
        if title_antisun == '防晒指数':
            num += 1
        print(title_antisun)

        if num == 6:
            return 1
        else:
            return 2


if __name__ == '__main__':
    print(LifePage().life_news_video_more())
