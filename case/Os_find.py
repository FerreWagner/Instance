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

    f = os.listdir(dir)

    n = 0
    for i in f:
        abs_name = os.path.abspath(dir)
        if base_name in os.path.split(dir)[1]:
            os.rename(abs_name, re.sub(base_name, update_name, abs_name))
            print(base_name, '======>', update_name)
            n += 1

    # if base_name in os.path.split(dir)[1]:
    #     abs_name = os.path.abspath(dir)
    #     # print(re.sub(base_name, update_name, abs_name))
    #     os.rename(abs_name, re.sub(base_name, update_name, abs_name))
    # if os.path.isfile(dir):
    #     return
    #
    # list_dir = os.listdir(dir)
    # for dire in list_dir:
    #     # real_path = re.sub(r'\\', '/', os.path.join(dir, dire))
    #     # print(real_path)
    #     # exit()
    #     change_name(os.path.join(dir, dire), base_name, update_name)


def change_new(path, base_name, update_name):
    # 获取该目录下所有文件，存入列表中
    f = os.listdir(path)

    n = 0
    for i in f:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + f[n]
        if base_name in oldname:
            newname = re.sub(base_name, update_name, oldname)
            os.rename(oldname, newname)

        # print(oldname)
        # exit()
        # # 设置新文件名
        # newname = path + 'a' + str(n + 1) + '.JPG'
        #
        # # 用os模块中的rename方法对文件改名
        # os.rename(oldname, newname)
        # print(oldname, '======>', newname)

        n += 1

change_new('D:/todo/', 'a', 'flask_')

# change_name('D:/todo/', '我', 'ddd')

