#!/usr/local/bin/python3
# coding:utf-8

"""
@author: joey
@file: word_count.py
@time: 2020/07/19
"""

from pathlib import Path

INPUT_PATH = input('enter your path:')
INPUT_FILE_CLASS = input('enter what you want to count of the files("*.py"):')
sum_all = 0

for path in Path(INPUT_PATH).glob(INPUT_FILE_CLASS):
    file = path.read_text(encoding='utf-8')
    l = len(file)
    print('file: (%s) have: (%s)' % (path.name, l))
    sum_all += l
print('all file count: (%s)' % sum_all)
