# -*- coding: utf-8 -*-

import time
from Split_world import split_word

print 'KIỂM LỖI CHÍNH TẢ\n'
sentence = u'học sinh học môn giải tích tại lớp học'
print u'Chuỗi: ', sentence, u'\nKết quả:\n'

start = time.time()

_list = split_word(sentence)
for word in _list:
    print word.word.lower(), word.correct

print 'Total time: ', time.time() - start
