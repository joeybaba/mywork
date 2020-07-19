#!/usr/local/bin/python3
# coding:utf-8

"""
@author: joey
@file: batch_merge_csv.py
@time: 2020/07/19
"""

from pathlib import Path
import pandas as pd
import os

INPUT_PATH = input('enter your path:')
OUTPUT_NAME = input('enter output file name:')
if '.csv' not in OUTPUT_NAME:
    OUTPUT_NAME = OUTPUT_NAME + '.csv'
csv_file_list = []
os.chdir(INPUT_PATH)

for fname in Path(INPUT_PATH).glob('*.csv'):
    csv_file = pd.read_csv(fname, header=0)
    csv_file_list.append(csv_file)
    print('file:', fname.name)

# pd.concat(csv_file_list, ignore_index=True).drop_duplicates().reset_index(drop=True).to_csv(OUTPUT_NAME)
new_data = pd.concat(csv_file_list, ignore_index=True)
new_data.to_csv(OUTPUT_NAME)
print('done!')

"""enter your path:/Users/joey/Desktop/1
enter output file name:a
file: test.csv
file: test 2.csv
file: test 3.csv
done!"""
