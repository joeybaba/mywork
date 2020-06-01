# coding:UTF-8

"""动态规划求最长公共子串"""


# https://blog.csdn.net/ggdhs/article/details/90713154?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4
# 返回最长子串长度
def lcs(string1, string2):
    if len(string1) < len(string2):
        string1, string2 = string2, string1
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
    result1 = 0

    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if string2[i - 1] == string1[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
                if result1 < res[i][j]:
                    max_result = res[i][j]
                    i_value = i
                    j_value = j
    string3 = string1[j_value - max_result:j]
    return max_result, string3


# 第二种方法
def fn(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    maxstr = s1
    substr_maxlen = max(len(s1), len(s2))
    for sublen in range(substr_maxlen, -1, -1):
        for i in range(substr_maxlen - sublen + 1):
            if maxstr[i:i + sublen] in s2:
                return maxstr[i:i + sublen]


if __name__ == '__main__':
    result = lcs('helloworld', 'world')
    print(result)

    result = fn('amdyesyes yesb', 'intelyes, two yesyes yesbb')
    print(result)
