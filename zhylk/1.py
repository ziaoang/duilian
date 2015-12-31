#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
import urllib2
from bs4 import BeautifulSoup


def html(url):
	return urllib2.urlopen(url).read()

max_id = 53398

all = ""

errlist = set([8873, 50288, 51214])

for id in range(51001, max_id+1):
	print(id)
	if id in errlist:
		continue
	url = "http://www.zhgc.com/ylck/p_asp/sm.asp?id=%d"%id
	code = html(url).decode("gbk")
	soup = BeautifulSoup(code, 'html.parser')
	text = soup.find("td", "p14").get_text().strip()
	t = text.split("\n")
	if len(t) >= 2:
		all += "%s\n%s\n"%(t[0].strip(), t[1].strip())
	if id % 1000 == 0:
		df = open("raw/%d.txt"%id, "w")
		df.write(all)
		df.close()
		all = ""
