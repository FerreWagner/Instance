# -*- coding: UTF-8 -*-

# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
# f(n) = f(n - 1) + f(n - 2); (n >= 2)

# 输入
inp = int(input('pls input num: '))

# 前两项
first  = 0
second = 1

# 项数初始化,起码为2项才满足斐波那契数列
num = 2

if inp <= 0:
    print('pls input positive integer')
elif inp == 1:
    print(first)
else:
    print(first, ",", second, end=" , ")
    while num < inp:
        fib = first + second
        print(fib, end=" , ")
        first  = second
        second = fib
        num += 1