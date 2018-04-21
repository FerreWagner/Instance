# -*- coding: UTF-8 -*-

# 摄氏温标（C）和华氏温标（F）之间的换算关系为：F=C×1.8+32    C=(F-32)÷1.8
# Python 摄氏温度转华氏温度

tem = int(input('请输入温度:选1摄氏温度,或2华氏温度'))

while tem != 1 and tem != 2:
    tem = int(input('选择有误,请重新输入'))

if tem == 1:
    real_temp = float(input('输入摄氏温度:'))
    fina_temp = (real_temp*1.8) + 32    #计算华氏温度
    print('华氏温度为:%0.1f' %fina_temp)
else:
    real_temp = float(input('输入华氏温度:'))
    fina_temp = (real_temp - 32)/1.8    #计算摄氏温度
    print('设置温度为:%0.1f' %fina_temp)