clf;clear
% DCG vs. n
x=linspace(0,25,6);
y1=[2.16496306,2.17260786,2.19099916,2.25148941,2.13420917,2.20018954];
y2=[2.69126727,2.78622990,2.81063812,2.81063812,2.81063812,2.81063812];
y3=[2.07167787,2.05562600,1.88952002,1.73622696,2.06423866,1.99234667];
y4=[1.89657221,2.02900343,1.77063464,2.10313100,1.73307776,1.84609582];
y5=[2.53096217,2.35963945,2.25403682,2.60027762,2.60027762,2.60027762];
subplot(2,3,1)
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
xlabel('\fontname{Times New Roman}(a) DCG Value vs. \itn')
ylabel('\fontname{Times New Roman}DCG Value')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'1000','1200','1400','1600','1800','2000'}); 
% DCG vs. d
x=3:8;
y1=[2.63421678,2.10829382,2.16702783,1.73945049,1.49879319,1.51666022];
y2=[2.89802111,2.78622990,2.84229830,2.61286102,2.38595783,2.40775909];
y3=[2.54327931,2.08802448,1.85495521,1.52936836,1.29462345,1.32538338];
y4=[2.53706139,2.11620915,2.12148619,1.66255737,1.15868921,1.46042336];
y5=[2.56357755,2.35963945,2.49227630,2.02896618,2.04910203,2.04501124];
subplot(2,3,2)
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
xlabel('\fontname{Times New Roman}(a) DCG Value vs. \itd')
ylabel('\fontname{Times New Roman}DCG Value')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'3','4','5','6','7','8'}); 
% DCG vs. k
x=3:8;
y1=[1.61365886,1.98451699,2.17786357,2.46642935,2.71859381,2.87178507];
y2=[1.98991078,2.41032264,2.78622990,3.13161264,3.45255932,3.75081871];
y3=[1.70294518,2.00233535,1.79552531,2.17546397,2.55665184,2.70178946];
y4=[1.48163542,1.65495089,2.04054040,1.99594531,2.48433659,2.97260769];
y5=[1.79599593,1.98200685,2.35963945,2.70576816,3.02897215,3.33271436];
subplot(2,3,3)
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
xlabel('\fontname{Times New Roman}(a) DCG Value vs. \itk')
ylabel('\fontname{Times New Roman}DCG Value')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'3','4','5','6','7','8'}); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% DCG vs. n
x=linspace(0,25,6);
y1=[1.00000000,0.97647059,0.95555556,0.96000000,0.98000000,0.97000000];
y2=[0.71428571,0.76470588,0.72222222,0.80000000,0.80000000,0.80000000];
y3=[1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000];
y4=[1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000];
y5=[1.00000000,1.00000000,1.00000000,0.90000000,0.90000000,0.90000000];
Y=[y1;y2;y3;y4;y5];
Y=Y';
subplot(2,3,4)
b=bar(Y,'group');
hold on;
set(b(1),'facecolor','r')
set(b(2),'facecolor','b')
set(b(3),'facecolor','c')
set(b(4),'facecolor','g')
set(b(5),'facecolor','m')
grid on
xlabel('\fontname{Times New Roman}(b) Diversity vs. \itn')
ylabel('\fontname{Times New Roman}Diversity')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'1000','1200','1400','1600','1800','2000'}); 
% DCG vs. d
x=3:8;
y1=[0.96470588,0.98823529,0.91000000,0.80757576,0.74823529,0.67971014];
y2=[0.88235294,0.76470588,0.67500000,0.59090909,0.48235294,0.36714976];
y3=[1.00000000,1.00000000,1.00000000,0.98484848,0.89411765,0.90821256];
y4=[1.00000000,1.00000000,1.00000000,0.93939394,0.74117647,0.80193237];
y5=[1.00000000,1.00000000,1.00000000,0.96969697,0.85882353,0.84541063];
subplot(2,3,5)
Y=[y1;y2;y3;y4;y5];
Y=Y';
b=bar(Y,'group');
hold on;
set(b(1),'facecolor','r')
set(b(2),'facecolor','b')
set(b(3),'facecolor','c')
set(b(4),'facecolor','g')
set(b(5),'facecolor','m')
grid on
xlabel('\fontname{Times New Roman}(b) Diversity vs. \itd')
ylabel('\fontname{Times New Roman}Diversity')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'3','4','5','6','7','8'}); 
% DCG vs. k
x=3:8;
y1=[0.90588235,0.94117647,0.95294118,0.98823529,0.98823529,1.00000000];
y2=[0.76470588,0.76470588,0.76470588,0.76470588,0.76470588,0.76470588];
y3=[1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000];
y4=[1.00000000,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000];
y5=[0.88235294,1.00000000,1.00000000,1.00000000,1.00000000,1.00000000];
subplot(2,3,6)
Y=[y1;y2;y3;y4;y5];
Y=Y';
b=bar(Y,'group');
hold on;
set(b(1),'facecolor','r')
set(b(2),'facecolor','b')
set(b(3),'facecolor','c')
set(b(4),'facecolor','g')
set(b(5),'facecolor','m')
grid on
xlabel('\fontname{Times New Roman}(b) Diversity vs. \itk')
ylabel('\fontname{Times New Roman}Diversity')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'3','4','5','6','7','8'}); 


