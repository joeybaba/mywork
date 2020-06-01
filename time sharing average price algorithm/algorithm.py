# coding:utf-8

"""股票分时均价算法"""

import json
from jsonpath_ import jsonpathpractice
import pandas

file = 'stockdata.json'
with open(file, 'r', encoding='utf-8') as f:
    stock_data = json.load(f, encoding='utf-8')

inTradingPriceList = jsonpathpractice.jsonpathpractice(stock_data, '$..inTradingPriceList')
inTradingVolList = jsonpathpractice.jsonpathpractice(stock_data, '$..inTradingVolList')

tradingpricelist = inTradingPriceList[0]
tradingvollist = inTradingVolList[0]


# 序号从0开始，239结束
def numerator(n):
    if n == 0:
        return tradingpricelist[0] * tradingvollist[0]
    return tradingpricelist[n] * tradingvollist[n] + numerator(n - 1)


# 序号从0开始，239结束
def denominator(n):
    if n == 0:
        return tradingvollist[0]
    return tradingvollist[n] + denominator(n - 1)


if __name__ == '__main__':
    result = []
    for i in range(len(tradingvollist)):
        dateresult = numerator(i) / denominator(i)
        result.append(dateresult)
    print(result)
    series = pandas.Series(result, dtype=float, name='value')
    series.to_csv('stockresult.csv')


