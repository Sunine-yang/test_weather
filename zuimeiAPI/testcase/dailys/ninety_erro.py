def ninety_erro_case(data):
    nine_erro_t1 = ''
    nine_erro_t2 = ''
    nine_erro_t3 = ''
    nine_erro_t4 = ''
    try:
        data_status = data['status']
    except BaseException:
        data_status = 200
        try:
            data_resultcode = data['resultcode']
        except BaseException:
            nine_erro_t3 = '接口异常'
        else:
            if data_resultcode != 0:
                nine_erro_t4 = '接口异常'
    if data_status == 500:
        print(f'此城市90天接口异常')
        # logger.info(f'此城市90天接口异常，定位：{accucode}')
        nine_erro_t1 = '接口异常'
        # with open(self.text_aaa + "ninety_erro.txt", mode='a+', encoding='utf-8') as f:
        #     f.write(f'[{accucode} / {cityname}] - 接口异常\n')
    else:
        # 判断是否 91 天
        days = len(data['dailys']['dailyweathers'])
        if days == 91:
            pass
        else:
            print(f'91天-实际返回天数-[{days}]\n')
            # logger.info(
            #     f'90天数据返回天数不正确，实际返回天数为{days}，定位为：{accucode}')
            nine_erro_t2 = f'{days}[返回天数91]'
            # with open(self.text_aaa + "ninety_erro.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(f'[{accucode} / {cityname}] - 实际返回天数-[{days}]\n')
    return nine_erro_t1, nine_erro_t2, nine_erro_t3, nine_erro_t4
