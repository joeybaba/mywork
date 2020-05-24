# coding:utf-8

"""词云分析"""

import jieba
import wordcloud
import imageio
import matplotlib.pyplot as plt


def wordcloudanalysis():
    with open('/Users/joey/Documents/PycharmProjects/mywork/Untitled.csv', 'r') as f:
        file = f.read().lower()

    mk = imageio.imread('/Users/joey/Documents/PycharmProjects/mywork/image.jpg')
    font = '/Users/joey/Library/Fonts/TT-Me.ttf'
    w = wordcloud.WordCloud(mask=mk, width=1920, height=1080, font_path=font, background_color='white',
                            max_words=100,
                            stopwords={'M17F', 'M19F', 'M18F', '已完成',
                                       '19F', 'M18F', '待跟进', '17F', '19e',
                                       '18w', '18f', '17e', '需要', '协助'})
    # w.generate(file)
    w.generate_from_text(file)
    w.to_file('text100.png')
    # plt.imshow(w, interpolation='bilinear')
    # plt.axis('off')
    # plt.show()


def jiebaanalysis():
    with open('/Users/joey/Documents/PycharmProjects/mywork/Untitled.csv', 'r') as f:
        file = f.read().lower()
    textlist = jieba.lcut(file)
    newlist = []
    for i, v in enumerate(textlist):
        if v in ['\n', '-']:
            continue
        else:
            newlist.append(v.strip())
    countdict = {}
    for i in newlist:
        countdict[i] = countdict.get(i, 1) + 1
    countlist = list(countdict.items())
    countlist.sort(key=lambda x: x[1], reverse=True)
    print(type(countlist))
    with open('countlist.text', 'w', encoding='utf-8') as f:
        f.write('词组 ' + ' 频率\n')
        for i in countlist:
            f.write(str(i) + '\n')

    newstr = ' '.join(newlist)
    return newstr


def test(newlist):
    font = '/Users/joey/Library/Fonts/TT-Me.ttf'
    w = wordcloud.WordCloud(width=1920, height=1080, font_path=font,
                            background_color='white', max_words=200,
                            )
    w.generate_from_text(newlist)
    w.to_file('test100.png')


if __name__ == '__main__':
    newstr = jiebaanalysis()
    test(newstr)
