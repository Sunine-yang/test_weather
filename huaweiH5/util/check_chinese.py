# 判断字符串是否包含五个或以上中文
def contain_chinese(check_str):
    num = 0
    for ch in check_str:
        if '\u4e00' <= ch <= '\u9fa5':
            num += 1
            if num == 5:
                return 1
    return 2


# 判断字符串是否包含中文
def contain_chinese_one(check_str):
    for ch in check_str:
        if '\u4e00' <= ch <= '\u9fa5':
            return 1
    return 2
