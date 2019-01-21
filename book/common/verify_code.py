# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-21 下午3:19
@Author  : muzili
@File    : gen_verify_code
'''
import random


def gen_verify_code():
    verify_code = ""
    list = []
    index = 0
    num = 0
    while num < 6:
        x = random.choice(range(12))  # 对随机生成的字符进行随机排序
        if x < 4:
            list.append(chr(random.choice(range(10)) + 48))  # 随机生成一个字符0—9
        elif x < 8:
            list.append(chr(random.choice(range(65, 90))))  # 随机生成一个字符A—Z
        else:
            list.append(random.choice(chr(random.choice(range(97, 122)))))  # 随机生成一个字符a—z
        num += 1
    while index < 6:
        str1 = list[index]
        verify_code += str1
        index += 1
    return verify_code


if __name__ == '__main__':
    pass
