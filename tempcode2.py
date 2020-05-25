# coding:utf-8

"""分时均价"""

import json
import jsonpath
import pandas
import time

file = r'/Users/joey/Documents/PycharmProjects/mywork/stockdata.json'
with open(file, 'r', encoding='utf-8') as f:
    stock_data = json.load(f, encoding='utf-8')

inTradingPriceList = jsonpath.jsonpath(stock_data, '$..inTradingPriceList')
inTradingVolList = jsonpath.jsonpath(stock_data, '$..inTradingVolList')

tradingpricelist = inTradingPriceList[0]
tradingvollist = inTradingVolList[0]


# 序号从0开始，239结束
def numerator(n):
    if n == 0:
        return tradingpricelist[0] * tradingvollist[0]
    return tradingpricelist[n] * tradingvollist[n] + numerator(n - 1)


# 尾递归优化
def numerator_optimize(n, result=tradingpricelist[0] * tradingvollist[0]):
    if n == 0:
        return result
    return numerator_optimize(n - 1, tradingpricelist[n] * tradingvollist[n] + result)


# 序号从0开始，239结束
def denominator(n):
    if n == 0:
        return tradingvollist[0]
    return tradingvollist[n] + denominator(n - 1)


if __name__ == '__main__':
    a = []
    start = time.perf_counter()
    for i in range(239):
        dateresult1 = numerator(i)
        a.append(dateresult1)
        # print(dateresult1)

    print(f'cost: {time.perf_counter() - start}')
    a = []

    start = time.perf_counter()

    for i in range(239):
        dateresult2 = numerator_optimize(i)
        # print(dateresult2)
        a.append(dateresult2)

    print(f'cost: {time.perf_counter() - start}')

    # result = []
    # for i in range(len(tradingvollist)):
    #     dateresult = numerator(i) / denominator(i)
    #     print(dateresult)
    #     result.append(dateresult)
    # series = pandas.Series(result, dtype=float)
    # series.to_csv('stockresult.csv')
