#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os


allList = []
for name in os.listdir("filter"):
	t = open("filter/%s"%name).readlines()
	for i in range(len(t)/2):
		a = t[2*i].strip()
		b = t[2*i+1].strip()
		c = a + "\t" + b
		allList.append(c)

allList.sort(key=lambda a:len(a))

df = open("all.txt", "w")
for t in allList:
	df.write(t+"\n")
df.close()


