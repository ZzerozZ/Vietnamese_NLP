# -*- coding: utf-8 -*-


def get_word(dec):
    r_value = dec.split('\t')
    return r_value[0].strip()


def get_dictionary():

    input_file = open("VDic_uni.txt", "r")
    dic = []
    for line in input_file:
        dic.append(get_word(line))
    return dic


def is_exist(word):
    dic = get_dictionary()
    try:
        dic.index(word)
        return u'\u2713'
    except ValueError:
        return u'\u274C'


def split_word(sentence):
    words = sentence.split(' ')
    word_array = []
    i = 0
    while i < len(words):
        if i + 2 < len(words) and is_exist((words[i] + ' ' + words[i + 1] + ' ' + words[i + 2]).encode('utf-8')) == u'\u2713':
            word_array.append(words[i] + ' ' + words[i + 1] + ' ' + words[i + 2])
            i += 2
        elif i + 1 < len(words) and is_exist((words[i] + ' ' + words[i + 1]).encode('utf-8')) == u'\u2713':
            word_array.append(words[i] + ' ' + words[i + 1])
            i += 1
        else:
            word_array.append(words[i])
        i += 1
    return word_array
