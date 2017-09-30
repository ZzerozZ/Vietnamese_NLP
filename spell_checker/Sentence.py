# -*- coding: utf-8 -*-

from Word import is_marker


def format_sentence(sentence):
    i = 0
    len_ = len(sentence)
    while i < len_:
        nchar = ''
        if is_marker(sentence[i]):
            if i + 1 < len(sentence) and sentence[i + 1] != ' ':
                nchar = ' '
            sentence = sentence[0: i] + ' ' + sentence[i] + nchar + sentence[i + 1:len(sentence)]
            if nchar == ' ':
                i += 1
                len_ += 1
            i += 1
            len_ += 1
        i += 1
    return sentence
