# -*- coding: utf-8 -*-

from Word import is_marker


def format_sentence(sentence):
    i = 0
    len_ = len(sentence)
    while i < len_:
        if is_marker(sentence[i]):
            sentence = sentence[0: i] + ' ' + sentence[i] + ' ' + sentence[i + 1:len(sentence)]
            i += 1
            len_ += 2
        i += 1
    return sentence
