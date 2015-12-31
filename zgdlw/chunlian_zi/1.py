#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
import urllib2
import HTMLParser
from bs4 import BeautifulSoup



def f(html):
	html_parser = HTMLParser.HTMLParser()
	return html_parser.unescape(html)

def html(url):
	return urllib2.urlopen(url).read()

def init():
	a = []
	for i in range(4, 32):
		a.append(i)
	a += [35,37,38,47,49,53,125]
	return ["%dzi"%t for t in a]

def isContent(string):
	a = re.findall("[0-9]+", string)
	if len(a) == 0:
		return True
	return False

def extractSeed(string):
	a = re.findall("[0-9]+zi_[0-9]+.html", string)
	return [t.split(".")[0] for t in a]


visited = set()
stack = init()

while 1:
	if len(stack) == 0:
		break
	seed = stack.pop()
	visited.add(seed)
	url = "http://www.duiduilian.com/chunlian/%s.html"%seed
	code = html(url).replace("&nbsp;", " ")
	for s in extractSeed(code):
		if s not in visited:
			stack.append(s)
	soup = BeautifulSoup(code, 'html.parser')
	text = soup.find("div", "contentF").get_text().strip()
	if isContent(text):
		df = open("raw/%s.txt"%seed, "w")
		for t in text.split("\n"):
			df.write(t.strip()+"\n")
		df.close()
