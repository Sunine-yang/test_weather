# coding=<encoding name> ： # coding=utf-8
# 接口是否有返回
def big_erro_case(data):
    result_OK = data['resultinfo']
    if result_OK != 'OK':
        print(f"接口异常")
        return f'接口异常'
    else:
        return ''
