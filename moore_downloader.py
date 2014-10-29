#coding=utf8

##日期：2014.10.29
##作者：moxie

import urllib2,urllib
import re
import threading
import os

prefix = 'http://www.autonlab.org/tutorials/'
pat = r'<LI><A HREF="(.*?)">'
pattern = re.compile(pat)

root = 'moore tutorials' + os.sep
if False == os.path.exists(root):
    os.mkdir(root)

page = urllib2.urlopen(prefix + 'list.html').read()
items = pattern.findall(page)
further_pages = [prefix + item for item in items]
tasks = []

def f_file_downloader(url):
    f_page = urllib2.urlopen(url).read()
    f_pat = r'<H3><A HREF="(.*?)">'
    f_pattern = re.compile(f_pat)
    f_items = f_pattern.findall(f_page)
    for f_item in f_items:
        f_url = prefix + f_item
        urllib.urlretrieve(f_url, os.path.join(root, f_item))

#for k in range(len(further_pages)):
 #   t = threading.Thread(target=f_file_downloader, args=(further_pages[k]))
  #  tasks.append(t)

for f_page in further_pages:
    t = threading.Thread(target=f_file_downloader, args=(f_page,))
    tasks.append(t)

for task in tasks:
    task.start()

for task in tasks:
    task.join(300)

