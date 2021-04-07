# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class VipSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class VipDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers["User-Agent"] = ua.random + "\u200b\u200c\u200d" + ""


from twisted.internet import reactor
from twisted.internet.defer import Deferred


class DelayedRequestsMiddleware(object):
    def process_request(self, request, spider):
        delay_s = request.meta.get("delay_request_by", None)
        if not delay_s:
            delay_s = 0.1
        deferred = Deferred()
        reactor.callLater(delay_s, deferred.callback, None)
        return deferred


class AddProxyAddrMiddleware(object):
    def process_request(self, request, spider):
        ip = (
            str(random.choice(list(range(255))))
            + "."
            + str(random.choice(list(range(255))))
            + "."
            + str(random.choice(list(range(255))))
            + "."
            + str(random.choice(list(range(255))))
        )
        """
            {
            'Host': ,
            'User-Agent': ,
            'server-addr': '',
            'remote_user': '',
            'X-Client-IP': ip,
            'X-Remote-IP': ip,
            'X-Remote-Addr': ip,
            'X-Originating-IP': ip,
            'x-forwarded-for': ip,
            'Origin': 'http://www.baidu.com' ,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://www.baidu.com/",
            'Content-Length': '0',
            "Connection": "keep-alive"
        """
        request.headers["X-Remote-IP"] = ip
        request.headers["X-Client-IP"] = ip
        request.headers["X-Remote-Addr"] = ip
        request.headers["x-forwarded-for"] = ip
