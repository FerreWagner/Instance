# 使用流程：http://www.naodongopen.com/942.html
# 安装工具 pip install myqr
# 命令行使用 myqr http:xxxx or 任何文字等
# myqr xxx -d 路径 -n 自定义图片名

#添加图片背景的二维码：参数后加-p
# myqr http://xxx -d C:\Users\Administrator\Downloads -c -n fkcu.png -p cat.png   #tips: -c表示真彩色，而不是黑白

# 若想使用动态二维码，加上gif文件即可,如：myqr http://www.naodongopen.com -c -p dog.gif

# 程序中使用该库
from MyQR import myqr
import os

words = 'love'

version, level, qr_name = myqr.run(
    words,
    version = 1,
    level = "H",
    picture = "C:\\Users\\Administrator\\xuge.jpg",
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name=None,
    save_dir=os.getcwd(),
)