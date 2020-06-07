This repository is the Python implementation with tensorflow 1.4.0 for the ICWS 2020 accepted paper:
> Guosheng Kang, Jianxun Liu, Buqing Cao, Yong Xiao. "Diversified QoS-Centric Service Recommendation for Uncertain QoS Preferences". IEEE International Conference on Services Computing. 2020, pp. \*\*-\*\*.

## Dataset
The experiments were conducted on a widely used public real-world dataset named QWS. This dataset can be accessed from [Zenodo website](https://zenodo.org/record/3557008#.XpmwmsgzaUn). The dataset contains 8-dimensional quality information on 2,507 real-world Web services, including latency, availability, etc.

## Data preprocessing
* **Code**: [data_preprocess.py](data_preprocess.py)
* **Input**: [qws2\\qws2.csv]([qws2/qws2.csv)
* **Output**: [QWS.pickle](QWS.pickle)
  
### Approaches (And Evaluate Effectiveness)
* **Code**: [approaches.py](approaches.py)
* **Input**: [QWS.pickle](QWS.pickle)
* **Output**:
  * [DCG_value_n.csv](DCG_value_n.csv)
  * [Div_value_n.csv](Div_value_n.csv)
  * [DCG_value_d.csv](DCG_value_d.csv)
  * [Div_value_d.csv](Div_value_d.csv)
  * [DCG_value_k.csv](DCG_value_k.csv)
  * [Div_value_k.csv](Div_value_k.csv)
  
* **Evaluate Efficiency**
  * **Code**: [evaluate_efficiency.py](evaluate_efficiency.py)
  * **Output**: [running_time_n.csv](running_time_n.csv), [running_time_d.csv](running_time_d.csv), [running_time_k.csv](running_time_k.csv)
  
* **Plot Figures for Effectiveness and Efficiency**
  * **Python Code**: [plot_effectiveness.py](plot_effectiveness.py),[plot_efficiency.py](plot_efficiency.py)
  * **Output**: [effectiveness.png](effectiveness.png),[efficiency.png](efficiency.png)
   * **Matlab Code**: [plot_effectiveness.m](plot_effectiveness.m),[plot_efficiency.m](plot_efficiency.m)
  * **Output**: [effectiveness.emf](effectiveness.emf),[efficiency.emf](efficiency.emf)

