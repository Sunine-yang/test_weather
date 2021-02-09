def ninety_erro_case(data, timeout, code, re):
    nine_erro_t1 = ''
    nine_erro_t2 = ''
    nine_erro_t3 = ''
    nine_erro_t4 = ''
    nine_erro_t5 = ''
    try:
        data_status = data['status']
    except BaseException:
        data_status = 200
        try:
            data_resultcode = data['resultcode']
        except BaseException:
            nine_erro_t3 = f'接口异常[{code}]\n接口返回:[{re}]'
        else:
            if data_resultcode != '0':
                nine_erro_t4 = f'接口异常[{code}]\n接口返回:[{re}]'
    if data_status == 500:
        print(f'此城市90天接口异常')
        # logger.info(f'此城市90天接口异常，定位：{accucode}')
        nine_erro_t1 = f'接口异常[{code}]\n接口返回:[{re}]'
        # with open(self.text_aaa + "ninety_erro.txt", mode='a+', encoding='utf-8') as f:
        #     f.write(f'[{accucode} / {cityname}] - 接口异常\n')
    else:
        # 判断是否 91 天
        days = len(data['dailys']['dailyweathers'])
        if days == 92:
            pass
        else:
            print(f'92天-实际返回天数-[{days}]\n')
            # logger.info(
            #     f'90天数据返回天数不正确，实际返回天数为{days}，定位为：{accucode}')
            nine_erro_t2 = f'{days}[返回天数92]'
            # with open(self.text_aaa + "ninety_erro.txt", mode='a+', encoding='utf-8') as f:
            #     f.write(f'[{accucode} / {cityname}] - 实际返回天数-[{days}]\n')
    if timeout == 2:
        nine_erro_t5 = '响应时间 > 5s'

    return nine_erro_t1, nine_erro_t2, nine_erro_t3, nine_erro_t4, nine_erro_t5
