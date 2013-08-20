#coding=utf8

##版本：1.0
##环境：python2.7
##作者：moxie
##日期：2013.08.20

import urllib2
import re
import threading
import sys

url = 'http://www.v2ex.com'
prefix = 'http://www.v2ex.com/recent?p='
allitems = []
pat = r'<a href="(.*?)" class="count_livid">(.*?)</a>'
pattern = re.compile(pat)
#页面详细信息的正则表达式
pat_info = r'<a href="/go.*?>(.*?)<.*?<h1>(.*?)<.*?>(.*?)<'
pattern_info = re.compile(pat_info,re.S)

#首页需要单独访问
page = urllib2.urlopen(url).read()
items = pattern.findall(page)
#for it in items:#保存到data.dat中
#    f = open('data.dat','a')
#    f.write(str(it)+ ' ')
allitems.extend(items)


def finditem(i):
    page = urllib2.urlopen(prefix + str(i)).read()
    items = pattern.findall(page)
#    for it in items:
#        f = open('data.dat','a')
#        f.write(str(it)+' ')
    lock = threading.Lock()
    lock.acquire()
    allitems.extend(items)
#    print str(len(allitems)) + ' '
    lock.release()

pool = 20#同时开启的线程数
last = 100#要统计的页数


def dlpool(n):
    tasks = []#要每次重新清零，否则报错，start once
    for i in range(n,pool+n):
        try:
            t = threading.Thread(target=finditem,args=(i,))
            tasks.append(t)
        except:
            print 'some error in %sth page' % i
            continue
    for task in tasks:
        task.start()
     
    for task in tasks:
        task.join(300)
    return 0
for n in range(1,last,pool):
# 实时显示进度
    sys.stdout.write("\r%s-%s of %s" % (str(n),str(n+pool-1),str(last)))
    sys.stdout.flush()
    dlpool(n)
sys.stdout.write("\rdone                  \n")
sys.stdout.flush()
#f.close()
#uitems = list(set(allitems))
uitems = allitems#去重
sorteditems = sorted(uitems,key = lambda x: int(x[1]),reverse=True)

#for item in items:
#    if item not in allitems:
#        allitems.append(item)

#帖子页面的详细信息
def info(infourl):
    return pattern_info.search(urllib2.urlopen(infourl).read())

print 'All %s pages    %s items    Top10 is:' % (str(last),str(len(sorteditems)))


for i in range(10):
    itm = sorteditems[i]
    print url + itm[0],itm[1]
#    result = info(url + itm[0])
#    for k in range(3):
#        print result.group(k+1)


