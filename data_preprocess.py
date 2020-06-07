#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-21 11:11:08
# @Author  : Guosheng Kang (guoshengkang@gmail.com)
# @Link    : https://guoshengkang.github.io
# @Version : $Id$
import os
import numpy as np
import pandas as pd
import random
import pickle

home_path = os.path.dirname(os.path.abspath(__file__))
QWS_file_path = os.path.join(home_path, 'qws2\\qws2.csv')
df=pd.read_csv(QWS_file_path)
arr=np.array(df.ix[:,:8])
## (1) Response Time	-
## (2) Availability		+
## (3) Throughput		+
## (4) Successability	+
## (5) Reliability		+
## (6) Compliance		+
## (7) Best Practices	+
## (8) Latency			-		
row_num,col_nuw=arr.shape
print("数据集的维度:",row_num,"X",col_nuw)
colmax=arr.max(axis=0) # 每列的最大值
colmin=arr.min(axis=0) # 每列的最大值
print("每列的最大值:",colmax)
print("每列的最小值:",colmin)
neg_or_pos=['-','+','+','+','+','+','+','-'] # 正负属性
for k,att in enumerate(neg_or_pos): # 全部转化成负属性
	if att=='-':
		arr[:,k]=(arr[:,k]-colmin[k])/(colmax[k]-colmin[k])
	else:
		arr[:,k]=(colmax[k]-arr[:,k])/(colmax[k]-colmin[k])

Constriant_nos=random.sample(range(row_num), 6)
Constriants=arr[Constriant_nos,:]
print("QoS constraints:")
print(Constriants.shape)
Candidates=np.delete(arr,Constriant_nos,axis=0) # 删除数组的行
print("Service candidates:")
print(Candidates.shape)

# 保存
with open('results\\QWS.pickle', 'wb') as f:
	pickle.dump(Constriants, f)  # QoS Constraints
	pickle.dump(Candidates, f)   # QoS of Web service candidates