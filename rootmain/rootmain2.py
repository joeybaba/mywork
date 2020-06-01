# coding:utf-8

"""主菜单类，创建功能，调用函数"""

# TODO 读取函数菜单 ok、创建函数 ok、保存函数菜单 ok
# TODO 返回调用函数 ok：通过runfunc调用

import sys
import traceback
from sys import stdin
import logging


# logging.basicConfig(level=logging.DEBUG)  # 大写debug，info，warning，error


class RootMain(object):

    def __init__(self, package):
        self.package = package
        try:
            self.importfunc = __import__(self.package)
            self.__createtext()
        except Exception as e:
            traceback.print_exc(limit=3, file=sys.stdout)
            # logging.exception(e)  # 显示错误后继续执行
            self.importfunc = None

    # TODO func
    def callfunc(self):
        funclist = [e for e in dir(self.importfunc) if not e.startswith('_')]
        return funclist

    def __createtext(self):  # 创建存储功能函数的text
        try:
            with open('rootmain.txt', 'r') as f:
                pass
        except Exception as e:
            print(e)
            print('first open file,now can we create the rootmain text file? (y/n)')
            if str(input()) == 'y':
                with open('rootmain.txt', 'w') as f:
                    f.write('%s%s' % (self.importfunc.__name__, '\r\n'))
                    print('create success')
                    f.close()
            else:
                print('ok,bye')
        try:
            with open('rootmain.txt', 'a+') as f:
                f.seek(0)
                if str(self.importfunc.__name__) not in f.read():
                    f.write('%s%s' % (self.importfunc.__name__, '\r\n'))
        except Exception as e:
            traceback.print_exc(file=sys.stdout)

    def funclist(self):
        try:
            with open('rootmain.txt', 'r') as f:
                print('now,we have these function:')
                print(f.read())
        except IOError:
            # traceback.print_exc(file=sys.stdout)
            print('function main textfile is NULL\n')


def runmian():
    prompt = """-----------------------------
    please select your options:\r\n
    (l)ook function main
    (u)se function
    (s)ee package function
    (q)uit
    \r\n:"""

    while True:
        try:
            instr = input(prompt).lower()
        except KeyboardInterrupt or EOFError:
            print('nothing input')
            instr = 'q'
        else:
            if instr == 'l':
                RootMain('').funclist()
            elif instr == 'u':
                packagename = str(input('input your package name:'))
                locals()[packagename] = RootMain(packagename).importfunc
                print("now,you can use package.please input your code sentence:(while input '.',stop the process)")
                while True:
                    print('>>>', end='')
                    a = str(input())
                    if a == '.':
                        break
                    # a = str(stdin.readline())  # 第二种方式
                    try:
                        exec(a)
                    except Exception:
                        continue
            elif instr == 's':
                packagename = str(input('input your package name:'))
                a = RootMain(packagename)
                result = a.callfunc()
                print(result)
            elif instr == 'q':
                print('exit')
                break
            else:
                print('exit')
                break


if __name__ == '__main__':
    runmian()
