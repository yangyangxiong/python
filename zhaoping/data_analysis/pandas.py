import pandas as pd  #数据框操作
import matplotlib.pyplot as plt #绘图
import matplotlib as mpl #配置字体
mpl.rcParams['font.sans-serif'] = ['SimHei'] #这个是绘图格式，不写这个的话横坐标无法变成我们要的内容
#配置绘图风格
plt.rcParams['axes.labelsize'] = 8.
plt.rcParams['xtick.labelsize'] = 12.
plt.rcParams['ytick.labelsize'] = 12.
plt.rcParams['legend.fontsize'] =10.
plt.rcParams['figure.figsize'] = [8.,8.]
data = pd.read_excel(r'D:\\practice\\zhaoping\\lagou2.xlsx',encoding='gbk')
data['经验要求'].value_counts().plot(kind='barh')  #绘制条形图
plt.show   #显示图片
data['工作地点'].value_counts().plot(kind='pie',autopct='%1.2f%%',explode=np.linspace(0,1.5,32))
plt.show   #显示图片
