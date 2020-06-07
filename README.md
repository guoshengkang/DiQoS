This repository is the Python implementation for the ICWS 2020 accepted paper:
> Guosheng Kang, Jianxun Liu, Buqing Cao, Yong Xiao. "Diversified QoS-Centric Service Recommendation for Uncertain QoS Preferences". IEEE International Conference on Services Computing. 2020, pp. \*\*-\*\*.

## Dataset
The experiments were conducted on a widely used public real-world dataset named QWS [1]. This dataset can be accessed from [Zenodo website](https://zenodo.org/record/3557008#.XpmwmsgzaUn). The dataset contains 8-dimensional quality information on 2,507 real-world Web services, including latency, availability, etc.  
[1] E. Al-Masri, and Q. H. Mahmoud, “Investigating Web Services on the World Wide Web,” International Conference on World Wide Web, 2008, pp. 795-804.

## Data preprocessing
* **Code**: [data_preprocess.py](data_preprocess.py)
* **Input**: [qws2\\qws2.csv]([qws2/qws2.csv)
* **Output**: [QWS.pickle](QWS.pickle)
  
### Approaches (and Evaluate Effectiveness)
#### Comparing Approaches
We have implemented DiQoS and other four existing representative approaches.  
**DSL-RS**: This baseline approach randomly selects k services from S_DSL.  
**DSL-KNN** [2]: This approach models services recommendation as a k nearest neighbors problem. It selects k services from S_DSL that are most similar to s_r. This is the first attempt to solve the problem of personalized quality centric service recommendation.  
**DQCSR-CC** and **DQCSR-CR** [3]: These approaches first identify the S_DSL. Then the identified services are clustered with K-Means algorithm. DQCSR-CC selects a service from each cluster which is nearest to its cluster center, and DQCSR-CR selects a service from each cluster whose coverage region has the minimum radius. This is the first attempt to handle users’ uncertain quality correlation in service recommendation.  
[2] Y. Zhang, X. Ai, Q. He, X. Zhang, W. Dou, F. Chen, L. Chen, and Y. Yang, “Personalized Quality Centric Service Recommendation,” International Conference on Service-Oriented Computing, 2017, pp. 528-544.  
[3] Y. Zhang, L. Wu, Q. He, F. Chen, S. Deng, and Y. Yang, “Diversified Quality Centric Service Recommendation,” IEEE International Conference on Web Services, 2019, pp. 126-133.
#### Implementation
* **Code**: [approaches.py](approaches.py)

### Evaluation
#### Evaluate Effectiveness
* **Code**: [approaches.py](approaches.py)
* **Input**: [QWS.pickle](QWS.pickle)
* **Output**:
  * [DCG_value_n.csv](DCG_value_n.csv)
  * [Div_value_n.csv](Div_value_n.csv)
  * [DCG_value_d.csv](DCG_value_d.csv)
  * [Div_value_d.csv](Div_value_d.csv)
  * [DCG_value_k.csv](DCG_value_k.csv)
  * [Div_value_k.csv](Div_value_k.csv)
  
#### Evaluate Efficiency
  * **Code**: [evaluate_efficiency.py](evaluate_efficiency.py)
  * **Output**: [running_time_n.csv](running_time_n.csv), [running_time_d.csv](running_time_d.csv), [running_time_k.csv](running_time_k.csv)
  
#### Plot Figures for Effectiveness and Efficiency
  * **Python Code**: [plot_effectiveness.py](plot_effectiveness.py), [plot_efficiency.py](plot_efficiency.py)
  * **Output**: [effectiveness.png](effectiveness.png), [efficiency.png](efficiency.png)
   * **Matlab Code**: [plot_effectiveness.m](plot_effectiveness.m), [plot_efficiency.m](plot_efficiency.m)
  * **Output**: [effectiveness.emf](effectiveness.emf), [efficiency.emf](efficiency.emf)

