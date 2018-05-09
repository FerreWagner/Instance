import os
import re

def search_file(dir,sname):            # 当sname为空时，打印当前目录所有文件
    if sname in os.path.split(dir)[1]: # 检验文件名里是否包含sname
        print(os.path.relpath(dir))    # 打印相对路径，相对指相对于当前路径
        # print(os.path.abspath(dir))    # 打印出绝对路径
    if os.path.isfile(dir):            # 如果传入的dir直接是一个文件目录 他就没有子目录，就不用再遍历它的子目录了
        return

    for dire in os.listdir(dir):                  # 遍历子目录  这里的dire为当前文件名
        search_file(os.path.join(dir,dire),sname) # jion一下就变成了当前文件的绝对路径
                                                  # 对每个子目录路劲执行同样的操作

# 修改特定文件名
def change_name(path, base_name, update_name):
    # 获取该目录下所有文件，存入列表中
    f = os.listdir(path)

    for i in f:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + i
        if base_name in oldname:
            newname = re.sub(base_name, update_name, oldname)
            os.rename(oldname, newname)

# 修改文件前缀
def change_first(path, new_name):
    f = os.listdir(path)

    for i in f:
        oldname = path + i
        newname = path + new_name + i
        os.rename(oldname, newname)


# 修改文件后缀
def change_suffix(path, old_suf, suf):
    f = os.listdir(path)

    for i in f:
        position = os.path.splitext(i)
        if position[1] == old_suf:
            newname = position[0] + suf
            os.rename(path + i, path + newname)


# change_name('D:/todo/', 'k', '你')
# change_first('D:/todo/', 'ferre_')
change_suffix('D:/todo/', '.rtf', '.txt')

