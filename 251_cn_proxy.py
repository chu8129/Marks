import urllib2
import re
import threading
import time
import random
from lxml import etree
import logging
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

proxy_urls=[]
for i in xrange(1,2):
	proxy_urls.append(r'http://www.cn-proxy.com')
logging.debug(proxy_urls[0])

proxy_list=[]

class proxy_get(threading.Thread):
	def __init__(self,proxy_url):
		threading.Thread.__init__(self)
		self.proxy_url=proxy_url
	def get_proxy(self):
		logging.debug('proxy target url: '+self.proxy_url)
		req=urllib2.urlopen(self.proxy_url)
		response_data=req.read()
		lxml_response=etree.HTML(response_data)
		proxys=lxml_response.xpath('//div[@class="table-container"]/table[@class="sortable"]/tbody/tr')
		for iproxy in proxys:
			ip=iproxy.xpath('td')[0].text
			port=iproxy.xpath('td')[1].text
			addr=iproxy.xpath('td')[2].text
			proxy=[ip,port,addr]
			logging.debug(ip+':'+port)
			proxy_list.append(proxy)
	def run(self):
		self.get_proxy()

check_proxy_list=[]
class proxy_check(threading.Thread):
	def __init__(self,proxy_list):
		threading.Thread.__init__(self)
		self.proxy_list=proxy_list
		self.timeout=5
		self.testurl2='http://1111.ip138.com/ic.asp'
		self.testurl='http://www.baidu.com'
		self.testStr='030173'
	def check_proxy(self):
		cookies=urllib2.HTTPCookieProcessor()
		for proxy in self.proxy_list:
			proxy_handler=urllib2.ProxyHandler({'http':r'http://%s:%s'%(proxy[0],proxy[1])})
			opener=urllib2.build_opener(proxy_handler)
#			opener.addheaders=[('User-agent', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')] 
			urllib2.install_opener(opener)
			t1=time.time()
			try:
				response=urllib2.urlopen(self.testurl2,timeout=self.timeout)
				response_data=response.read()
				time_used=time.time()-t1
				pos=response_data.find(self.testStr)
#				if pos>1 and response.code==200:
				if response.code==200:
					logging.debug(response_data)
					logging.debug(proxy[0]+':'+proxy[1])
					check_proxy_list.append((proxy[0],proxy[1],time_used))
				else:
					logging.debug(proxy[0]+' '+proxy[1]+' '+proxy[2]+': fail')
					continue
			except Exception,e:
				logging.debug(e.message)
				continue
	def run(self):
		self.check_proxy()	
def proxy(num):
	get_proxy_thread=[]
        for i in range(len(proxy_urls)):
                t=proxy_get(proxy_urls[i])
                get_proxy_thread.append(t)
        for i in range(len(get_proxy_thread)):
                get_proxy_thread[i].start()
        for i in range(len(get_proxy_thread)):
                get_proxy_thread[i].join()
        check_thread=[]
        for i in range(4):
                t=proxy_check(proxy_list[((len(proxy_list)+3)/4)*i:((len(proxy_list)+3)/4)*(i+1)])
                check_thread.append(t)
	logging.debug('check_thread length :%s'%len(check_thread))
        for i in range(len(check_thread)):
                check_thread[i].start()
        for i in range(len(check_thread)):
                check_thread[i].join()
	return check_proxy_list
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
