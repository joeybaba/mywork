from scipy.special import gamma
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 伽马函数
x = np.linspace(0,10,20)
y = gamma(x)
# sns.pointplot(x,y)
sns.lineplot(x,y)
# plt.plot(x,y)
plt.show()
