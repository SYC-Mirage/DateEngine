import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.pyplot as plt

# 读取车辆数据
car_info = pd.read_csv('CarPrice_Assignment.csv')

# 将数据标签取出，并去除无用标签car_ID和CarName
labels = []
for i in car_info.columns:
    labels.append(i)
labels.remove('car_ID')
labels.remove('CarName')

# 创建分类用数据
train = car_info[labels]

# 将数据中的字符串数据处理为数字
le = preprocessing.LabelEncoder()
for label in labels:
    train[label] = le.fit_transform(train[label])

# 将数据规范化
min_max_scaler = preprocessing.MinMaxScaler()
train = min_max_scaler.fit_transform(train)

# # 运用kmeans进行聚类，并用手肘法选择簇数
# sse = []
# for k in range(2,80):
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(train)
#     # 计算簇内误差平方和
#     sse.append(kmeans.inertia_)
# x = range(2,80)
# plt.xlabel('K')
# plt.ylabel('SSE')
# plt.plot(x,sse,'o-')
# plt.show()

# 经过手肘法确认簇数为10-15为宜
kmeans = KMeans(n_clusters=15)
kmeans.fit(train)
predict = kmeans.predict(train)

car_info['聚类结果'] = predict

car_info.to_csv('聚类结果.csv',encoding='gbk',index=False)

# print(car_info)
# 找出vw的车型
vw_cars = car_info[car_info['CarName'].str.contains('vw')|car_info['CarName'].str.contains('volkswagen')]['CarName']

# 针对每种车型搜索竞品车型
for car in set(vw_cars):
    car_label = car_info.loc[car_info['CarName']==car,'聚类结果']
    for temp in car_label:
        car_label = temp

    compete_cars = car_info.loc[car_info['聚类结果']==car_label,'CarName']
    # 将vw车型从竞品车型中去除
    compete_cars = compete_cars.loc[~(compete_cars.str.contains('volkswagen'))&~(compete_cars.str.contains('vw'))]
    compete_cars_list = compete_cars.tolist()
    print("The compete cars of ",car," are:\n",compete_cars_list)
