# # coding: utf-8
#
# """openpyxl lib"""
#
# import os
# from openpyxl import load_workbook
#
# # print(os.getcwd())
#
#
# workbook = load_workbook(filename='test.xlsx', read_only=True)
# print(workbook.sheetnames)
# ws = workbook.active
# print(ws.max_row)
#
# # sheet = workbook['DM004_月休安排不合理导致的加班成本(考勤月)']
# # print(sheet)
# # workbook.sheetnames()
# # workbook = load_workbook()

import pandas as pd
import numpy as np
import openpyxl
import time
import asyncio


# async def read():
#     return openpyxl.load_workbook('data.xlsx', read_only=True).active
#
#
# async def write():
#     newwb = openpyxl.Workbook()
#     newws = newwb.active
#     t = 1
#     ws = await read()
#     for i in ws.values:
#         newws.append(i)
#         t += 1
#         if t == 10:
#             break
#     newwb.save('bb1.xlsx')
#
#
#
# asyncio.run(write())

import random
import numpy
a = numpy.random.rand(1)

print(type(a),type(str(a)))
