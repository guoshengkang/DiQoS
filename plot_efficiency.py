#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

running_time_n=np.loadtxt("results\\running_time_n.csv", delimiter=',')
running_time_d=np.loadtxt("results\\running_time_d.csv", delimiter=',')
running_time_k=np.loadtxt("results\\running_time_k.csv", delimiter=',')
n_list=[1000,1200,1400,1600,1800,2000]	# number of service candidates
d_list=[3,4,5,6,7,8]					# QoS dimensions
k_list=[3,4,5,6,7,8]					# top-k

fig=plt.figure(figsize=(9, 4))

# Number of Candidate Services
ax1=fig.add_subplot(1,3,1)
ax1.plot(range(6),running_time_n[0,:], "bo-", label='DSL-RS')
ax1.plot(range(6),running_time_n[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(6),running_time_n[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(6),running_time_n[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(6),running_time_n[4,:], "mD-", label='DiQoS')
ax1.legend(loc='best')
plt.xlabel("Number of Candidate Services($n$)\n(a) Time vs. $n$")
plt.ylabel("Time(ms)")
plt.xlim((0,5))
plt.xticks(range(6),["1000","1200","1400","1600","1800","2000"])
plt.grid(linestyle='-.')

# Number of QoS Dimensions
ax1=fig.add_subplot(1,3,2)
ax1.plot(range(6),running_time_d[0,:], "bo-", label='DSL-RS')
ax1.plot(range(6),running_time_d[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(6),running_time_d[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(6),running_time_d[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(6),running_time_d[4,:], "mD-", label='DiQoS')
ax1.legend(loc='best')
plt.xlabel("Number of QoS Dimensions($d$)\n(b) Time vs. $d$")
plt.ylabel("Time(ms)")
plt.xlim((0,5))
plt.xticks(range(6),["3","4","5","6","7","8"])
plt.grid(linestyle='-.')

# Number of  Services to Recommend
ax1=fig.add_subplot(1,3,3)
ax1.plot(range(6),running_time_k[0,:], "bo-", label='DSL-RS')
ax1.plot(range(6),running_time_k[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(6),running_time_k[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(6),running_time_k[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(6),running_time_k[4,:], "mD-", label='DiQoS')
ax1.legend(loc='best')
plt.xlabel("Number of Services to Recommend($k$)\n(c) Time vs. $k$")
plt.ylabel("Time(ms)")
plt.xlim((0,5))
plt.xticks(range(6),["3","4","5","6","7","8"])
plt.grid(linestyle='-.')


plt.tight_layout() #设置默认的间距
plt.savefig('results/efficiency.png', dpi=1000,bbox_inches='tight') #指定分辨率保存
plt.show()
