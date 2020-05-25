# coding:utf-8
import argparse

"""https://www.jianshu.com/p/fef2d215b91d"""
"""https://zhuanlan.zhihu.com/p/56922793"""

# 构造命令行参数
parser = argparse.ArgumentParser(description='Terminal Login tool')

parser.add_argument('-u', help='username value')
parser.add_argument('-p', '--password', type=str, nargs='+', help='password value')  # nargs ‘+’ 表示传入至少一个参数
args = parser.parse_args()

print(args.u)
print(args.password)

# 直接在命令行中就可以向程序中传入参数并让程序运行
# 调用方式
# python3 tempcode2.py --help
# python3 tempcode2.py --p abc

#
# import argparse
# parser = argparse.ArgumentParser(description='菜单')
# parser.add_argument('intergers', type=str, help='传入数字')
# args = parser.parse_args()
# # 获取传入参数
# print(args)
