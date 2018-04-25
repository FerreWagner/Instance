# cookie:_T_WM=549da2f7173cd8ac2d6324b3f1c52456; ALF=1527133753; SCF=Ar7LWwR2nmgJC4wry1oEYp127mJbbb7GKCTlqXpGhqT2BprmkajeWVSepUEujWWyDipzIDEe5Yx4CdI1ag-tDAw.; SUB=_2A2535DLIDeRhGeVG7FUZ8ibOwj2IHXVVJ16ArDV6PUJbktANLWuhkW1NT4SkMhsZN2tMGI61GQg_TdEM_K9gVf6i; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFh-spqyBu1XLjxdSZK2Bac5JpX5K-hUgL.FoeRS0MReonE1K22dJLoI7Us9PiE9-pf; SUHB=0QS55fyOz4Ka7q; SSOLoginState=1524646554; M_WEIBOCN_PARAMS=featurecode%3D20000320%26luicode%3D10000011%26lfid%3D1076035621509969


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

    texts = soup.find_all('div', attrs={'class' : 'c'})

    # foreach
    for alexa in texts:
        comment = {}
        try:
            comment['title']   = alexa.find('div', attrs={'class' : 'WB_text W_f14'}).text.strip()
            # comment['author']  = alexa.find('cite').text.strip()
            # comment['comment'] = alexa.find('td', attrs={'class' : 'num'}).find('a', attrs={'class' : 'xi2'}).text.strip()
            # comment['view']    = alexa.find('td', attrs={'class' : 'num'}).find('em').text.strip()
            # comment['cate']    = alexa.find('th', attrs={'class' : 'common'}).find('em').find('a').text.strip()
            comments.append(comment)
        except:
            print('crawl wrong')

    print(url)
    exit()
    return comments


# 保存数据至文件
def save_file(dict):
    file_name = ''
    for ran in range(1, 4):
        file_name = file_name + str(random.randint(0,9))
    file_name = 'sg_' + str(ran) + str(time.strftime("%Y-%m-%d")) + file_name + '.txt'
    with open(file_name, 'a+', encoding='utf-8') as sg_file:
        for comment in dict:
            sg_file.write('标题：{}\n作者：{}\n评论：{}\n浏览：{}\n\n'.format(comment['title'], comment['author'], comment['comment'], comment['view']))
        print('file save success')
        sg_file.close()


def main(url, deep):
    url_list = []
    for i in range(0, deep):
        url_list.append(url + str(deep))
    print('url parser success')

    # 循环写入数据
    for url in url_list:
        content = crawl_detail(url)
        save_file(content)
    print('All Success')


deep = 2
# url = 'https://weibo.cn/u/2274543693?page='
url = 'https://m.weibo.cn/u/2274543693?uid=2274543693&luicode=10000012&lfid=1005053877828291_-_FOLLOWERS&featurecode=20000320'
# end_url  = '#feedtop'
# 设置需要爬取的页码数量

if __name__ == '__main__':
    main(url, deep)
