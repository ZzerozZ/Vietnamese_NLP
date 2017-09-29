# -*- coding: utf-8 -*-

import time
from Split_world import split_word

print 'KIỂM LỖI CHÍNH TẢ\n'
sentence = u'YG đã sẵn sàng để chinh phục.Các bạn thấy đông đảo khán giả chủ nhà không,hãy cùng tiếp sức cho YG nào!'
print u'Chuỗi: ', sentence, u'\nKết quả:\n'

start = time.time()

_list = split_word(sentence)
for word in _list:
    print word.word, word.correct

print 'Total time: ', time.time() - start
