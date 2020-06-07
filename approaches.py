#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-23 16:19:56
# @Author  : Guosheng Kang (guoshengkang@gmail.com)
# @Link    : https://guoshengkang.github.io
# @Version : $Id$

import os
import pickle
import random
from scipy import spatial
import numpy as np
import scipy.stats as stats
import math
from itertools import combinations
from sklearn.cluster import KMeans

def RS(Constraint=None,Candidates=None,top_k=None):
	row_num,col_nuw=Candidates.shape
	selected_nos=random.sample(range(row_num), top_k)
	return selected_nos

def KNN(Constraint=None,Candidates=None,top_k=None):
	row_num,col_nuw=Candidates.shape
	distances=[]
	for k in range(row_num):
		distance=spatial.distance.euclidean(Constraint,Candidates[k,:])
		distances.append(distance)
	distance_tuple=list(zip(range(row_num),distances))
	distance_tuple.sort(key=lambda x:x[1]) # reverse=True
	selected_nos=[x[0] for x in distance_tuple]
	return selected_nos[:top_k]

def DQCSR_CC(Constraint=None,Candidates=None,top_k=None):
	clf = KMeans(n_clusters=top_k)
	clf.fit(Candidates)
	centers = clf.cluster_centers_ # ndarray
	labels = clf.labels_   # 每个数据点所属分组 ndarray
	label_dict={}
	for index, class_no in enumerate(labels):
		temp_list=label_dict.get(class_no,[])
		temp_list.append(index)
		label_dict[class_no]=temp_list
	selected_nos=[]
	for class_no in range(top_k):
		distances=centers[class_no,:]-Candidates[label_dict[class_no],:]
		distances=(distances**2).sum(axis=1)
		distances=distances**(1/2)
		ranked_index=distances.argsort() # 升序排序,返回索引
		selected_service_no=label_dict[class_no][ranked_index[0]]
		selected_nos.append(selected_service_no)
	return selected_nos

def DQCSR_CR(Constraint=None,Candidates=None,top_k=None):
	clf = KMeans(n_clusters=top_k)
	clf.fit(Candidates)
	centers = clf.cluster_centers_ # ndarray
	labels = clf.labels_   # 每个数据点所属分组 ndarray
	label_dict={}
	for index, class_no in enumerate(labels):
		temp_list=label_dict.get(class_no,[])
		temp_list.append(index)
		label_dict[class_no]=temp_list
	selected_nos=[]
	for class_no in range(top_k):
		class_radius=[]
		for Si in label_dict[class_no]:
			Si_radius=[0]
			for Sj in label_dict[class_no]:
				if Si!=Sj:
					temp_radius=spatial.distance.euclidean(Candidates[Si,:],Candidates[Sj,:])
					Si_radius.append(temp_radius)
			max_Si_radius=max(Si_radius)
			class_radius.append(max_Si_radius)
		ranked_index=np.array(class_radius).argsort() # 升序排序,返回索引
		selected_nos.append(label_dict[class_no][ranked_index[0]])
	return selected_nos

def DiQoS(sn=None,Constraint=None,Candidates=None,top_k=None,lamda=0.5):
	results=[]
	K=len(sn["nodes"]) # 节点数量
	candidate_nos=list(range(K))
	for _ in range(top_k): # 迭代选择top_k个服务
		selected_no=candidate_nos[0]
		max_rank_score=(1-lamda)*sn["nodes"][selected_no]+lamda*diversity(sn=sn,resutls=results+[selected_no])
		for temp_no in candidate_nos[1:]:
			temp_rank_score=(1-lamda)*sn["nodes"][temp_no]+lamda*diversity(sn=sn,resutls=results+[temp_no])
			if temp_rank_score>max_rank_score:
				max_rank_score=temp_rank_score
				selected_no=temp_no
		candidate_nos.remove(selected_no)
		results.append(selected_no)
	return results

def A_dominates_B(A,B): # A and B must be np.array
	if all(A<=B) and any(A<B):
		isDominate=True
	else:
		isDominate=False
	return isDominate

def mapping(Constraint=None,Candidates=None):
	Candidates=abs(Candidates-Constraint)
	return Candidates

def Skyline(Candidates=None):
	row_num,col_nuw=Candidates.shape
	skyline_nos=[]
	for i in range(row_num):
		A=Candidates[i,:]
		dominated=True
		for j in range(row_num):
			B=Candidates[j,:]
			if i==j:
				continue
			if A_dominates_B(B,A):
				dominated=False
		if dominated:
			skyline_nos.append(i)
	return skyline_nos

def DCG(Constraint=None,items=None,alph=0.5):
	scores=[]
	DCG_value=0.0
	for one_row in items:
		tau, p_value = stats.kendalltau(Constraint, one_row)
		dis=spatial.distance.euclidean(Constraint,one_row)
		temp_score=alph*(1.0-dis/math.sqrt(2.0))+(1-alph)*tau
		scores.append(temp_score)
	for index,score in enumerate(scores):
		pi=index+1
		DCG_value=DCG_value+(2**score-1)/math.log2(1+pi)
	return DCG_value

def get_thresholds(Candidates=None,alph=0.5):
	# 计算欧氏距离,余弦相似度,QoS相似度
	sim_dict={}
	i=0;
	for Si,Sj in list(combinations(range(len(Candidates)), 2)):
		temp_krcc, p_value=stats.kendalltau(Candidates[Si,:],Candidates[Sj,:])
		temp_dis=spatial.distance.euclidean(Candidates[Si,:],Candidates[Sj,:])
		temp_sim=(1-alph)*(1.0-temp_dis/math.sqrt(2.0))+alph*temp_krcc
		sim_dict[(Si,Sj)]=temp_sim
		i=i+1
		if i%10000==0:
			print(i)
	# thresh_sim=np.mean(list(sim_dict.values())) # average QoS similarity
	sim_arr=np.array(list(sim_dict.values()))
	thresh_sim=np.percentile(sim_arr,80)
	return thresh_sim

def service_network(Constraint=None,Candidates=None,sim_threshold=None,alph=0.5):
	# 计算节点的score
	scores=[]
	for Candidate in Candidates: # compute similarity between Sr and Si
		tau, p_value = stats.kendalltau(Constraint, Candidate)
		dis=spatial.distance.euclidean(Constraint,Candidate)
		temp_score=alph*(1.0-dis/math.sqrt(2.0))+(1-alph)*tau
		scores.append(temp_score)
	# 计算欧氏距离，余弦距离 --> 计算QoS相似度 --> 构建服务网络图的边
	edges=[]
	for Si,Sj in list(combinations(range(len(Candidates)), 2)):
		temp_krcc, p_value =stats.kendalltau(Candidates[Si,:],Candidates[Sj,:])
		temp_dis=spatial.distance.euclidean(Candidates[Si,:],Candidates[Sj,:])
		temp_sim=(1-alph)*(1.0-temp_dis/math.sqrt(2.0))+alph*temp_krcc
		if temp_sim>=sim_threshold:
			edges.append((Si,Sj))
	sn={"nodes":scores,"edges":edges}
	return sn

def diversity(sn=None,resutls=None):
	K=len(sn["nodes"]) # 节点数量
	ES=set(resutls) # Expanded Set
	for service_no in resutls:
		for edge in sn["edges"]: # edge=(i,j)
			if service_no in edge:
				ES=ES|set(edge)
	ER=len(ES)/K 	# Expansion Ratio
	return ER


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
	DCG_arr=np.zeros((5,6))
	Div_arr=np.zeros((5,6))
	for index,n in enumerate(n_list):
	# for index,d in enumerate(d_list):
	# for index,top_k in enumerate(k_list):

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
		DCG_values=[]
		diversities=[]
		for time in range(10):
			results_RS=RS(Constraint=Sr,Candidates=skyline_serves,top_k=top_k)
			results=skyline_serves[results_RS,:]
			temp_DCG=DCG(Constraint=Sr,items=results,alph=0.5)
			temp_diversity=diversity(sn=sn,resutls=results_RS)
			DCG_values.append(temp_DCG)
			diversities.append(temp_diversity)
		DCG_value=np.mean(DCG_values)
		div=np.mean(diversities)
		DCG_arr[0,index]=DCG_value
		Div_arr[0,index]=div

		# (2)调用DSL_KNN方法
		results_KNN=KNN(Constraint=Sr,Candidates=skyline_serves,top_k=top_k)
		results=skyline_serves[results_KNN,:]
		DCG_value=DCG(Constraint=Sr,items=results,alph=0.5)
		div=diversity(sn=sn,resutls=results_KNN)
		DCG_arr[1,index]=DCG_value
		Div_arr[1,index]=div

		# (3)调用DQCSR_CC方法
		results_CC=DQCSR_CC(Constraint=Sr,Candidates=skyline_serves,top_k=top_k)
		results=skyline_serves[results_CC,:]
		DCG_value=DCG(Constraint=Sr,items=results,alph=0.5)
		div=diversity(sn=sn,resutls=results_CC)
		DCG_arr[2,index]=DCG_value
		Div_arr[2,index]=div

		# (4)调用DQCSR_CR方法
		results_CR=DQCSR_CR(Constraint=Sr,Candidates=skyline_serves,top_k=top_k)
		results=skyline_serves[results_CR,:]
		DCG_value=DCG(Constraint=Sr,items=results,alph=0.5)
		div=diversity(sn=sn,resutls=results_CR)
		DCG_arr[3,index]=DCG_value
		Div_arr[3,index]=div
		
		# (5)调用DiQoS方法
		results_DQ=DiQoS(sn=sn,Constraint=Sr,Candidates=skyline_serves,top_k=top_k,lamda=lamda)
		results=skyline_serves[results_DQ,:]
		DCG_value=DCG(Constraint=Sr,items=results,alph=0.5)
		div=diversity(sn=sn,resutls=results_DQ)
		DCG_arr[4,index]=DCG_value
		Div_arr[4,index]=div
	np.savetxt("DCG_value_n.csv",DCG_arr,delimiter=',',fmt='%.8f')
	np.savetxt("Div_value_n.csv",Div_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("DCG_value_d.csv",DCG_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("Div_value_d.csv",Div_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("DCG_value_k.csv",DCG_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("Div_value_k.csv",Div_arr,delimiter=',',fmt='%.8f')
	print(DCG_arr)
	print(Div_arr)
	