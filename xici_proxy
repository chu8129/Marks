import urllib2
import re
import threading
import time
import random
from lxml import etree
from multiprocessing.dummy import Pool 
import logging
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")
import Queue

proxy_urls=[]

for num in xrange(1,300):
	proxy_urls.append('http://www.xicidaili.com/nn/%s'%num)

proxy_list=[]

cqueue=Queue.Queue()

class get_proxy():
	global queue
	def get_proxy(self,proxy_url):
		logging.debug('proxy target url: '+proxy_url)
		try:
			response=urllib2.urlopen(urllib2.Request(url=proxy_url,headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Encoding":"gzip, deflate, sdch","Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4","Connection":"keep-alive","host":"www.xicidaili.com","User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"}))
		except Exception,e:
			logging.debug('fial,'+e.message)
			return
		response_data=response.read()
		lxml_response=etree.HTML(response_data)
		proxys=lxml_response.xpath('//table[@id="ip_list"]/tbody/tr')
		for iproxy in xrange(1,len(proxys)):
			ip=iproxy.xpath('td')[2].text
			port=iproxy.xpath('td')[3].text
			addr=iproxy.xpath('td')[5].text
			logging.debug(ip+':'+port+':'+addr)
			self.check_proxy(ip+':'+port)
		
	def __init__(self,proxy_url):
		self.timeout=5
		self.testurl2='http://1111.ip138.com/ic.asp'
		self.testurl='http://www.baidu.com'
		self.testStr='030173'
		self.get_proxy(proxy_url)
	
	def check_proxy(self,proxy):
		cookies=urllib2.HTTPCookieProcessor()
		proxy_handler=urllib2.ProxyHandler({'http':r'http://%s'%(proxy)})
		opener=urllib2.build_opener(cookies,proxy_handler)
		urllib2.install_opener(opener)
		try:
			response=urllib2.urlopen(self.testurl2,timeout=self.timeout)
			print response.code
			response_data=response.read()+response.headers
			if response.code==200:
				logging.debug('data: '+response_data)
				logging.debug(proxy+':pass')
				cqueue.put(proxy)
			else:
				logging.debug(proxy+':fail')
		except Exception,e:
			logging.debug(proxy+':fail')
			logging.debug(e.message)
def proxy(num):
#	get_proxy(proxy_urls[1])
	pool=Pool(num)
	pool.map(get_proxy,proxy_urls)
def get_page(url,proxylist,sleeptime=0,timeout=10):
	while True:
		try:
			proxy=proxylist.pop()
			break
		except:
			time.sleep(5)
	cookies=urllib2.HTTPCookieProcessor()
	proxy_handler=urllib2.ProxyHandler({'http':r'http://%s:%s'%(proxy[0],proxy[1])})
	opener=urllib2.build_opener(cookies,proxy_handler)
	opener.addheaders=[('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')]
	response=urllib2.urlopen(url,timeout=timeout)
	logging.debug(response.code)
	proxylist.append(proxy)
	time.sleep(sleeptime)
if __name__=='__main__':
	proxy(4)
