#! /usr/bin/PYTHON3
#coding = utf-8

''' 
Author:
Data:
HTD:
'''
import requests
import re

url = 'http://localhost/ctf/6/?rnd=12312421'
s = requests.Session()
r = s.get(url)
math = re.search(r'^<div>(.*)=\?;</div>$',r.text,re.M | re.S).group(1)
p = int(eval(math))
print(p)
d = {"value":p}
r = s.post(url,data=d)
if r.status_code == 200:
    print(r.status_code)
else:
    print('ERRER PAGE')
print(r.text)


