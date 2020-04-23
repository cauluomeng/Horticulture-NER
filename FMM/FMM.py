#!/usr/bin/python3
# -*- coding: utf-8 -*-
test_file = 'dict.txt'  # 词典
test_file2 = '思科后门.txt'  # 测试语料
test_file3 = 'result.txt'  # 生成结果

#生成词典
def get_dic(test_file):  # 读取文本返回列表
    with open(test_file, 'r', encoding='utf-8', ) as f:
        try:
            file_content = f.read().split()
        finally:
            f.close()
    chars = list(set(file_content))
    return chars
dic = get_dic(test_file)

#读取测试文本
my_list = []
def readfile(test_file2):
    max_length = 5
    h = open(test_file3, 'w', encoding='utf-8', )
    with open(test_file2, 'r', encoding='utf-8', ) as f:
        lines = f.readlines()
#正向最大匹配
    for line in lines:
        max_length = 5
        my_list = []
        len_hang = len(line)
        while len_hang > 0:
            tryWord = line[0:max_length]
            while tryWord not in dic:
                if len(tryWord) == 1:
                    break
                tryWord = tryWord[0:len(tryWord) - 1]
            my_list.append(tryWord)
            line = line[len(tryWord):]
            len_hang = len(line)
            # print(my_list)
# 将分词结果写入文本
        for t in my_list:
            if t == '\n':
                h.write('\n')
            else:
                h.write(t + "  ")
    h.close()
readfile(test_file2)

#读取生成的分词文件
def get_dict(file, need_word):
    dict_words = {}
    with open(file, 'r', encoding='utf8') as fr:
        for line in fr:
            words = line.split("  ")
            for word in words:
                if word in need_word:
                    dict_words[word] = dict_words.get(word, 0) + 1
    return dict_words

#词频统计
r_dic = get_dict(test_file3, dic)
sort_dic = sorted(r_dic.items(), key=lambda item: item[1], reverse=True)
fw = open(test_file, 'w', encoding='utf8')
ii = 0
for key, value in sort_dic:
    fw.write(key + "\t" + str(value) + "\n")
    ii += 1
    if ii > 99:
        break
fw.close()
