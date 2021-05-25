'''

爬虫：抓取网页数据

需要引用urllib文件夹中的模块
'''
#简单获取某个页面html代码
import urllib.request as req
# response = req.urlopen("https://book.qidian.com/info/1026956528")
# html = response.read()
# #print(html) # 二进制数据
# html = html.decode("utf-8")
# print(html)

#抓取图片
#response = req.urlopen("https://bookcover.yuewen.com/qdbimg/349573/1026956528/180")
# data = response.read()
# #wb写入二进制数据到文件中
# with open("D:\\catch_img.jpg","wb") as f:
#     f.write(data)
#print(response.geturl()) # https://bookcover.yuewen.com/qdbimg/349573/1026956528/180
#print(response.getcode()) #200
#print(response.info())
'''
response.info()打印的结果：
Content-Type: image/jpeg
Access-Control-Allow-Origin: *
Timing-Allow-Origin: *
Accept-Ranges: bytes
Server: Lego Server
Date: Mon, 24 May 2021 09:18:27 GMT
X-Cache-Lookup: Cache Hit
Last-Modified: Thu, 01 Apr 2021 19:14:50 GMT
Content-Length: 14955
X-NWS-LOG-UUID: 1359270942599973698
Connection: close
X-Cache-Lookup: Hit From Inner Cluster
'''
#调用有道翻译的服务端接口操作（因有签名参数，没法调用成功）
import urllib.request as req
import urllib.parse as parse
import json
import time as t
# url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# data = {}
# data['i'] = '我爱学习'
# data['from'] = 'AUTO'
# data['to'] = 'AUTO'
# data['smartresult']='dict'
# data['client']='fanyideskweb'
#
# data['salt']='16219135421285'
# data['sign']='20699c6cf0221b9a606165580eef49ee'
# data['lts']='1621913542128'
# data['bv']='9ff8102373b1562471f4b6881a5653e9'
# data['doctype']='json'
# data['version']='2.1'
# data['keyfrom']='fanyi.web'
# data['action']='FY_BY_CLICKBUTTION'
# data = parse.urlencode(data).encode("utf-8")
# response = req.urlopen(url,data)
# html = response.read().decode('utf-8')
# print(html)

#调用百度翻译
url = "https://fanyi.baidu.com/sug"
data = {}
data['kw'] = 'hello'
data = parse.urlencode(data).encode("utf-8")
response = req.urlopen(url,data)
html = response.read().decode('unicode_escape')
print(html)
