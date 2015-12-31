#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
import urllib2
from bs4 import BeautifulSoup


def html(url):
	return urllib2.urlopen(url).read()

def init():
	return ["151","hunian","tunian","longnian","shenian","manian","yangnian","hounian","jinian","gounian","zhunian","shunian","zongheshengxiao"]


visited = set()
stack = init()

while 1:
	if len(stack) == 0:
		break
	seed = stack.pop()
	if seed in visited:
		continue
	visited.add(seed)

	url = "http://www.duiduilian.com/chunlian/%s.html"%seed
	code = html(url).replace("&nbsp;", " ")
	soup = BeautifulSoup(code, 'html.parser')
	text = soup.find("div", "contentF").get_text().strip()
	df = open("raw/%s.txt"%seed, "w")
	for t in text.split("\n"):
		df.write(t.strip()+"\n")
	df.close()

	for t in soup.find(id="pages").find_all("a"):
		key = t["href"].split("/")[1].split(".")[0]
		if key not in visited:
			stack.append(key)
