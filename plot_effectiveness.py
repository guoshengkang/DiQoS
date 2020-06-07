#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

DCG_arr_n=np.loadtxt("results\\DCG_value_n.csv", delimiter=',')
Div_arr_n=np.loadtxt("results\\Div_value_n.csv", delimiter=',')
DCG_arr_d=np.loadtxt("results\\DCG_value_d.csv", delimiter=',')
Div_arr_d=np.loadtxt("results\\Div_value_d.csv", delimiter=',')
DCG_arr_k=np.loadtxt("results\\DCG_value_k.csv", delimiter=',')
Div_arr_k=np.loadtxt("results\\Div_value_k.csv", delimiter=',')
n_list=[1000,1200,1400,1600,1800,2000]	# number of service candidates
d_list=[3,4,5,6,7,8]					# QoS dimensions
k_list=[3,4,5,6,7,8]					# top-k

fig=plt.figure(figsize=(16, 9))

# Number of Candidate Services
ax1=fig.add_subplot(2,3,1)
ax1.plot(range(6), DCG_arr_n[0,:], "bo-", label='DSL-RS')
ax1.plot(range(6), DCG_arr_n[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(6), DCG_arr_n[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(6), DCG_arr_n[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(6), DCG_arr_n[4,:], "mD-", label='DiQoS')
ax1.legend(loc='best')
plt.xlabel("Number of Candidate Services($n$)\n(a) DCG Value vs. $n$")
plt.ylabel("DCG Value")
plt.xlim((0,5))
plt.xticks(range(6),["1000","1200","1400","1600","1800","2000"])
plt.grid(linestyle='-.')

# Number of QoS Dimensions
ax1=fig.add_subplot(2,3,2)
ax1.plot(range(6), DCG_arr_d[0,:], "bo-", label='DSL-RS')
ax1.plot(range(6), DCG_arr_d[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(6), DCG_arr_d[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(6), DCG_arr_d[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(6), DCG_arr_d[4,:], "mD-", label='DiQoS')
ax1.legend(loc='best')
plt.xlabel("Number of QoS Dimensions($d$)\n(a) DCG Value vs. $d$")
plt.ylabel("DCG Value")
plt.xlim((0,5))
plt.xticks(range(6),["3","4","5","6","7","8"])
plt.grid(linestyle='-.')

# Number of  Services to Recommend
ax1=fig.add_subplot(2,3,3)
ax1.plot(range(6), DCG_arr_k[0,:], "bo-", label='DSL-RS')
ax1.plot(range(6), DCG_arr_k[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(6), DCG_arr_k[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(6), DCG_arr_k[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(6), DCG_arr_k[4,:], "mD-", label='DiQoS')
ax1.legend(loc='best')
plt.xlabel("Number of Services to Recommend($k$)\n(a) DCG Value vs. $k$")
plt.ylabel("DCG Value")
plt.xlim((0,5))
plt.xticks(range(6),["3","4","5","6","7","8"])
plt.grid(linestyle='-.')
################################################################

# Number of Candidate Services
ax1=fig.add_subplot(2,3,4)
ax1.plot(range(6), Div_arr_n[0,:], "bo-", label='DSL-RS')
ax1.plot(range(6), Div_arr_n[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(6), Div_arr_n[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(6), Div_arr_n[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(6), Div_arr_n[4,:], "mD-", label='DiQoS')
ax1.legend(loc='best')
plt.xlabel("Number of Candidate Services($n$)\n(b) DCG Value vs. $n$")
plt.ylabel("Diversity")
plt.xlim((0,5))
plt.xticks(range(6),["1000","1200","1400","1600","1800","2000"])
plt.grid(linestyle='-.')

# Number of QoS Dimensions
ax1=fig.add_subplot(2,3,5)
ax1.plot(range(6), Div_arr_d[0,:], "bo-", label='DSL-RS')
ax1.plot(range(6), Div_arr_d[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(6), Div_arr_d[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(6), Div_arr_d[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(6), Div_arr_d[4,:], "mD-", label='DiQoS')
ax1.legend(loc='best')
plt.xlabel("Number of QoS Dimensions($d$)\n(b) DCG Value vs. $d$")
plt.ylabel("Diversity")
plt.xlim((0,5))
plt.xticks(range(6),["3","4","5","6","7","8"])
plt.grid(linestyle='-.')

# Number of  Services to Recommend
ax1=fig.add_subplot(2,3,6)
ax1.plot(range(6), Div_arr_k[0,:], "bo-", label='DSL-RS')
ax1.plot(range(6), Div_arr_k[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(6), Div_arr_k[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(6), Div_arr_k[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(6), Div_arr_k[4,:], "mD-", label='DiQoS')
ax1.legend(loc='best')
plt.xlabel("Number of Services to Recommend($k$)\n(b) DCG Value vs. $k$")
plt.ylabel("Diversity")
plt.xlim((0,5))
plt.xticks(range(6),["3","4","5","6","7","8"])
plt.grid(linestyle='-.')


plt.tight_layout() #设置默认的间距
plt.savefig('results/effectiveness.png', dpi=1000,bbox_inches='tight') #指定分辨率保存
plt.show()
