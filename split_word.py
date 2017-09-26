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

