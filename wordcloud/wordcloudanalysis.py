# coding:utf-8

"""词云生成"""

import jieba
import wordcloud
import imageio
import openpyxl
import collections
import matplotlib.pyplot as plt


# 中文分词
def jiebaanalysis():
    with open('/wordcloud/wordclouddata.csv', 'r') as f:
        file = f.read().lower()
    textlist = jieba.lcut(file)

    # 过滤空格等无效单词
    newlist = []
    for v in textlist:
        if v in ['\n', '-', '']:
            continue
        else:
            newlist.append(v.strip())

    # 连接词组，并返回
    newstr = ' '.join(newlist)
    return newstr


def writefile(newlist):

    # 频率计算1
    countdict = {}
    for i in newlist:
        countdict[i] = countdict.get(i, 1) + 1

    # 频率计算2，依赖collections
    # c = collections.Counter()
    # for ch in newlist:
    #     c[ch] = c[ch] + 1

    # 词组频率排序
    countlist = list(countdict.items())
    countlist.sort(key=lambda x: x[1], reverse=True)

    # # 直接转化写入，不使用其他模块
    # with open('countlist.txt', 'w', encoding='utf-8') as f:
    #     f.write('词组 ' + ' 频率\n')
    #     for i in countlist:
    #         f.write(str(i) + '\n')

    # 写入xls,不使用其他模块
    # with open('countlist.xls', 'w', encoding='utf-8',) as f:
    #     f.write('词组\t频率\t\n')
    #     for i in range(len(countlist)):
    #         for j in countlist[i]:
    #             f.write(str(j))
    #             f.write('\t')
    #         f.write('\n')

    # 依赖openpyxl写入文件
    wb = openpyxl.Workbook()
    ws = wb.active
    for i in range(len(countlist)):
        # for j in countlist[i]:
        ws.append(countlist[i])
    wb.save('countlist_xl.xlsx')


# jieba解释后，画词云，输出图片
def jiebawordcloud(newstr):
    # 指定字体
    font = '/Users/joey/Library/Fonts/TT-Me.ttf'
    w = wordcloud.WordCloud(width=1920, height=1080, font_path=font,
                            background_color='white', max_words=200,
                            scale=15)  # scale 清晰度
    w.generate_from_text(newstr)
    w.to_file('jieba_wordcloud.jpg')


# 输出词云图片
def wordcloudanalysis():
    with open('/wordcloud/wordclouddata.csv', 'r') as f:
        file = f.read().lower()

    mk = imageio.imread('/Users/joey/Documents/PycharmProjects/mywork/image.jpg')
    font = '/Users/joey/Library/Fonts/TT-Me.ttf'
    w = wordcloud.WordCloud(mask=mk, width=1920, height=1080, font_path=font, background_color='white',
                            max_words=100,
                            stopwords={'M17F', 'M19F', 'M18F', '已完成',
                                       '19F', 'M18F', '待跟进', '17F', '19e',
                                       '18w', '18f', '17e', '需要', '协助', '谢谢'})
    # 词云生成
    # w.generate(file)
    w.generate_from_text(file)

    # 输出文件
    w.to_file('wordcloud.png')

    # 解释器内直接输出图片
    # plt.imshow(w, interpolation='bilinear')
    # plt.axis('off')
    # plt.show()


if __name__ == '__main__':

    wordcloudanalysis()

    newstr = jiebaanalysis()

    jiebawordcloud(newstr)
