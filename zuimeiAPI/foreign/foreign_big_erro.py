# coding=<encoding name> ： # coding=utf-8
# 接口是否有返回
def foreign_big_erro_case(data, time_out, code, re):
    big_erro_1 = ''
    big_erro_2 = ''
    result_OK = data['resultinfo']
    if time_out == 2:
        big_erro_1 = '响应时间 > 5s'
    if result_OK != 'OK':
        print(f"接口异常")
        big_erro_2 = f'接口异常-[{code}]\n接口返回:[{re}]'
    else:
        pass
    return big_erro_1, big_erro_2
