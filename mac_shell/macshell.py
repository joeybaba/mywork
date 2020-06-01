# coding: utf-8

"""调用shell脚本"""

import os
import json
import logging
import subprocess

logging.basicConfig(level=logging.INFO)
global cmd


def printcmd():
    if cmd:
        print('\n目前指令有：')
        print('序号', ' 命令')
        for i, v in enumerate(cmd):
            print(i, ' : ', v)
        return True
    else:
        print('命令为空')
        return False


def addcmd():
    global cmd
    print('请输入新指令(该指令将预运行以检查是否有效):')
    newcmd = input()
    try:
        subprocess.check_call(newcmd, shell=True, stdout=False, stderr=subprocess.STDOUT)
        cmd.append(newcmd)
        with open('maccmd.json', 'w', encoding='utf-8') as f:
            json.dump(cmd, f, ensure_ascii=False)
        print('增加成功')
    except Exception as e:
        print('指令无效')


def delcmd():
    global cmd
    printcmd()
    n = int(input('\n选择需要删除的指令:'))
    if n < len(cmd):
        del cmd[n]
        with open('maccmd.json', 'w', encoding='utf-8') as f:
            json.dump(cmd, f, ensure_ascii=False)
        print('删除成功')
    else:
        print('输入指令无效，删除失败')
    printcmd()


def runcmd():
    try:
        if printcmd():
            n = int(input('\n选择需要运行的指令:'))
            # os.system(cmd[n])
            subprocess.call(cmd[n], shell=True)
    except Exception as e:
        # logging.exception(e)
        print('输入无效')


def defaultcmd():
    global cmd
    cmd = ['PWD', 'diskutil list', 'uptime', 'uname', 'env', 'who', 'whoami', 'w', 'csrutil status']
    with open('maccmd.json', 'w', encoding='utf-8') as f:
        json.dump(cmd, f, ensure_ascii=False)
    print('初始化成功')


def main():
    global cmd
    file = os.path.join(os.getcwd(), 'maccmd.json')
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            cmd = json.load(f)
    else:
        cmd = []
    prompt = """
----------------
菜单：
    【0】初始化指令（重置原有指令）
    【1】运行指令
    【2】增加指令
    【3】删除指令
    【4】退出
选择您的选项:"""
    while True:
        try:
            n = int(input(prompt))
            if n == 0:
                defaultcmd()
            elif n == 1:
                runcmd()
            elif n == 2:
                addcmd()
            elif n == 3:
                delcmd()
            else:
                break
        except Exception as e:
            # logging.exception(e)
            print('输入无效')


if __name__ == '__main__':
    main()
