#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-23 16:19:56
# @Author  : Guosheng Kang (guoshengkang@gmail.com)
# @Link    : https://guoshengkang.github.io
# @Version : $Id$

import os
import random
import numpy as np
from approaches import *
from time import *

if __name__=='__main__':
	with open('QWS.pickle', 'rb') as f:
		Constraints = pickle.load(f)	# (6, 8)
		Candidates = pickle.load(f)		# (2501, 8)
	# sim_threshold=get_thresholds(Candidates=Candidates,alph=0.5)
	# print("sim_threshold:",sim_threshold)
	
	sim_threshold=0.7122835781845623 # 80%
	# sim_threshold = 0.5523330169011025	# mean
	
	# 参数变化
	n_list=[1000,1200,1400,1600,1800,2000]	# number of service candidates
	k_list=[3,4,5,6,7,8]					# top-k
	d_list=[3,4,5,6,7,8]					# QoS dimensions
	c_list=[0,1,2,3,4,5]					# QoS constraints
	# 默认参数
	n=1200
	top_k=5
	d=4
	c_k=1
	lamda=0.8
	
	# 参数变化结果
	efficiency_arr=np.zeros((5,6))
	# for index,n in enumerate(n_list):
	# for index,d in enumerate(d_list):
	for index,top_k in enumerate(k_list):

		Sr=Constraints[c_k,:d]
		Services=Candidates[:n,:d]

		# 计算 Dynamic Skyline Services
		mapped_Candidates=mapping(Constraint=Sr,Candidates=Services)
		skyline_nos=Skyline(Candidates=mapped_Candidates)
		skyline_serves=Services[skyline_nos,:]
		# print("number of skyline services:",len(skyline_serves))
		# 构建QoS相似服务网络
		sn=service_network(Constraint=Sr,Candidates=skyline_serves,sim_threshold=sim_threshold,alph=0.5)

		# 调用服务推荐方法
		##########################################################
		
		# (1)调用DSL_RS方法
		time_range=[]
		for _ in range(10):
			begin_time = time()
			results_RS=RS(Constraint=Sr,Candidates=skyline_serves,top_k=top_k)
			end_time = time()
			run_time = end_time-begin_time
			time_range.append(run_time)
		ave_time=np.mean(time_range)
		efficiency_arr[0,index]=ave_time

		# (2)调用DSL_KNN方法
		time_range=[]
		for _ in range(10):
			begin_time = time()
			results_KNN=KNN(Constraint=Sr,Candidates=skyline_serves,top_k=top_k)
			end_time = time()
			run_time = end_time-begin_time
			time_range.append(run_time)
		ave_time=np.mean(time_range)
		efficiency_arr[1,index]=ave_time

		# (3)调用DQCSR_CC方法
		time_range=[]
		for _ in range(10):
			begin_time = time()
			results_CC=DQCSR_CC(Constraint=Sr,Candidates=skyline_serves,top_k=top_k)
			end_time = time()
			run_time = end_time-begin_time
			time_range.append(run_time)
		ave_time=np.mean(time_range)
		efficiency_arr[2,index]=ave_time

		# (4)调用DQCSR_CR方法	
		time_range=[]
		for _ in range(10):
			begin_time = time()
			results_CR=DQCSR_CR(Constraint=Sr,Candidates=skyline_serves,top_k=top_k)
			end_time = time()
			run_time = end_time-begin_time
			time_range.append(run_time)
		ave_time=np.mean(time_range)
		efficiency_arr[3,index]=ave_time

		# (5)调用DiQoS方法
		time_range=[]
		for _ in range(10):
			begin_time = time()
			results_DQ=DiQoS(sn=sn,Constraint=Sr,Candidates=skyline_serves,top_k=top_k,lamda=lamda)
			end_time = time()
			run_time = end_time-begin_time
			time_range.append(run_time)
		ave_time=np.mean(time_range)
		efficiency_arr[4,index]=ave_time

	efficiency_arr=efficiency_arr*1000

	# np.savetxt("results\\running_time_n.csv",efficiency_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("results\\running_time_d.csv",efficiency_arr,delimiter=',',fmt='%.8f')
	np.savetxt("results\\running_time_k.csv",efficiency_arr,delimiter=',',fmt='%.8f')
	
	print(efficiency_arr)
	