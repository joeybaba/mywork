"""程序目标：读取“地址”列中的区/县名，
并复制到“所在区（县、市）”列同一行的格子中"""
import pandas as pd
import numpy as np
import re
import warnings
import os as bb
warnings.filterwarnings("ignore")  # 过滤警告
# del warnings


regex = re.compile(r".{2}(区|县)")  # 准备正则表达式
# data = pd.read_excel(table)  # 读取表格数据
# row = data["地址"]  # 读取“地址”列数据

row = ['浙江省杭州市余杭区仁和镇獐山街道'] * 5
print(row)
# data = pd.DataFrame(np.arange(10).reshape(5,2),columns=['a','b'])
data = pd.DataFrame()
print(data)
for i in row:
    place = regex.search(i).group()  # 匹配区/县名（到这里可以正常匹配区/县名）
    data['c']=place  # 将区/县名复制到“所在区（县、市）”列
    print(data.values)
# ↑ 到这一步无法正常运行，输出data["所在区（县、市）"]时出现奇怪的数据


# data.to_excel(output) # 写入至新的XLSX文件
# print(data)





