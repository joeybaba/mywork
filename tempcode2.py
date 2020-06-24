'''
@Author: your name
@Date: 2020-04-30 18:15:53
@LastEditTime: 2020-06-24 11:09:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /mywork/tempcode2.py
'''
from scipy.special import gamma
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed()

# 伽马函数
# *din
# !da
# TODO:daif
# ?da
x = np.linspace(0, 10, 20)
y = gamma(x)
# sns.pointplot(x,y)
sns.lineplot(x, y)
# plt.plot(x,y)
df = np.random.normal()
df = np.radom.normal()
for i in range(11):
    try:
        