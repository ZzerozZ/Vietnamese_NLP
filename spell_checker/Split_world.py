# -*- coding: utf-8 -*-

from Word import Word, special_type
from Sentence import format_sentence
from dic_hashing import hash_word, get_hashtable


def is_exist(word, hash_table):
    word = word.strip().lower().decode('utf-8')
    word = special_type(word)

    k = 0
    pos = hash_word(word)
    while hash_table[(pos + k * k) % 50000].encode('utf-8') != word.lower().encode('utf-8'):
        if hash_table[(pos + k * k) % 50000] == ''.encode('utf-8'):
            return u'\u274C'
        k += 3
    return u'\u2713'


def split_word(sentence):
    sentence = format_sentence(sentence)
    words = sentence.split(' ')
    word_array = []
    hash_table = get_hashtable()

    i = 0
    len_ = len(words)

    while i < len_:
        if i + 2 < len_ and is_exist((words[i] + ' ' + words[i + 1] + ' ' + words[i + 2]).encode('utf-8'), hash_table)\
                == u'\u2713':
            word_array.append(Word(words[i] + ' ' + words[i + 1] + ' ' + words[i + 2], u'\u2713'))
            i += 2
        elif i + 1 < len_ and is_exist((words[i] + ' ' + words[i + 1]).encode('utf-8'), hash_table) == u'\u2713':
            word_array.append(Word(words[i] + ' ' + words[i + 1], u'\u2713'))
            i += 1
        else:
            if is_exist(words[i].encode('utf-8'), hash_table) == u'\u2713':
                word_array.append(Word(words[i], u'\u2713'))
            else:
                word_array.append(Word(words[i], u'\u274C'))
        i += 1

    return word_array
