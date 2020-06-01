# coding:UTF-8

"""内存中读写"""

from io import StringIO
from io import BytesIO


def stringio(str):
    f = StringIO()
    f.writelines([str, ])
    f.write(str)
    print(f.getvalue())

    f.seek(0)
    while True:
        s = f.read()
        if s == '':
            break
        print(s.strip())


def bytesio(str):
    s = str.encode('utf-8')
    f = BytesIO()
    f.write(s)
    f.write(s)

    f.seek(0)
    print(f.read())

    f.seek(0)
    print(f.read().decode('utf-8'))


if __name__ == '__main__':
    stringio('abc')
    print('-----------\n')
    bytesio('abcdef\n')
