# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError
import urllib.request
import socket
import random
import time
from bs4 import BeautifulSoup

from app import app


engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'


@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')
		
@engine.define
def hellowrld():
	print('hellowrld22222')
	return 'hellowrld return'
		
@engine.define
def visitAddress():
	User_Agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
			'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
			'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
			'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
			'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
			'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
			]
	shareUrl = ['http://t.cn/Rfo1g82',
	'http://t.cn/RfztMs8'
	]
	ipUrl = 'http://api.xicidaili.com/free2016.txt'
	req = urllib.request.Request(ipUrl)
	res = urllib.request.urlopen(req).read()

	soup = BeautifulSoup(res , 'html.parser')
	ips = soup.find_all('pre')
	ippp = '\n'.join(soup.prettify().split()) + '\n'

	socket.setdefaulttimeout(3)
	lines = ippp.split('\n')
	proxys = []
	for i in range(0,len(lines)):
		ip = lines[i]
		proxy_host = "http://" + ip
		proxys.append(proxy_host)
		
	#url = "http://t.cn/RfztMs8"
	for i in range(0 , len(shareUrl)):
		count = 0
		for proxy in proxys:
			try:
				if count >=5:
					break
				proxy_support=urllib.request.ProxyHandler({'http':proxy})
				opener = urllib.request.build_opener(proxy_support)
				random_userAget = random.choice(User_Agent)
				req = urllib.request.Request(shareUrl[i])
				req.add_header("User-Agent", random_userAget) 
				res = urllib.request.urlopen(req).read().decode("utf8")	
				count = count + 1
				time.sleep(random.randint(1, 10))	#random sleep
				print (count)
				print (res)
			except Exception as e:
				print (proxy)
				print (e)
				if count >= 5:
					break
				else:
					continue
