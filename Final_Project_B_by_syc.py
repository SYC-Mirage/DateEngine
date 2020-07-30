import pandas as pd
from efficient_apriori import apriori

# 读取源数据
raw_guests = pd.read_csv('D:\数据分析学习\数据分析训练营-结营考试\数据分析训练营-结营考试\ProjectB\客户.csv',sep=',',encoding='gbk')
orders = pd.read_csv('D:\数据分析学习\数据分析训练营-结营考试\数据分析训练营-结营考试\ProjectB\订单表.csv',sep=',',encoding='gbk')

# 将客户ID取出，以每一个客户的销售作为一项
guests = raw_guests['客户ID']
transactions = []
print(len(orders))

# 以字典形式存储客户ID和销售的产品
data = {}
for guest in guests:
    data[guest] = []

for i in range(0,len(orders)):
    item = orders.loc[i]
    data[item['客户ID']].append(item['产品名称'])

# 去除重复的产品
for guest in guests:
    data[guest] = set(data[guest])
    transactions.append(data[guest])

# 进行关联性分析，经多次尝试确定了min_support和min_confidence合适的取值
items, rules = apriori(transactions, min_support=0.08,  min_confidence=0.1)
print("频繁项集：", items)
print("关联规则：", rules)
