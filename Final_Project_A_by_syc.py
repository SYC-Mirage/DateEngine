import requests
import pandas as pd
from bs4 import BeautifulSoup

# 请求url
url = "http://car.bitauto.com/xuanchegongju/?l=8&mid=8"

# 获取页面内容
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html = requests.get(url,headers=headers,timeout=10)
content = html.text
print(content)

# 通过content创建BeautifulSoup对象
soup = BeautifulSoup(content, 'html.parser', from_encoding='gbk')

# 寻找搜索结果,提取车辆信息
car_info = pd.DataFrame()
car_names = []
car_prices = []
imgs = []
for div in soup.find_all('div',class_='search-result-list-item'):
    car_name = div.find('p',class_='cx-name text-hover').text
    car_price = div.find('p',class_='cx-price').text
    car_img = div.find('img',class_='img')['src']
    car_names.append(car_name)
    car_prices.append(car_price)
    imgs.append(car_img)
    print(car_name,'  ',car_price,' ',car_img)
car_info['车辆名称'] = car_names
car_info['车辆价格'] = car_prices
car_info['车辆照片'] = imgs

# 生成csv
car_info.to_csv("车辆数据采集.csv",index=False,encoding='gbk')

