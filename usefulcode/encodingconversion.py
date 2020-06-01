# coding:utf-8

"""编码批量转换 https://www.jianshu.com/p/d5030db5da0e"""

import os
import codecs
import chardet
import logging


# get the specified folder file
def listfolderfiles(path):
    """返回‘文件夹’和‘文件’"""

    list_folder = []
    list_files = []

    for file in os.listdir(path):
        file_folder_path = os.path.join(path, file)
        if os.path.isdir(file_folder_path):
            list_folder.append(file)
        else:
            list_files.append(file)
    return list_folder, list_files


# file coding transfor
def fileconvert(oldfile_name, newfile, in_code='GBK', out_code='UTF-8'):
    """
        该程序用于将目录下的文件从指定格式转换到指定格式，默认的是GBK转到UTF-8
        :param file:    文件名称
        :param in_code:  输入文件格式
        :param out_code: 输出文件格式
        :return:
        """

    out_path = '/Users/joey/Desktop/test/new'
    try:
        with codecs.open(oldfile_name, 'r', in_code) as f_in:
            new_content = f_in.read()
            f_out = codecs.open(os.path.join(out_path, newfile), 'w', out_code)
            f_out.write(new_content)
            f_out.close()
    except IOError as err:
        logging.exception(err)


# Main function
def Main():
    path = '/Users/joey/Desktop/test/old'
    floders, files = listfolderfiles(path)
    os.chdir('/Users/joey/Desktop/test/old')
    for file in files:
        with open(file, 'rb') as f_in:
            data = f_in.read()
            code_type = chardet.detect(data)['encoding']
            fileconvert(file, file, code_type, 'UTF-8')


if __name__ == '__main__':
    Main()

    # a,b = listfolderfiles('/Users/joey/Desktop/test/old')
    # print(os.getcwd())
    # print(a,b)
