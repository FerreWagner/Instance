import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='heater', charset='utf8')

cursor = conn.cursor()
effect_row = cursor.execute("insert into heater_link(name, url, sort) values('过分了', '111', '2');")

#获取查询结果的第一条数据，返回的是一个元祖
row_1 = cursor.execute("select * from heater_link")

row_2 = cursor.fetchone()

row_3 = cursor.fetchmany(3)

row_4 = cursor.fetchall()

print(row_1)
print(row_2)
print(row_3)
print(row_4)

#提交，不然无法保存新建或修改的数据
conn.commit()

#获取最新自增id
new_id = cursor.lastrowid
print(new_id)

#关闭游标
cursor.close()
#关闭数据库连接
conn.close()
