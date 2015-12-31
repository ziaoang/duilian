#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import re
from collections import defaultdict

def zhongshu(arr):
	cnt = defaultdict(int)
	for t in arr:
		cnt[t] += 1
	a = []
	for t in cnt:
		a.append([t, cnt[t]])
	a.sort(key=lambda c:c[1], reverse=True)
	if len(a) >= 2 and a[0][1] == a[1][1]:
		print("err")
		exit()
	return a[0][0]


for name in os.listdir("manual"):
	length = []
	for line in open("manual/%s"%name):
		t = line.strip()
		if len(t) != 0:
			length.append(len(t))
	length.sort()
	most = zhongshu(length)
	if length[0] != most:
		print("err")
		exit()
	limit = length[0]
	df = open("filter/%s"%name, "w")
	for line in open("manual/%s"%name):
		t = line.strip()
		if len(t) != 0:
			df.write(t[:limit].replace("，","\n")+"\n")
	df.close()

