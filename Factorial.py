# -*- coding: UTF-8 -*-
import math
#python通过输入数字计算阶乘

# num = int(input("请输入一个正整数:"))
# begin = 1   #初始化
#
# # 判断输入
# if num < 0:
#     print('负数没有阶乘')
# elif num == 0:
#     print('0的阶乘为1')
# else:
#     for i in range(1, num + 1):
#         begin = begin * i
#     print('fainal: %d' %begin)

# -------------------------------------------------
# math库的方法
num = int(input("请输入一个数字："))
if num < 0:
    print("负数是没有阶乘的！")
else:
    print("{0} final {1}".format(num, math.factorial(num)))




