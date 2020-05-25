# coding:utf-8

"""分时均价"""

import json
import jsonpath
import pandas

file = '/Users/joey/Documents/PycharmProjects/mywork/stockdata.json'
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


# 序号从0开始，239结束
def denominator(n):
    if n == 0:
        return tradingvollist[0]
    return tradingvollist[n] + denominator(n - 1)


if __name__ == '__main__':

    # print(tradingpricelist)
    # print(tradingvollist)
    # for i in range(3):
    #     dateresult1 = numerator(i)
    #     dateresult2 = denominator(i)
    #     print(dateresult1)
    #     print(dateresult2)

    result = []
    for i in range(len(tradingvollist)):
        dateresult = numerator(i) / denominator(i)
        print(dateresult)
        result.append(dateresult)
    series = pandas.Series(result, dtype=float)
    series.to_csv('stockresult.csv')


    # with open('stockresult.txt', 'w', encoding='utf-8') as f:
    #     f.writelines(result)

