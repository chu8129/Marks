#coding:utf-8
import urllib2,socket,logging,urllib,traceback
import lxml.etree as etree
logging.basicConfig(level=logging.DEBUG,
	format='%(asctime)s>>%(filename)s>>line:%(lineno)d>>%(levelname)s %(message)s',
	datefmt='%s,%d %b %Y:%H:%S',
	filemame='log',
	filemode='w')
def test_proxy(proxy,proxytype,url,headers='',timeout=10):
    req=urllib2.Request(url=url,headers=headers)
    req.set_proxy(proxy,proxytype)
    try:
    	html=urllib2.urlopen(req,timeout=timeout)
    	logging.info('{0} : {1}'.format('http code',html.code))
    	html_content=html.read()
    	return html_content
    except Exception,e:
    	traceback.print_exc()
    	logging.info('there were some wrong!!..')
def check_ip_ip138(html_content):
  try:
  	lxml_data=etree.HTML(html_content)
  	ip_info=lxml_data.xpath('//center/text()')
  	logging.info('\n{0}'.format(str(ip_info)))
  except Exception,e:
		traceback.print_exc()
   	
if __name__=='__main__':
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
	site=raw_input('plese import test site like http://1212.ip138.com/ic.asp\n') or 'http://1212.ip138.com/ic.asp'
	print 'test site :',site
	while True:			
			proxy=raw_input('plese import proxy like 127.0.0.1:8129\n') or '127.0.0.1:8129'
			proxytype=raw_input('plese import proxy type(http<default>,https)\n').lower() or 'http'
			check_ip_ip138(test_proxy(proxy,proxytype,site,headers))
			
			
			
#1、urllib
#urllib.urlopen(url,proxies={'http':'http://127.0.0.1:8580'})
#2、urllib2
#request = urllib2.Request(url)
#request.add_header('Range', 'bytes=%d-%d' %self.headerrange)
#request.set_proxy('127.0.0.1:8580','http')
#conn = urllib2.urlopen(request)
#3\
#proxy_handler = urllib2.ProxyHandler({"http" : 'http://192.168.0.101:3128'})
#opener = urllib2.build_opener(proxy_handler)
#urllib2.install_opener(opener)			