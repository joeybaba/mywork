# coding: utf-8

"""调用shell脚本"""

import os
import logging
import subprocess

logging.basicConfig(level=logging.INFO)
cmd = ['ls', 'uptime','PWD']


def printcmd():
    print('\n目前指令有：')
    print('序号', ' 命令')
    for i, v in enumerate(cmd):
        print(i, ' : ', v)


def addcmd():
    global cmd
    print('请输入新指令(该指令将预运行以检查是否有效):')
    newcmd = input()
    try:
        subprocess.check_call(newcmd, shell=True, stdout=False, stderr=subprocess.STDOUT)
        cmd.append(newcmd)
        print('增加成功')
    except Exception as e:
        print('指令无效')


def runcmd(n):
    print('\n')
    os.system(cmd[n])
    print('\n')


def main():
    os.chdir('/Users/joey/')
    prompt = """
----------------
菜单：
【0】运行指令
【1】增加指令
【2】退出
 选择您的指令:"""
    while True:
        try:
            n = int(input(prompt))
            if n == 0:
                try:
                    printcmd()
                    n = int(input('\n选择您的指令:'))
                    runcmd(n)
                except Exception as e:
                    # logging.exception(e)
                    print('输入无效')
            elif n == 1:
                addcmd()
            else:
                break
        except Exception as e:
            # logging.exception(e)
            print('输入无效')


if __name__ == '__main__':
    main()
