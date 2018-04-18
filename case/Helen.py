# -*- coding: UTF-8 -*-

# 海伦公式计算三角形面积

a = float(input('输入三角形第1边长:'))
b = float(input('输入三角形第2边长:'))
c = float(input('输入三角形第3边长:'))

#半周长
p = (a + b + c)/2

#面积
area = (p*(p - a)*(p - b)*(p - c))**0.5

print('area: %0.2f' %area)