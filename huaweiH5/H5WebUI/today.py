import time
from common.common_page import Share
from util.conf_read import ConfRead
from util.find_element import FindElement
from util.get_date import format_month, format_weekday
from util.get_driver import UtilWebDriver
from util.load_page import load_page
from util.regular_deal import get_num, get_api, get_tmp_num, get_icon_src, last_two, last_nineteen, last_five, \
    last_long, first_one
from log.Log import logger


class TodayPage(FindElement):
    def __init__(self):
        # 继承find element类
        super(TodayPage, self).__init__()
        # 创建配置文件读取对象
        cityData = ConfRead.conf_return('cityID.conf')
        # 读取城市名称和城市ID
        self.cityID = cityData.get('citydata', 'cityId')
        # 调用单例模式的driver
        self.driver = UtilWebDriver.get_driver()
        # 打开实况界面
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/today.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
            '=A1&orild=P4&source=zm&oriId=P2')
        self.driver.get(
            'about:blank')
        self.driver.get(
            f'http://h5.zuimeitianqi.com/page/zh/today.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
            '=A1&orild=P4&source=zm&oriId=P2')

        self.driver.implicitly_wait(10)
        time.sleep(2)

    '''
    
    ————————
    实况界面
    
    主卡片
    ————————
    
    '''

    # 城市名称
    def cityname(self):
        try:
            # 页面城市名称
            name = self.get_text('xpath', '//*[@id="city_name"]/span')
            # 打开配置文件
            cityData = ConfRead.conf_return('cityID.conf')
            # 读取城市名称
            cityName = cityData.get('citydata', 'cityName')

        except BaseException:
            print('获取城市名称失败！')
            logger.info('获取城市名称失败！')
        else:
            print(f'成功获取城市名称，页面城市名称为：{name}，读取conf城市名称为：{cityName}')
            logger.info(f'成功获取城市名称，页面城市名称为：{name}，读取conf城市名称为：{cityName}')
            if name == cityName:
                return 1
            else:
                return 2

    # 日期，几月几日
    def date(self):
        try:
            # 页面显示的日期
            month = self.get_text('xpath', '//*[@id="city_info"]/span[1]')
            # 当前的日期
            realdata = format_month()
        except BaseException:
            print('获取当前日期失败！')
            logger.info('获取当前日期失败！')
        else:
            print(f'成功获取当前日期，页面日期为：{month},当前日期为：{realdata}')
            logger.info(f'成功获取当前日期，页面日期为：{month},当前日期为：{realdata}')
            if month == realdata:
                return 1
            else:
                return 2

    # 星期几
    def weekday(self):
        try:
            # 页面显示星期
            week = self.get_text('xpath', '//*[@id="city_info"]/span[2]')
            # 当前星期
            realweekday = format_weekday()
        except BaseException:
            print('获取当前星期几失败！')
            logger.info('获取当前星期几失败！')
        else:
            print(f'成功获取当前星期，页面显示今天星期：{week}，当前实际星期：{realweekday}')
            logger.info(f'成功获取当前星期，页面显示今天星期：{week}，当前实际星期：{realweekday}')
            if week == realweekday:
                return 1
            else:
                return 2

    # 最低最高温
    def range_tmp(self):
        try:
            tmp1 = self.get_text('xpath', '//*[@id="tmp_section"]/span[1]')
            # 最高温度
            max_tmp = int(get_tmp_num(tmp1))
            tmp2 = self.get_text('xpath', '//*[@id="tmp_section"]/span[2]')
            # 最低温度
            min_tmp = int(get_tmp_num(tmp2))
        except BaseException:
            print('获取最低最高温度失败！')
            logger.info('获取最低最高温度失败！')
        else:
            print(f'成功获取最高温，最高温度为：{max_tmp}，最低气温为：{min_tmp}')
            logger.info(f'成功获取最高温，最高温度为：{max_tmp}，最低气温为：{min_tmp}')
            if max_tmp > min_tmp:
                return 1
            else:
                return 2

    # 当前气温
    def tmp(self):
        try:
            # 页面显示现在实况温度
            now = int(self.get_text('xpath', '//*[@id="tmp"]'))
            tmp1 = self.get_text('xpath', '//*[@id="tmp_section"]/span[1]')
            # 最高温度
            max_tmp = int(get_tmp_num(tmp1))
            tmp2 = self.get_text('xpath', '//*[@id="tmp_section"]/span[2]')
            # 最低温度
            min_tmp = int(get_tmp_num(tmp2))
        except BaseException:
            print('获取当前实时气温失败!')
            logger.info('获取当前实时气温失败！')
        else:
            print(f'成功获取当前实时气温，温度为：{now}，最高：{max_tmp},最低：{min_tmp}')
            logger.info(f'成功获取当前实时气温，温度为：{now}，最高：{max_tmp},最低：{min_tmp}')
            if min_tmp <= now <= max_tmp:
                return 1
            else:
                return 2

    # 空气质量指数
    def api(self):
        try:
            # 空气质量指数
            api = self.get_text('xpath', '//*[@id="aqi_info"]')
            air = int(get_num(api))
        except BaseException:
            print('获取当前空气质量失败！')
            logger.info('获取当前空气质量失败！')
        else:
            print(f'成功获取当前空气质量，指数为：{air}')
            logger.info(f'成功获取当前空气质量，指数为：{air}')
            if 0 <= air <= 500:
                return 1
            else:
                return 2

    # 空气质量描述
    def api_word(self):
        try:
            api = self.get_text('xpath', '//*[@id="aqi_info"]')
            # 指数
            air = int(get_num(api))
            # 文字描述
            word = get_api(api)
        except BaseException:
            print('获取空气质量文字描述失败！')
            logger.info('获取空气质量文字描述失败！')
        else:
            print(f'成功获取空气质量文字描述，空气质量为：{word}，指数为：{air}')
            logger.info(f'成功获取空气质量文字描述，空气质量为：{word}，指数为：{air}')

            if 0 <= air <= 50 and word == '优':
                return 1
            elif 51 <= air <= 100 and word == '良':
                return 1
            elif 101 <= air <= 150 and word == '轻度':
                return 1
            elif 151 <= air <= 200 and word == '中度':
                return 1
            elif 201 <= air <= 300 and word == '重度':
                return 1
            elif 300 <= air <= 500 and word == '严重':
                return 1
            else:
                return 2

    # 天气状况文字描述与图标是否匹配
    def wea_txt_icon(self):
        try:
            wea_txt = self.get_text('xpath', '//*[@id="wea_txt"]')
            wea_icon = self.get_attr('xpath', '//*[@id="wea_icon"]/img', what='src')
            wea_icon_txt = get_icon_src(wea_icon)
        except BaseException:
            print('获取天气状况文字描述与图标失败！')
            logger.info('获取天气状况文字描述与图标失败！')
        else:
            print(f'获取天气状况文字描述与图标src关键词，天气状况为：{wea_txt},图标src关键词为：{wea_icon_txt}')
            logger.info(f'获取天气状况文字描述与图标src关键词，天气状况为：{wea_txt},图标src关键词为：{wea_icon_txt}')
            if wea_txt == '晴' and wea_icon_txt == 'sunny' or 'sunny_night':
                return 1
            elif wea_txt == '多云' and wea_icon_txt == 'cloudy' or 'mostlycloudy' or 'mostlycloudy_night':
                return 1
            elif wea_txt == '阴天' and wea_icon_txt == 'overcast':
                return 1
            elif wea_txt == '雷阵雨' and wea_icon_txt == 'thundeshower':
                return 1
            elif wea_txt == '阵雨' and wea_icon_txt == 'shower':
                return 1
            elif wea_txt == '小雨' and wea_icon_txt == 'lightrain':
                return 1
            elif wea_txt == '中雨' and wea_icon_txt == 'moderaterain':
                return 1
            elif wea_txt == '大雨' and wea_icon_txt == 'heavyrain':
                return 1
            elif wea_txt == '暴雨' and wea_icon_txt == 'rainstorm':
                return 1
            elif wea_txt == '冻雨' and wea_icon_txt == 'sleet':
                return 1
            elif wea_txt == '雨夹雪' and wea_icon_txt == 'rainsnow':
                return 1
            elif wea_txt == '阵雪' and wea_icon_txt == 'showersnow':
                return 1
            elif wea_txt == '小雪' and wea_icon_txt == 'lightsnow':
                return 1
            elif wea_txt == '中雪' and wea_icon_txt == 'moderatesnow':
                return 1
            elif wea_txt == '大雪' and wea_icon_txt == 'heavysnow':
                return 1
            elif wea_txt == '雾' and wea_icon_txt == 'fog':
                return 1
            elif wea_txt == '浮尘' and wea_icon_txt == 'dust':
                return 1
            elif wea_txt == '沙尘暴' and wea_icon_txt == 'dust_storm':
                return 1
            elif wea_txt == '霾' and wea_icon_txt == 'haze':
                return 1
            elif wea_txt == '夜晚晴' and wea_icon_txt == 'nightsunny':
                return 1
            elif wea_txt == '夜晚多云' and wea_icon_txt == 'nightcloudy':
                return 1
            else:
                return 2

    # 天气预警信息 横幅
    # def warn(self):
    #     try:
    #         warn = self.get_text('xpath', '//*[@id="warn_info"]')
    #         if warn == '':
    #             print('当前城市当前时间没有天气预警信息')
    #             logger.info('当前城市当前时间没有天气预警信息')
    #         else:
    #             print(f'当前城市当前时间有天气预警信息,天气预警信息为：{warn}')
    #             logger.info(f'当前城市当前时间有天气预警信息,天气预警信息为：{warn}')
    #             try:
    #                 warn_contentself = self.get_text('xpath', '//*[@id="warn_content"]')
    #             except BaseException:
    #                 print('没有找到顶部预警条状横幅！')
    #                 logger.info('没有找到顶部预警条状横幅！')
    #                 return 2
    #             else:
    #                 print(f'顶部条状横幅显示正常，内容为：{warn_contentself}')
    #                 logger.info(f'顶部条状横幅显示正常，内容为：{warn_contentself}')
    #                 return 1
    #     except BaseException:
    #         print('获取预警信息失败!')
    #         logger.info('获取预警信息失败!')
    #     else:
    #         return 1

    # 天气预警信息二级页面
    def warn_page_two(self):
        time.sleep(2)
        warn = self.get_text('xpath', '//*[@id="warn_info"]')
        if warn == '':
            print('当前城市没有天气预警，所以不验证天气预警二级页面~')
            logger.info('当前城市没有天气预警，所以不验证天气预警二级页面~')
            return 1
        else:
            try:
                time.sleep(2)
                page_two = UtilWebDriver.wait_element_present('xpath', '//*[@id="warn_info"]', timeout=10)
                page_two.click()
                time.sleep(2)
                # 预警
                title = self.get_text('xpath', '//*[@id="warn_box"]/div/div/div[1]/span')
                title_txt = last_two(title)
                # print(title_txt)
                # 国家预警信息中心...
                content = self.get_text('xpath', '//*[@id="warn_box"]/div/div/div[3]')
                content_txt = last_nineteen(content)
                # print(content_txt)
                # 避灾指南
                disaster_txt = self.get_text('xpath', '//*[@id="operate_wrapper"]/div[1]/div[1]')
                # print(disaster_txt)
                # first_防御指南
                first = self.get_text('xpath', '//*[@id="operate_list"]/li[1]/a/div[1]/h3')
                first_txt = last_five(first)
                # print(first_txt)
                # last_防御指南
                last = self.get_text('xpath', '//*[@id="operate_list"]/li[6]/a/div[1]/h3')
                last_txt = last_five(last)
                time.sleep(2)
                # print(last_txt)
            except BaseException:
                print("天气预警二级页面元素获取验证失败！")
                logger.info('天气预警二级页面元素获取验证失败！')
            else:
                if \
                        title_txt == '预警' \
                                and content_txt == '（预警信息来源：国家预警信息发布中心）' \
                                and disaster_txt == '避灾指南' \
                                and first_txt == '及防御指南' \
                                and last_txt == '及防御指南':
                    self.driver.back()
                    time.sleep(2)
                    return 1
                else:
                    self.driver.back()
                    time.sleep(2)
                    return 2

    # 判断实况温度与温度文字描述是否相匹配
    def hum_tmp(self):
        try:
            hum_now = int(self.get_text('xpath', '//*[@id="tmp"]'))
            hum = self.get_text('xpath', '//*[@id="hum_txt"]')
        except BaseException:
            print('温度文字描述获取失败！')
            logger.info('温度文字描述获取失败！')
        else:
            print(f'温度文字描述获取成功，当前温度描述为：{hum},当前温度为：{hum_now}')
            logger.info(f'温度文字描述获取成功，当前温度描述为：{hum}-------------当前温度为：{hum_now}')
            if hum_now < -10 and hum == '天寒地冻，感觉极冷':
                return 1
            elif hum_now <= 4 and hum == '寒冷刺骨，感觉很冷':
                return 1
            elif 4 < hum_now <= 8 and hum == '凄凄阴冷 ，感觉冷':
                return 1
            elif 8 < hum_now <= 13 and hum == '略感凉意 ，感觉有点冷':
                return 1
            elif 13 < hum_now <= 18 and hum == '温度低，感觉冷':
                return 1
            elif 18 < hum_now <= 20 and hum == '略感微凉，感觉凉':
                return 1
            elif 20 < hum_now <= 26 and hum == '温度舒适，感觉凉快':
                return 1
            elif 27 < hum_now <= 30 and hum == '温度高，感觉不适':
                return 1
            elif 30 < hum_now <= 33 and hum == '感觉很热，需要空调':
                return 1
            elif 33 < hum_now <= 35 and hum == '暑气闷热，需要冲凉':
                return 1
            elif 35 < hum_now <= 37 and hum == '气温太热，大汗淋漓':
                return 1
            elif hum_now > 37 and hum == '气温极热，热不可耐':
                return 1
            else:
                return 2

    '''
    ————————
    实况界面
    
    数据来源
    ————————
    '''

    # 数据来源检查
    def data_sources(self):
        try:
            # 天气数据来源
            weather_txt = self.get_text('xpath', '//*[@id="page_container"]/div[7]/div/span[1]')
            # 中国气象
            weather_name = self.get_text('xpath', '//*[@id="page_container"]/div[7]/div/span[3]')
            # 中国气象图标
            weather_logo = self.find_element('xpath', '//*[@id="weather_logo_icon"]')
        except BaseException:
            print('天气数据来源信息获取失败！')
            logger.info('天气数据来源信息获取失败！')
        else:
            if weather_txt == '天气数据来源' and weather_name == '中国气象':
                print(f'天气数据来源信息获取成功，显示正常，{weather_txt}:{weather_name}')
                logger.info(f'天气数据来源信息获取成功，显示正常，{weather_txt}:{weather_name}')
                return 1
            else:
                print(f'天气数据来源信息获取成功，显示不正常！显示为：{weather_txt}:{weather_name}')
                logger.info(f'天气数据来源信息获取成功，显示不正常！显示为：{weather_txt}:{weather_name}')
                return 2

    # 天气各项数据卡片图标检查
    def weather_item_icon(self):
        try:
            # 体感温度
            feel = self.get_attr('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[1]/span[1]/img', what='src')
            # 能见度
            vis = self.get_attr('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[2]/span[1]/img', what='src')
            # 湿度
            humidity = self.get_attr('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[3]/span[1]/img', what='src')
            # 紫外线
            uvIndex = self.get_attr('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[4]/span[1]/img', what='src')



        except BaseException:
            print('天气各项数据卡片图标元素src获取失败！')
            logger.info('天气各项数据卡片图标元素src获取失败！')
        else:
            print('天气各项数据卡片图标元素src获取成功！')
            print(f'体感温度src为:{feel}')
            print(f'湿度src为:{humidity}')
            print(f'紫外线src为:{uvIndex}')
            print(f'能见度src为:{vis}')

            logger.info('天气各项数据卡片图标元素src获取成功！')
            logger.info(f'体感温度src为:{feel}')
            logger.info(f'湿度src为:{humidity}')
            logger.info(f'紫外线src为:{uvIndex}')
            logger.info(f'能见度src为:{vis}')

            # 添加计数器
            num = 0

            wea_icon_src = ConfRead.conf_return('weather_icon_src.conf')

            feel_conf = wea_icon_src.get('weather_icon_src', 'feel_src')
            print(f'读取的配置文件feel为：{feel_conf}')
            logger.info(f'读取的配置文件feel为：{feel_conf}')

            vis_conf = wea_icon_src.get('weather_icon_src', 'vis_src')
            print(f'读取的配置文件vis为：{vis_conf}')
            logger.info(f'读取的配置文件vis为：{vis_conf}')

            humidity_conf = wea_icon_src.get('weather_icon_src', 'humidity_src')
            print(f'读取的配置文件humidity为：{humidity_conf}')
            logger.info(f'读取的配置文件humidity为：{humidity_conf}')

            uvIndex_conf = wea_icon_src.get('weather_icon_src', 'uvIndex_src')
            print(f'读取的配置文件uvIndex为：{uvIndex_conf}')
            logger.info(f'读取的配置文件uvIndex为：{uvIndex_conf}')

            if feel == feel_conf:
                num = num + 1
            if humidity == humidity_conf:
                num = num + 1
            if uvIndex == uvIndex_conf:
                num = num + 1
            if vis == vis_conf:
                num = num + 1

            print(f'weather_item_icon计数器计数为：{num}')
            logger.info(f'weather_item_icon计数器计数为：{num}')

            if num == 4:
                return 1
            else:
                return 2

    # 天气各项数据卡片数据检查
    def weather_item_data(self):
        try:
            # 体感温度
            feel = int(self.get_text('xpath', '//*[@id="feel_tmp"]'))
            feel_suf = self.get_text('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[1]/span[2]/em[2]')  # ℃
            # 湿度
            humidity = int(self.get_text('xpath', '//*[@id="t_hum"]'))
            humidity_suf = self.get_text('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[3]/span[2]/em[2]')  # %
            # 紫外线
            uvIndex = int(self.get_text('xpath', '//*[@id="t_uv"]'))
            uvIndex_suf = first_one(self.get_text('xpath', '//*[@id="t_level"]'))  # 级
            # 能见度
            vis = int(self.get_text('xpath', '//*[@id="t_vis"]'))
            vis_suf = self.get_text('xpath', '//*[@id="t_vis_unit"]')  # km


        except BaseException:
            print('天气各项数据卡片数据以及数据单位元素获取失败！')
            logger.info('天气各项数据卡片数据以及数据单位元素获取失败！')

        else:
            print('天气各项数据卡片图标元素src获取成功！')
            print(f'体感温度数据为:{feel}')
            print(f'体感温度单位为:{feel_suf}')
            print(f'湿度数据为:{humidity}')
            print(f'湿度单位为:{humidity_suf}')
            print(f'紫外线数据为:{uvIndex}')
            print(f'紫外线单位为:{uvIndex_suf}')
            print(f'能见度数据为:{vis}')
            print(f'能见度单位为:{vis_suf}')

            logger.info('各项天气指数数据及数据单位获取成功！')
            logger.info(f'体感数据为:{feel}')
            logger.info(f'体感温度单位为:{feel_suf}')
            logger.info(f'湿度数据为:{humidity}')
            logger.info(f'湿度单位为:{humidity_suf}')
            logger.info(f'紫外线数据为:{uvIndex}')
            logger.info(f'紫外线单位为:{uvIndex_suf}')
            logger.info(f'能见度数据为:{vis}')
            logger.info(f'能见度单位为:{vis_suf}')
            # 添加计数器
            num = 0
            # 实况温度
            real_data = int(self.get_text('xpath', '//*[@id="tmp"]'))

            if real_data - 5 <= feel <= real_data + 5:
                num = num + 1
            if feel_suf == '℃':
                num = num + 1
            if 0 <= humidity <= 100:
                num = num + 1
            if humidity_suf == '%':
                num = num + 1
            if 1 <= uvIndex <= 15:
                num = num + 1
            if uvIndex_suf == '级':
                num = num + 1
            if 0 <= vis <= 30:
                num = num + 1
            if vis_suf == 'km':
                num = num + 1

            if num == 8:
                return 1
            else:
                return 2

    # 天气各项数据卡片文字描述检查
    def weather_item_txt(self):
        try:

            # 体感温度
            feel = self.get_text('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[1]/span[3]')

            # 能见度
            vis = self.get_text('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[2]/span[3]')

            # 湿度
            humidity = self.get_text('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[3]/span[3]')

            # 紫外线
            uvIndex = self.get_text('xpath', '//*[@id="weather_card"]/div/div[3]/ul/li[4]/span[3]')





        except BaseException:
            print('天气各项数据卡片文字描述元素获取失败！')
            logger.info('天气各项数据卡片文字描述元素获取失败！')
        else:
            print('天气各项数据卡片文字描述元素获取成功！')
            print(f'体感温度描述为:{feel}')
            print(f'湿度描述为:{uvIndex}')
            print(f'紫外线描述为:{vis}')
            print(f'能见度描述为:{humidity}')

            num = 0

            if feel == '体感温度':
                num = num + 1
            if humidity == '湿度':
                num = num + 1
            if uvIndex == '紫外线':
                num = num + 1
            if vis == '能见度':
                num = num + 1

            if num == 4:
                return 1
            else:
                return 2

    '''
    ————————
    实况界面
    
    日出日落
    ————————
    '''

    # 日出日落
    def sun(self):
        i = Share().sun()
        if i == 1:
            return 1
        else:
            return 2

    # 日出日落二级页面
    def sun_page_two(self):
        i = Share().sun_page_two()
        if i == 1:
            return 1
        else:
            return 2

    '''
    实况页面
    
    分钟预报
    '''

    # 分钟预报
    def radar(self):
        try:
            # 分钟预报
            radar_title = self.get_text('xpath', '//*[@id="radar_box"]/div[1]/div[1]')
            # radar_content = self.get_text('xpath', '//*[@id="radar_box"]/div[2]')
        except BaseException:
            print('分钟预报页面元素未获取到或者页面内元素显示失败！')
            logger.info('分钟预报页面元素未获取到或者页面内元素显示失败！')
        else:
            print(f'分钟预报页面元素获取显示成功，分钟预报title显示为：{radar_title}')
            logger.info(f'分钟预报页面元素获取成功，分钟预报title显示为：{radar_title}')
            if radar_title == '分钟预报':
                return 1
            else:
                return 2

    # 分钟预报二级页面
    def radar_page_two(self, long=400):
        try:
            # 进入二级页面
            more = self.find_element('xpath', '//*[@id="radar_more"]')
            load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', long)
            more.click()

            self.click('xpath', '//*[@id="slide_box"]/div[3]/div[1]/div/div/img')
            time.sleep(1)
            # 截取卫星云图图片url .jpg
            slide_img = last_long(self.get_attr('xpath', '//*[@id="slide_box"]/div[1]/img', what='src'), 4)
            # 截取卫星云图播放按钮图标后缀 ressed.png
            play_img = last_long(self.get_attr('xpath', '//*[@id="slide_box"]/div[3]/div[1]/div/div/img', what='src'),
                                 10)
            # 降水雷达
            slide_txt = self.get_text('xpath', '//*[@id="page_container"]/div[2]/div')
            # 猜你喜欢
            you_like = self.get_text('xpath', '//*[@id="info_title"]/div/div[1]')
            # 推荐
            good = self.get_text('xpath', '//*[@id="info_tab_wrap"]/li[1]')
        except BaseException:
            print('分钟预报二级页面元素获取失败！')
            logger.info('分钟预报二级页面元素获取失败！')
        else:
            print(f'分钟预报二级页面元素获取成功，截取卫星云图图片地址后缀为：{slide_img}，'
                  f'截取卫星云图播放按钮图标后缀：{play_img}，降水雷达为：{slide_txt}，'
                  f'猜你喜欢显示为：{you_like}，'
                  f'猜你喜欢下推荐显示为：{good}')
            logger.info(f'分钟预报二级页面元素获取成功，截取卫星云图图片url：{slide_img}，'
                        f'截取卫星云图播放按钮图标后缀：{play_img}，降水雷达为：{slide_txt}，'
                        f'猜你喜欢显示为：{you_like}，'
                        f'猜你喜欢下推荐显示为：{good}')

            num = 0
            if slide_img == '.jpg':
                num = num + 1
            if play_img == 'normal.png' or 'ressed.png':
                num = num + 1
            if slide_txt == '降水雷达':
                num = num + 1
            if you_like == '猜你喜欢':
                num = num + 1
            if good == '推荐':
                num = num + 1
            if num == 5:
                self.driver.back()
                time.sleep(2)
                return 1
            else:
                self.driver.back()
                time.sleep(2)
                return 2

    # today生活指南
    def today_living_guide(self):
        try:
            i = Share().living_guide()
        except BaseException:
            print('从共用页面里->调用生活指南失败！')
            logger.info('从共用页面里->调用生活指南失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # today生活指南二级页面
    def today_living_guide_page_two(self):
        try:
            i = Share().living_guide_page_two(400)
        except BaseException:
            print('从共用页面里->调用生活指南二级页面失败！')
            logger.info('从共用页面里->调用生活指南二级页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # today生活资讯
    def today_operate_wrapper(self):
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

    # today 生活资讯 更多 页面
    def today_operate_wrapper_more(self):
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

    # today 天气快讯
    def today_reptile_news(self):
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

    # today 天气快讯 更多 页面
    def today_reptile_news_more(self):
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

    # today天气纵览
    def today_news_video(self):
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

    #  today天气纵览 更多 页面
    def today_news_video_more(self):
        try:
            i = Share().news_video_more(730)
        except BaseException:
            print('从共用页面里->调用天气纵览 更多 页面失败！')
            logger.info('从共用页面里->调用天气纵览 更多 页面失败！')
        else:
            if i == 1:
                return 1
            if i == 2:
                return 2

    # today猜你喜欢
    def today_weather_news(self):
        i = Share().weather_news()
        if i == 1:
            return 1
        if i == 2:
            return 2

    # today猜你喜欢 更多页面
    def today_weather_news_more(self):
        i = Share().weather_news_more(400)
        if i == 1:
            return 1
        else:
            return 2

    # today版权信息
    def today_copyright(self):
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

    # 搜索切换城市
    def change_city(self):
        try:
            # 城市搜索框
            change = self.find_element('xpath', '//*[@id="city_name"]')
            change.click()
            # cityid = 01010101
            # 输入北京
            self.input_text('xpath', '//*[@id="search_city"]', value='北京')
            time.sleep(1)
            # 选择第一个
            self.click('xpath', '//*[@id="location_info"]/div[3]/div[3]/ul/li[1]')
            time.sleep(1)

            cityname = self.get_attr('xpath', '//*[@id="city_name"]/span', what='textContent')
            print('cityname为：' + cityname)

            self.click('xpath', '//*[@id="tab_item"]/span[2]/em')
            time.sleep(1)
            page_url = self.driver.current_url
            print(page_url)
            self.click('xpath', '//*[@id="tab_item"]/span[3]/em')
            page_url2 = self.driver.current_url
            print(page_url2)

        except BaseException:
            print('搜索切换城市操作失败！')
            logger.info('搜索切换城市操作失败！')
        else:
            num = 0
            if cityname == '北京市':
                num += 1
                print(1)
            if '01010101' in page_url and page_url2:
                num += 1
                print(2)

            if num == 2:
                return 1
            else:
                return 2

    # 页面跳转 小时天气 多天预报 生活指数 新闻资讯
    # def page_jump(self):
    #     try:
    #         hourly_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/img', what='src')
    #         hourly_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[1]/span', what='textContent')
    #
    #         days_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/img', what='src')
    #         days_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[2]/span', what='textContent')
    #
    #         comfor_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/img', what='src')
    #         comfor_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[3]/span', what='textContent')
    #
    #         news_img = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/img', what='src')
    #         news_txt = self.get_attr('xpath', '//*[@id="page_jump"]/ul/li[4]/span', what='textContent')
    #     except BaseException:
    #         print('页面跳转 小时天气 多天预报 生活指数 新闻资讯 获取内容失败！')
    #         logger.info('页面跳转 小时天气 多天预报 生活指数 新闻资讯 获取内容失败！')
    #     else:
    #         num = 0
    #         if hourly_img == 'http://s1.zuimeitianqi.com/page/dist/res/img/page_btn/btn_page_hourly.svg' \
    #                 and days_img == 'http://s1.zuimeitianqi.com/page/dist/res/img/page_btn/btn_page_days.svg' \
    #                 and comfor_img == 'http://s1.zuimeitianqi.com/page/dist/res/img/page_btn/btn_page_live.svg' \
    #                 and news_img == 'http://s1.zuimeitianqi.com/page/dist/res/img/page_btn/btn_page_news.svg':
    #             num += 1
    #             print(1)
    #         if hourly_txt == '小时天气' and days_txt == '多天预报' and comfor_txt == '生活指数' and news_txt == '新闻资讯':
    #             num += 1
    #             print(2)
    #
    #         self.driver.get(
    #             f'http://h5.zuimeitianqi.com/page/zh/today.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
    #             '=A1&orild=P4&source=zm&oriId=P2')
    #         self.driver.refresh()
    #         time.sleep(3)
    #         load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 500)
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[1]/span')
    #         time.sleep(3)
    #         page_url = self.driver.current_url
    #         if 'hourly' in page_url:
    #             num += 1
    #             print(3)
    #
    #         self.driver.get(
    #             f'http://h5.zuimeitianqi.com/page/zh/today.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
    #             '=A1&orild=P4&source=zm&oriId=P2')
    #         self.driver.refresh()
    #         time.sleep(3)
    #         load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 500)
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[2]/span')
    #         time.sleep(3)
    #         page_url = self.driver.current_url
    #         if 'days' in page_url:
    #             num += 1
    #             print(4)
    #
    #         self.driver.get(
    #             f'http://h5.zuimeitianqi.com/page/zh/today.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
    #             '=A1&orild=P4&source=zm&oriId=P2')
    #         self.driver.refresh()
    #         time.sleep(3)
    #         load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 500)
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[3]/span')
    #         time.sleep(3)
    #         page_url = self.driver.current_url
    #         if 'comfor' in page_url:
    #             num += 1
    #             print(5)
    #
    #         self.driver.get(
    #             f'http://h5.zuimeitianqi.com/page/zh/today.html?cityId={self.cityID}&lan=zh-cn&partner=hw&space'
    #             '=A1&orild=P4&source=zm&oriId=P2')
    #         self.driver.refresh()
    #         time.sleep(3)
    #         load_page('//*[@id="float_fixed_advert"]/div/ul/li/a/img', 500)
    #         self.click('xpath', '//*[@id="page_jump"]/ul/li[4]/img')
    #         time.sleep(3)
    #         page_url = self.driver.current_url
    #         if 'news' in page_url:
    #             num += 1
    #             print(6)
    #
    #         if num == 6:
    #             return 1
    #         else:
    #             return 2

    # def game(self):
    #     try:
    #         i = Share().little_game()
    #     except BaseException:
    #         print('从共用页面里->调用小游戏 和 小游戏更多页面失败！')
    #         logger.info('从共用页面里->调用小游戏 和 小游戏更多页面失败！')
    #     else:
    #         if i == 1:
    #             return 1
    #         else:
    #             return 2


if __name__ == '__main__':
    a = TodayPage()
    # print(a.cityname())
    # print(a.date())
    # print(a.weekday())
    # print(a.max_tmp())
    # print(a.min_tmp())
    # print(a.tmp())
    # print(a.api())
    print(a.radar_page_two())
