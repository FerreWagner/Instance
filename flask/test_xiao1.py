
def parse_url(url):
    # 检查协议
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url

    #检查默认path
    #xxx.baidu.com/baike
    i = u.find('/')
    if i == -1:
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]

    #检查端口
    port_dict = {
        'http': 80,
        'https': 443,
    }
    #默认端口
    port = port_dict[protocol]
    if ':' in host:
        h = host.split(':')
        host = h[0]
        port = int(h[1])
    #return了一个tuple
    return protocol, host, port, path
