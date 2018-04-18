# -*- coding: UTF-8 -*-

# 引入日历模块
import calendar

#输入指定年月
yy = int(input('year:'))
mm = int(input('mouth:'))

#显示日历
print(calendar.month(yy, mm))