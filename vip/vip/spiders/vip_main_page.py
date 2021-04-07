# -*- coding: utf-8 -*-
import scrapy
import json

from lxml import etree
import scrapy_splash
from vip.items import Item
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import Rule


lua_loadall = """
    function main(splash)
        splash.images_enabled = false
        splash:go(splash.args.url)
        splash:wait(2)
        splash:select('#J_main_nav_link'):mouse_hover()
        splash:wait(1)
        splash:select('#J_main_nav_category_menu > li.cate-menu-item'):mouse_hover()
        splash:wait(1)

        return splash:html()
    end

"""
lua_loadmultipage = """
    function main(splash)
        t = 3
        splash.images_enabled = false
        splash:go(splash.args.url)
        splash:wait(t)
        res = {}
        a = 1
        res[a]=splash:html()
        local s = splash:select("a.page-next-txt")
        while (s)
            do
            splash:select("a.page-next-txt"):mouse_click()
            splash:wait(t)
            a = a+1
            res[a] = splash:html()
            s = splash:select("a.page-next-txt")
            end
        return res
    end

"""


class VipMainPageSpider(scrapy.Spider):
    name = "vip-main-page"
    allowed_domains = ["www.vip.com", "list.vip.com"]
    start_urls = ("http://www.vip.com",)
    rules = (Rule(LinkExtractor(allow="autolist.html"), callback="parse_sub_category_goods_response"),)

    def parse(self, response):
        h5 = etree.HTML(response.body)

        main_category_list = h5.xpath('//li[@class="cate-menu-item J_main_nav_category_menu_item"]')
        for category_li in main_category_list:
            _id = category_li.xpath("@data-cateid")
            name = category_li.xpath("span/text()")
            self.logger.info("id:%s, name:%s", _id, name)

        self.logger.info("-----" * 30)

        category_list = h5.xpath("//dl//dd/a")
        self.logger.info("sub category list:%s", category_list)
        for category_cell in category_list:
            self.logger.debug(etree.tostring(category_cell))
            href = category_cell.xpath("@href")[0]
            name = category_cell.xpath("text()")[0]
            self.logger.info("href:%s, name:%s", href, name)
            yield scrapy_splash.SplashRequest(
                "http:" + href,
                meta={"category": name},
                endpoint="execute",
                args={"lua_source": lua_loadmultipage},
                cache_args=["lua_source"],
                callback=self.parse_goods,
            )

    def parse_goods(self, response):
        self.logger.info("%s", response.body[:100])
        meta = response.request.meta
        for index, html in json.loads(response.body).items():
            yield from self.parse_sub_category_goods(html, meta)

    def parse_sub_category_goods_on_response(self, response):
        yield from self.parse_sub_category_goods(response.body)

    def parse_sub_category_goods(self, html, meta={}):
        self.logger.info("html:%s", html[:1000])
        h5 = etree.HTML(html)
        goods = h5.xpath('//div[@class="c-goods-item  J-goods-item c-goods-item--auto-width"]')
        # self.logger.info("goods nums:%s, request:%s", len(goods), response.request.url)
        for good in goods:
            yield self.parse_goods_cell(good, meta)

    def parse_goods_cell(self, goods, meta):
        link = goods.xpath("./a/@href")
        name = goods.xpath('.//div[@class="c-goods-item__name  c-goods-item__name--two-line"]/text()')
        self.logger.info("%s", (name))
        self.logger.info("category:%s, name:%s, link:%s", meta["category"], name, link)
        item = Item()
        item["data"] = json.dumps(dict(category=meta.get("category", ""), name=name, link=link), ensure_ascii=False)
        self.logger.debug("item:%s", item["data"])
        return item

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy_splash.SplashRequest(
                url, meta={}, endpoint="execute", args={"lua_source": lua_loadall}, cache_args=["lua_source"]
            )
