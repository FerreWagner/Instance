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

def change_name(dir, base_name, update_name):

    if base_name in os.path.split(dir)[1]:
        abs_name = os.path.abspath(dir)
        print(re.sub(base_name, update_name, abs_name))
        os.rename(abs_name, re.sub(base_name, update_name, abs_name))
    if os.path.isfile(dir):
        return

    list_dir = os.listdir(dir)
    for dire in list_dir:
        real_path = re.sub(r'\\', '/', os.path.join(dir, dire))
        # print(real_path)
        # exit()
        change_name(real_path, base_name, update_name)



change_name('D:/todo', '我', '123')


# a = 'asd123asd'
# b = re.sub('asd', '你', a)
# print(b)