# -*- coding: utf-8 -*- 
 
 
#---------------------------------------  
#   程序：点点美女图片爬虫  
#   版本：1.0  
#   作者：zippera  
#   日期：2013-07-26  
#   语言：Python 2.7  
#--------------------------------------- 
 
import urllib2
import urllib
import re
 
 
 
pat = re.compile('<div class="feed-big-img">\n.*?imgsrc="(ht.*?)\".*?')
nexturl1 = "http://www.diandian.com/tag/%E7%BE%8E%E5%A5%B3?page="
 
 
count = 1
 
while count < 2:
 
    print "Page " + str(count) + "\n"
    myurl = nexturl1 + str(count)
    myres = urllib2.urlopen(myurl)
    mypage = myres.read()
    ucpage = mypage.decode("utf-8") #转码
 
    mat = pat.findall(ucpage)
    
 
    
    
    
    if len(mat):
        cnt = 1
        for item in mat:
            print "Page" + str(count) + " No." + str(cnt) + " url: " + item + "\n"
            cnt += 1
            fnp = re.compile('(\w{10}\.\w+)$')
            fnr = fnp.findall(item)
            if fnr:
                fname = fnr[0]
                urllib.urlretrieve(item, fname)
      	
    else:
        print "no data"
        
    count += 1
