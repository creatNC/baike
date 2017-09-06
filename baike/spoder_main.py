#!/usr/bin/python env
# -*- coding: utf-8 -*-
from baike import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDown()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_urls():
            try:
                new_url = self.urls.get_new_url()
                if new_url == "https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91%EF%BC%9A%E9%94%81%E5%AE%9A%E8%AF%8D%E6%9D%A1":
                    continue
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 100:
                    break
                count = count + 1
            except:
                print("craw faile")

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/%E5%AE%9D%E9%A9%AC/34549"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url) 