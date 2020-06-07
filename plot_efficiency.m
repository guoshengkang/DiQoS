clf;clear
x=linspace(0,25,6);
y1=[0.00000000,0.09973049,0.00000000,0.09932518,0.00000000,0.10008812];
y2=[0.09970665,0.09973049,0.19943714,0.19953251,0.19955635,0.19910336];
y3=[19.04909611,18.55037212,18.85321140,18.35088730,18.74971390,18.94655228];
y4=[19.34821606,19.74718571,19.24483776,19.14885044,20.34559250,19.94655132];
y5=[0.99732876,2.09434032,2.19404697,3.28841209,3.29113007,3.29411030];
subplot(1,3,1)
plot(x,y1,'-rp','LineWidth',1.5,'MarkerFaceColor','r','MarkerSize',10)
hold on
plot(x,y2,'-bs','LineWidth',1.5,'MarkerFaceColor','b','MarkerSize',10)
hold on
plot(x,y3,'-co','LineWidth',1.5,'MarkerFaceColor','c','MarkerSize',10)
hold on
plot(x,y4,'-gd','LineWidth',1.5,'MarkerFaceColor','g','MarkerSize',10)
hold on
plot(x,y5,'-m^','LineWidth',1.5,'MarkerFaceColor','m','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(a) Time vs. \itn')
ylabel('\fontname{Times New Roman}Time(ms)')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'1000','1200','1400','1600','1800','2000'}); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x=3:8;
y1=[0.00000000,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000];
y2=[0.19671917,0.19638538,0.49555302,0.70095062,0.90034008,2.19392776];
y3=[19.15161610,18.65286827,20.84426880,23.33784103,24.93340969,31.81166649];
y4=[19.54479218,19.24569607,24.63693619,32.61280060,42.08767414,129.15754318];
y5=[2.19695568,1.99785233,16.75548553,42.48602390,63.13104630,136.54675007];
subplot(1,3,2)
plot(x,y1,'-rp','LineWidth',1.5,'MarkerFaceColor','r','MarkerSize',10)
hold on
plot(x,y2,'-bs','LineWidth',1.5,'MarkerFaceColor','b','MarkerSize',10)
hold on
plot(x,y3,'-co','LineWidth',1.5,'MarkerFaceColor','c','MarkerSize',10)
hold on
plot(x,y4,'-gd','LineWidth',1.5,'MarkerFaceColor','g','MarkerSize',10)
hold on
plot(x,y5,'-m^','LineWidth',1.5,'MarkerFaceColor','m','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(b) Time vs. \itd')
ylabel('\fontname{Times New Roman}Time(ms)')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'3','4','5','6','7','8'}); 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x=3:8;
y1=[0.09970665,0.00000000,0.00000000,0.00000000,0.00000000,0.00000000];
y2=[0.19948483,0.19943714,0.20253658,0.19938946,0.19943714,0.10037422];
y3=[14.25909996,16.85209274,18.94905567,21.83876038,23.93610477,26.02670193];
y4=[15.56091309,17.45612621,19.44510937,22.93870449,24.13535118,26.32949352];
y5=[0.89499950,1.39632225,1.99787617,2.69267559,3.39083672,4.08914089];
subplot(1,3,3)
plot(x,y1,'-rp','LineWidth',1.5,'MarkerFaceColor','r','MarkerSize',10)
hold on
plot(x,y2,'-bs','LineWidth',1.5,'MarkerFaceColor','b','MarkerSize',10)
hold on
plot(x,y3,'-co','LineWidth',1.5,'MarkerFaceColor','c','MarkerSize',10)
hold on
plot(x,y4,'-gd','LineWidth',1.5,'MarkerFaceColor','g','MarkerSize',10)
hold on
plot(x,y5,'-m^','LineWidth',1.5,'MarkerFaceColor','m','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(c) Time vs. \itk')
ylabel('\fontname{Times New Roman}Time(ms)')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'3','4','5','6','7','8'}); 


