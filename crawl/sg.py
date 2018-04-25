import requests
import random
import time
from bs4 import BeautifulSoup


# 解析dom
def crawl_detail(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()

        html = r.text
    except:
        return " ERROR "

    comments = []
    soup = BeautifulSoup(html, 'lxml')

    texts = soup.find_all('tbody')

    # foreach
    for alexa in texts:
        comment = {}
        try:
            comment['title'] = alexa.find('a', attrs={'class' : 's xst'}).text.strip()
            comment['author'] = alexa.find('cite').text.strip()
            comments.append(comment)
        except:
            print('crawl wrong')

    # print(comments)
    # exit()
    return comments


# 保存数据至文件
def save_file(dict):
    file_name = ''
    for ran in range(1, 4):
        file_name = file_name + str(random.randint(0,9))
    file_name = 'sg_' + str(ran) + str(time.strftime("%Y-%m-%d")) + file_name + '.txt'
    with open(file_name, 'a+', encoding='utf-8') as sg_file:
        for comment in dict:
            sg_file.write('标题：{}\n'.format(comment['title']))
        print('file save success')
        sg_file.close()


def main(font_utl, end_url, deep):
    url_list = []
    for i in range(0, deep):
        url_list.append(font_url + str(i) + end_url)
    print('url parser success')

    # 循环写入数据
    for url in url_list:
        content = crawl_detail(url)
        save_file(content)
    print('All Success')


deep = 2
font_url = 'http://bbs.sgamer.com/forum-44-'
end_url  = '.html'
# 设置需要爬取的页码数量

if __name__ == '__main__':
    main(font_url, end_url, deep)
