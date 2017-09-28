# -*- coding: utf-8 -*-
# NEED TO UPDATE: 'á', 'ở',...


def get_word(dec):
    r_value = dec.split('\t')
    return r_value[0].strip()


def to_int(char):
    if char == 'a':
        return 21
    elif char.encode('utf-8') == u'ă'.encode('utf-8'):
        return 32
    elif char.encode('utf-8') == u'â'.encode('utf-8'):
        return 43
    elif char == 'b':
        return 64
    elif char == 'c':
        return 85
    elif char == 'd':
        return 106
    elif char.encode('utf-8') == u'đ'.encode('utf-8'):
        return 117
    elif char == 'e':
        return 138
    elif char.encode('utf-8') == u'ê'.encode('utf-8'):
        return 149
    elif char == 'g':
        return 160
    elif char == 'h':
        return 181
    elif char == 'i':
        return 202
    elif char == 'k':
        return 223
    elif char == 'l':
        return 244
    elif char == 'm':
        return 265
    elif char == 'n':
        return 286
    elif char == 'o':
        return 297
    elif char.encode('utf-8') == u'ô'.encode('utf-8'):
        return 308
    elif char.encode('utf-8') == u'ơ'.encode('utf-8'):
        return 329
    elif char == 'p':
        return 340
    elif char == 'q':
        return 361
    elif char == 'r':
        return 382
    elif char == 's':
        return 403
    elif char == 't':
        return 424
    elif char == 'u':
        return 445
    elif char.encode('utf-8') == u'ư'.encode('utf-8'):
        return 456
    elif char == 'v':
        return 477
    elif char == 'x':
        return 488
    elif char == 'y':
        return 499
    else:
        return 0


def hash_word(word):
    hash_value = 0
    for char in range(0, len(word)):
        hash_value += to_int(word[char])
    return hash_value % 50000


def hash_dictionary():
    input_file = open("VDic_uni.txt", "r")
    input_ = input_file.readlines()
    input_file.close()

    dic = []
    for i in range(0, 50000):
        dic.append('\n')

    index = 0
    while index < len(input_):
        pos = hash_word(get_word(input_[index].decode('utf-8')))
        k = 0
        while dic[(pos + k * k) % 50000] != '\n':
            k += 3
        dic[(pos + k * k) % 50000] = input_[index]
        index += 1

    file_out = open("dic_hashed.txt", "w")
    for i in range(0, 50000):
        file_out.write(dic[i])
    file_out.close()


def get_hashtable():
    dic = open("dic_hashed.txt", "r").readlines()
    for i in range(0, len(dic)):
        dic[i] = get_word(dic[i]).lower().strip().decode('utf-8')
    return dic
