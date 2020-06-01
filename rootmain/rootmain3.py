# coding:utf-8

"""主菜单类，创建功能，调用函数"""

# rootmain3该版本替换数据保存方式，用数据库保存

# TODO 读取函数菜单 ok、创建函数 ok、保存函数菜单 ok
# TODO 返回调用函数 ok：通过runfunc调用

import sys
import traceback
import mysql.connector
# from mysql.connector import connect
from sys import stdin
import logging


# logging.basicConfig(level=logging.DEBUG)  # 大写debug，info，warning，error


class RootMain(object):
    def __init__(self, package):
        self.package = package
        try:
            self.dbconn = WriteDB()
        except Exception as e:
            print(e)
            print('MySQL failure')

        try:
            self.importfunc = __import__(self.package)
            self.__createtext()
        except Exception as e:
            # traceback.print_exc(limit=10, file=sys.stdout)
            # logging.exception(e)  # 显示错误后继续执行
            self.importfunc = None

    # TODO func
    def callfunc(self):
        funclist = [e for e in dir(self.importfunc) if not e.startswith('_')]
        return funclist

    def __createtext(self):  # 创建存储功能函数的text
        try:
            self.dbconn.insertvalue(self.importfunc.__name__)
            self.dbconn.closeconn()
        except Exception as e:
            logging.exception(e)

    def funclist(self):
        try:
            result = self.dbconn.rootmainvalue()
            self.dbconn.closeconn()
            print('now,we have these function:')
            for i in result:
                print(i[0])
        except Exception:
            traceback.print_exc(file=sys.stdout)
            print('function main textfile is NULL\n')


class WriteDB(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', port=3306, user='root',
                                            password='rootroot', charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS rootmaindb")
        self.cursor.execute("USE rootmaindb")
        sql = """CREATE TABLE IF NOT EXISTS rootmain (
                        id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        packagename VARCHAR(100) NOT NULL
                )ENGINE = INNODB DEFAULT CHARSET='utf8'
                """
        self.cursor.execute(sql)  # 注意executemany的用法
        # self.cursor.callproc(sql)
        # self.cursor.stored_results()
        # self.conn.close()

    def rootmainvalue(self):
        sql = "SELECT packagename FROM rootmain"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def insertvalue(self, packagename):
        result = self.rootmainvalue()
        for i in result:
            if i[0] == packagename:
                print('exists')
                break
        else:
            try:
                sql2 = "INSERT INTO rootmain(packagename) VALUES ('%s')" % packagename
                self.cursor.execute(sql2)
                self.conn.commit()
            except:
                self.conn.rollback()

    def testinsertion(self, packagename):
        sql3 = "INSERT INTO rootmain(packagename) VALUES ('%s')" % packagename
        try:
            self.cursor.execute(sql3)
            self.conn.commit()
        except:
            self.conn.rollback()

        value = []
        for i in range(10):
            value.append((i,))
        print(value)
        sql4 = "INSERT INTO rootmain(packagename) VALUES ('%s')"
        try:
            # value为列表，内为元组
            self.cursor.executemany(sql4, value)
            self.conn.commit()
        except Exception as e:
            logging.exception(e)
            self.conn.rollback()

    def closeconn(self):
        self.cursor.close()
        self.conn.close()


def runmian():
    prompt = """-----------------------------
    please select your options:\r\n
    (l)ook registrable function main
    (u)se function(package)
    (s)ee function in package 
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
                        print('invalid statement')
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

    # testconn = WriteDB()
    # testconn.testinsertion('joeybaba')
    # testconn.closeconn()
