#coding:utf-8
import urllib2
import base64
import re
from lxml import etree
from multiprocessing.dummy import Pool
from urllib import unquote,quote
import logging
logging.basicConfig(level=logging.INFO,format='%(message)s',filename='server.log',filemode='w')
#logging.basicConfig(level=logging.INFO,format='%(message)s')
def get_info(url):
	logging.debug(url)
	try:
                response=urllib2.urlopen(url)
        except:
                response.code=404
	logging.debug(response.code)
	if response.code==200:
		lwebdata=etree.HTML(response.read().decode('utf-8'))
		title=lwebdata.xpath('//title/text()') and lwebdata.xpath('//title/text()')[0] or ''
		logging.debug(title)
		if title=='错误'.decode('utf8'):
			return 0
	else:
		try:
                        response=urllib2.urlopen(url)
                except:
                        response.code=404
		if response.code==200:
			lwebdata=etree.HTML(response.read().decode('utf-8'))
			title=lwebdata.xpath('//title/text()') and lwebdata.xpath('//title/text()')[0] or ''
			logging.debug(title)
			if title=='错误'.decode('utf8'):return 0
		else:
			return 0
	logging.debug('go into while ')
	while lwebdata.xpath('//div[@class="padappbody"]/div[@class="padtit1xia1"]/div/a[span[contains(text(),"%s")]]/@href'%('查看更多'.decode('utf8'))):
		url=re.findall('(http://.*?\.com)',url)[0]+lwebdata.xpath('//div[@class="padappbody"]/div[@class="padtit1xia1"]/div/a[span[contains(text(),"%s")]]/@href'%('查看更多'.decode('utf8')))[0]
		webdata=urllib2.urlopen(url).read().decode('utf-8')
		lwebdata=etree.HTML(webdata)
	logging.debug(' the last url:%s'%(url))
	app_platform=lwebdata.xpath('//div[@class="padsubsearch"]/div/span[@class="padlan" and not(@style)]')[0].text
	app_country=lwebdata.xpath('//div[@style="float:left; margin-left: 40px"]/span[@class="padlan" and not(@href) and not(@style)]') and lwebdata.xpath('//div[@style="float:left; margin-left: 40px"]/span[@class="padlan" and not(@href) and not(@style)]')[0].text or lwebdata.xpath('//a[@id="btn_countrys"]/text()')[0]
	app_category_title=lwebdata.xpath('//div[@class="padsearch"]/div[@class="padsubsearch" and @style="background: #F1F1F1; margin-top: -5px"]/div[@style="float: left; margin-left: 40px"]/span[@class="padlan" and not(@style)]')[0].text	
	app_cost=re.findall('(\d)\?',url)[0]
	apps=lwebdata.xpath('//div[@class="padappbody"]/div[@class="padtit1xia1"]/div')
	if apps:
		pass	
	else:
		return 0
	for app in apps:
		app_rank=app.xpath('a/@id') and (len(app.xpath('a/@id')[-1])>4 and app.xpath('a/@id')[-1][4:] or '') or ''
		app_name=app.xpath('span[@class="padhuang"]/a/@title') and app.xpath('span[@class="padhuang"]/a/@title')[0].strip() or ''
		app_link=app.xpath('span[@class="padhuang"]/a/@href') and app.xpath('span[@class="padhuang"]/a/@href')[0].strip() or ''
		app_company=unquote(app.xpath('span[@class="padlan1"]/a/@title') and app.xpath('span[@class="padlan1"]/a/@title')[0].strip() or '')
		app_rank_ud_info=app.xpath('span[@class="padlan1"]/text()') and app.xpath('span[@class="padlan1"]/text()')[0] or ''
		app_rank_ud=re.findall('(.*?)\d',app_rank_ud_info) and re.findall('(.*?)\d',app_rank_ud_info)[0] or ''
		app_rank_ud_num=re.findall('(\d+)',app_rank_ud_info) and re.findall('(\d+)',app_rank_ud_info)[0] or ''
		app_rank_c_rank=len(app.xpath('span[@class="padlan1"]/text()'))>1 and app.xpath('span[@class="padlan1"]/text()')[1] or ''
		app_rank_c=re.findall('(.*?)\d',app_rank_c_rank) and re.findall('(.*?)\d',app_rank_c_rank)[0] or ''
		app_rank_c_rank_num=re.findall('(\d+)',app_rank_c_rank) and re.findall('(\d+)',app_rank_c_rank)[0] or ''
		try:
                        app_info=urllib2.urlopen((re.findall('(http://.*?\.com)/',url) and re.findall('(http://.*?\.com)/',url)[0] or '')+app_link).read()
                except:
                        app_info=''
		l_app_info=etree.HTML(app_info)
		app_id=l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"AppID")]') and l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"AppID")]')[0].text.strip() or ''
		app_catogory=l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"%s")]/a'%('类型'.decode('utf8'))) and l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"%s")]/a'%('类型'.decode('utf8')))[0].text.strip() or ''
		app_update=l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"%s")]'%('更新'.decode('utf8'))) and l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"%s")]'%('更新'.decode('utf8')))[0].text.strip() or ''
		app_apk=l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"%s")]'%('大小'.decode('utf8'))) and l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"%s")]'%('大小'.decode('utf8')))[0].text.strip() or ''
		app_comment_times=l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"%s")]/a'%('评论'.decode('utf8'))) and l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"%s")]/a'%('评论'.decode('utf8')))[0].text.strip() or ''
		app_coment_core=len(l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd"]/div[@class="zhihd2"]/ul/li[@class="zhihdzi"]/span[contains(text(),"%s")]/a/img'%('评论'.decode('utf8'))))
		app_store_href=l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd1"]/a/@href') and l_app_info.xpath('//div[@id="ads"]/div[@class="zhihd1"]/a/@href')[0].strip() or ''
		app_id_d=re.findall('：(.*)'.decode('utf8'),app_id) and re.findall('：(.*)'.decode('utf8'),app_id)[0] or ''
		app_update_d=re.findall('：(.*)'.decode('utf8'),app_update) and re.findall('：(.*)'.decode('utf8'),app_update)[0] or ''
		app_apk_d=re.findall('：(.*)'.decode('utf8'),app_apk) and re.findall('：(.*)'.decode('utf8'),app_apk)[0] or ''
#		logging.info(app_company.decode('utf-8'))
#		logging.info('|%s|%s|%s'%(app_link,app_name,app_company))
		logging.info(('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|'%(app_platform,app_country,app_category_title,app_cost,app_rank,app_link,app_name,app_company.decode('utf-8'),app_rank_ud,app_rank_ud_num,app_rank_c,app_rank_c_rank_num,app_id_d,app_catogory,app_update_d,app_apk_d,app_comment_times,app_coment_core,app_store_href)).encode('utf8'))
	return 0
if __name__=='__main__':
#	get_info('http://sgp.ann9.com/33_11?p=0')
	urls=[]
	with open('countries.data','r') as rf:
#		for host in rf.readlines():
		for host in ['www.ann9.com']:
			for category in [33,21,12,20,5,1,2,3,4,6,7,8,9,34,10,11,13,14,15,16,17,18,19,22,35]:
				for cost in [1,2,3]:#1免费2付费3畅销5精品推荐-新品推荐6精品推荐-时下热门7精品推荐-付费9精品推荐-免费
#					for platform in [1,2]:
					for platform in [1]:#1是是ipphone2是ipad
						urls.append('http://%s/%s_%s%s?p=0'%(host.strip(),category,platform,cost))
	pools=Pool(8)
	pools.map(get_info,urls)
#	for url in urls:
#		get_info('http://www.ann9.com/2_11?p=0')	
##        get_info('http://www.ann9.com/2_11?p=0')
