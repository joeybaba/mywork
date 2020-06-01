# coding:UTF-8

__author__ = 'joey'

"""JSON和Python的转换，jsonpath"""
import os
import json
import jsonpath

os.chdir('/Users/joey/Documents/PycharmProjects/mywork/jsonpath_/')

listStr = [1, 2, 3, 4]

print(type(listStr))

# Python类型转换为JSON字符串
# 注意：json.dumps() 序列化时默认使用的ascii编码
# 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
result = json.dumps(listStr, ensure_ascii=False)
print(result, type(result))

listStr1 = [{"city": "北京"}, {"name": "蚂蚁"}]
result1 = json.dumps(listStr1, ensure_ascii=False)
print(type(result1))

# 将Python内置类型序列化为Json对象后写入文件
json.dump(listStr, open('listStr.json', 'w', encoding='utf-8'), ensure_ascii=False)

# 把Json格式字符串解码转换成Python对象
# json数据自动按utf-8存储
listStr2 = '[1, 2, 3, 4]'
result2 = json.loads(listStr2)
print(result2, type(result2))

# 读取文件中Json形式的字符串，转换成Python类型
strlist = json.load(open(r'/Users/joey/Downloads/股票数据/ranks.json', 'r'), encoding='utf-8')
print(type(strlist))

# 读写第一层name和percent
pathresult = jsonpath.jsonpath(strlist, '$.*.name')
pathresult1 = jsonpath.jsonpath(strlist, '$.*.percent')
# print(pathresult[-1])
# print(pathresult1[0])

# 组合name和percent并显示
newresult = []
for i in range(0, len(pathresult)):
    newresult.append(pathresult[i] + ' ' + pathresult1[i])
    print(newresult[i])
