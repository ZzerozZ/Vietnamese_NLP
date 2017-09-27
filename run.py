# -*- coding: utf-8 -*-


from Split_world import is_exist, split_word

print 'KIỂM LỖI CHÍNH TẢ\n'

sentence = u'học sinh học môn giải tích tại lớp học'
print u'Chuỗi: ', sentence, u'\nKết quả:\n'
_list = split_word(sentence)

for word in _list:
    print word.lower(), is_exist(word.lower().encode('utf-8'))

