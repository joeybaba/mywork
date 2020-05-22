# coding:utf-8

"""主菜单类，创建功能，调用函数。原始文档，以'rootmain2.py为准"""

# TODO 读取函数菜单 ok、创建函数 ok、保存函数菜单 ok
# TODO 返回调用函数 ok：通过runfunc调用

import sys
import traceback
import logging

logging.basicConfig(level=logging.DEBUG)  # 大写debug，info，warning，error


class RootMain(object):

    def __init__(self, mainfun):
        self.mainfun = mainfun
        self.importfunc = self.__returnimportfunc()
        if self.importfunc:
            self.__createtext()

    def __call__(self):  # 调用错误的，给出提示
        print('error call')

    # def __getattr__(self, item):  # .属性，间接调用self.importfunc
    #     return self.importfunc

    def __returnimportfunc(self):  # 返回导入的包名
        try:
            mod = __import__(self.mainfun)
            return mod

        except Exception as e:
            # logging.debug(e)
            # logging.exception(e)
            # print(e)
            traceback.print_exc(limit=3, file=sys.stdout)

    def __createtext(self):  # 创建存储功能函数的text
        try:
            with open('../rootmain.txt', 'r') as f:
                pass
        except Exception as e:
            print(e)
            print('first open file,now can we create the rootmain text file? (y/n)')
            if str(input()) == 'y':
                with open('../rootmain.txt', 'w') as f:
                    f.write('%s%s' % (self.importfunc.__name__, '\r\n'))
                    print('create success')
                    f.close()
            else:
                print('ok,bye')

        try:
            with open('../rootmain.txt', 'a+') as f:
                f.seek(0)
                if str(self.importfunc.__name__) not in f.read():
                    f.write('%s%s' % (self.importfunc.__name__, '\r\n'))
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            # print(e,'writefile')

    def funclist(self):
        try:
            with open('../rootmain.txt', 'r') as f:
                print('now,we have these function:')
                print(f.read())
        except IOError:
            traceback.print_exc(file=sys.stdout)
            print('function main textfile NULL')
