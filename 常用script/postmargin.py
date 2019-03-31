#coding=utf-8
import requests
import base64

url='http://localhost/ctf/5/?rnd=1123241'
user_agent='Mozilla/5.0(WindowsNT6.3;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/45.0.2454.101Safari/537.36'
headers=("user-agent",user_agent)
s=requests.Session()
result=s.get(url).headers['flag']
print(result)
flag=base64.b64decode(result)[-12:] #从后开始截取12位
flag=base64.b64decode(flag)
print(flag)
data={'margin':flag}
r=s.post(url,data=data)
print(r.content)
