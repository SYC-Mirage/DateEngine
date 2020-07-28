import pandas as pd
from efficient_apriori import apriori

# 读取源数据
raw_dates = pd.read_csv('D:\数据分析学习\数据分析训练营-结营考试\数据分析训练营-结营考试\ProjectB\日期表.csv',sep=',',encoding='gbk')
orders = pd.read_csv('D:\数据分析学习\数据分析训练营-结营考试\数据分析训练营-结营考试\ProjectB\订单表.csv',sep=',',encoding='gbk')

# 将日期取出，以每一天的销售作为一项
dates = raw_dates['日期']
transactions = []
print(len(orders))

# 以字典形式存储日期和销售的产品
data = {}
for date in dates:
    data[date] = []

for i in range(0,len(orders)):
    item = orders.loc[i]
    data[item['订单日期']].append(item['产品名称'])

# 去除重复的产品
for date in dates:
    data[date] = set(data[date])
    transactions.append(data[date])

# 进行关联性分析，经多次尝试确定了min_support和min_confidence合适的取值
items, rules = apriori(transactions, min_support=0.27,  min_confidence=0.2)
print("频繁项集：", items)
print("关联规则：", rules)
