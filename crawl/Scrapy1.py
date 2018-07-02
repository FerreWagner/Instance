# Engine从Spider处获得爬取请求(request)
# Engine将爬取请求转发给Scheduler，调度指挥进行下一步
# Engine从Scheduler出获得下一个要爬取的请求
# Engine将爬取请求通过中间件发给Downloader
# 爬取网页后后，downloader返回一个Response给engine
# Engine将受到的Response返回给spider处理
# Spider处理响应后，产生爬取项和新的请求给engine
# Engine将爬取项发送给ITEM PIPELINE（写出数据）
# Engine将会爬取请求再次发给Scheduler进行调度（下一个周期的爬取）

