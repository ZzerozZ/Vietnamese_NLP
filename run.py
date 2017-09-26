# -*- coding: utf-8 -*-

import underthesea


from Split_world import is_exist

print 'KIỂM LỖI CHÍNH TẢ\n'

sentence = u'một nhóm xe ôm truyền thống đánh hội đồng một người chạy GrabBike'
print u'Chuỗi: ', sentence, u'\nKết quả:\n'
_list = underthesea.word_sent(sentence)

for word in _list:
    print word.lower(), is_exist(word.lower().encode('utf-8'))


