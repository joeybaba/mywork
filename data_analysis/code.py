# coding:utf-8

import codecs
import chardet

with codecs.open('book1.xlsx', 'rb') as f:
    str = f.read()
    print(str)
    # str.decode('utf-8')
    print(type(str))
    encodinginfo = chardet.detect(str)
    print(encodinginfo)
    # newfile = codecs.open('data11.xlsx', 'wb', 'utf-8')
    # newfile.write(str)
    # print('done')
