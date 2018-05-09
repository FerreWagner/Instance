import os

# 文件基本属性
def file_attr(file_name):
    if os.path.isfile(file_name):
        content = os.stat(file_name)
        print('文件大小为：', content.st_size)
        print('上次访问时间：', content.st_atime)
        print('最后修改时间：', content.st_mtime)
    else:
        print('不是一个文件路径')
    # for i in f:
    #     print(i)
    #     if os.path.isdir(i) == True:
    #         print('shit')
    #     else:
    #         print('good')

    # print(os.stat(path))

file_attr('D:/todo/123.txt')