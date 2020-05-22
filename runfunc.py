from rootmain2 import RootMain
from sys import stdin

prompt = """-----------------------------
please select your options:\r\n
(l)ook function main
(u)se function
(s)ee package function
\r\n:"""

while True:
    instr = input(prompt).lower()
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
            # a = str(stdin.readline())
            eval(a)
    elif instr == 's':
        packagename = str(input('input your package name:'))
        a = RootMain(packagename)
        result = a.callfunc()
        print(result)
    else:
        print('exit')
        break
