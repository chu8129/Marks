sel.xpath('//div[@class="head"]/h1/text()').extract()
sel.xpath('//div[@class="head"]/h1/@href').extract()
sel.xpath('//div[@class="head" and @name]/h1/@href').extract()
brand="品牌"
sel.xpath('//div[@class="mall_goods_foursort_style_frame" and contains(text(),brand)]')[0].extract()
a.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"AppID")]')[0].text


创建
scrapy startproject tutorial
启动
scrapy crawl dmoz
启动保存
scrapy crawl dmoz -o items.json -t json
使用shell
scrapy shell url
返回的是response


contains中选择包括中文？
