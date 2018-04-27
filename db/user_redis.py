import redis

r = redis.Redis(host='127.0.0.1', port=6379)  # 指定连接redis的端口和ip以及哪个数据库
r.set('name', 'value')  # set string类型的值
r.setnx('name2', 'value')  # 设置的name的值，如果name不存在的时候才会设置
r.setex('name3', 'value', 3)  # 设置的name的值，和超时时间，过了时间key就会自动失效
r.mset(k1='v1', k2='v2')  # 批量设置值
r.get('name')  # 获取值
print(r.mget('k1', 'k2'))  # 批量获取key

r.delete('name')  # 删除值
r.delete('k1', 'k2')  # 批量删除
# ======下面是操作哈希类型的
r.hset('hname', 'key', 'value')  # set 哈希类型的值
r.hset('hname', 'key1', 'value2')  # set 哈希类型的值
r.hsetnx('hname', 'key2', 'value23')  # 给name为hname设置key和value，和上面的不同的是key不存在的时候
# 才会set
r.hmset('hname', {'k1': 'v1', 'k2': 'v2'})  # 批量设置哈希类型的key和value
r.hget('name', 'key')  # 获取哈希类型的值
print(r.hgetall('hname'))  # 获取这个name里所有的key和value
r.hdel('hname', 'key')  # 删除哈希类型的name里面指定的值
print(r.keys())  # 获取所有的key