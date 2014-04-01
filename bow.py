#!/usr/bin/env python
#coding=utf-8
import os
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2
from sklearn import svm
from sklearn import cross_validation
ncluster = 6 #聚类数

########
#读入数据
root = '/Users/moxie/Documents/dat' #目录
dir1 = root + '/kl' #恐龙文件夹
dir2 = root + '/qc' #汽车文件夹

#kl数据读取
kl = [] #恐龙文件夹
inf_kl = [] #局部特征的个数
for i in range(95):
    pic = []
    f_name = '%s.txt' % i
    file1 = os.path.join(dir1,f_name)
    for line in open(file1,'rb'):
        localf = [] #每行
        for dms in line.strip().split():
            localf.append(float(dms))
        pic.append(localf) #每个图片
    inf = pic.pop(0)
    kl.extend(pic)
    count = int(inf[0])
    inf_kl.append(count)

#qc数据读取
qc = []
inf_qc = []
for i in range(95):
    pic = []
    f_name = '%s.txt' % i
    file2 = os.path.join(dir2,f_name)
    for line in open(file2,'rb'):
        localf = []
        for dms in line.strip().split():
            localf.append(float(dms))
        pic.append(localf)
    inf = pic.pop(0)
    qc.extend(pic)
    count = int(inf[0])
    inf_qc.append(count)
kl.extend(qc) #所有的局部特征
inf_kl.extend(inf_qc) #所有的特征数量信息
#print inf_kl,len(inf_kl)

#######
#kmeans 处理为 k 类，同时标记每个数据的所属类别，之后用；另外，均值就是代表点了；根据均值点建立词典。
features  = array(kl)
whitened = whiten(features) #scale一致化
cent,label = kmeans2(whitened,ncluster) #label 为每个局部特征所属类别

#######
#把每个图片表示为 bow 形式
#求 x
codebook = list(set(label))
x = []
begin = 0
label = list(label)
#print 'label:' , label
for n in inf_kl:
    end = begin + n
    temp =  label[begin:end]
    picf = [] #每个图片
    for ii in codebook:
        nn = temp.count(ii)
        picf.append(nn)
    x.append(picf)
    begin = end

#print len(x),len(picf)

#求 y
y = [0] * 95 + [1] * 95

#print x,y,len(x),len(y)

#######
#分开为 train 和 test

X_train, X_test, y_train, y_test = cross_validation.train_test_split(x, y, 
test_size=0.3, random_state=0)

#x_test = x[:32] + x[158:]
#x_train = x[32:158]
#y_test = y[:32] + y[158:]
#y_train = y[32:158]

#分类
clf = svm.SVC(kernel='linear', C=1)
clf.fit(X_train,y_train)
print '正确率为：',clf.score(X_test,y_test)

#正确率：0.982456140351