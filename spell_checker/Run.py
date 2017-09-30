# -*- coding: utf-8 -*-

import time
from Split_world import split_word
from Checker import check

print 'KIỂM LỖI CHÍNH TẢ\n'
sentence = u'Vietnamese Natural Language Processing\
  Xử lý ngôn ngữ là một kĩ thuật quan trọng nhằm giúp máy tính hiểu được ngôn ngữ của con người, qua đó hướng dẫn máy tính thực hiện và giúp đỡ con người trong những công việc có liên quan đến ngôn ngữ như : dịch thuật, phân tích dữ liệu văn bản, nhận dạng tiếng nói, tìm kiếm thông tin, ... \
  XLNN cũng đóng một vai trò quan trọng trong việc đẩy mạnh sự phát triển của CNTT Việt Nam để sánh ngang với các cường quốc khác. \
\
  Tuy nhiên, XLNN tiếng Việt (XLNNTV) cũng vấp phải vô vàn khó khăn, mà lớn nhất phải kể đến sự khó khăn về nhân sự. Những người nắm giữ những kiến thức về XLNNTV quả thực không nhiều, và cũng không có được 1 mạng lưới liên kết, trao đổi và hỗ trợ một cách hiệu quả. Ngoài ra, những khó khăn khác như không có dữ liệu đủ lớn, thiếu những nghiên cứu nền tảng, ... cũng hạn chế không ít sự phát triển của XLNNTV. \
\
  Trang web này được tạo ra để chia sẻ và tập hợp những thông tin về nghiên cứu XLNN nói chung, và XLNNTV nói riêng. Thông qua trang web này, chúng tôi muốn kêu gọi sự đoàn kết và giúp đỡ của những người quan tâm đến XLNNTV. \
  Đầu tiên, chúng tôi muốn tạo ra 1 mailing list để tăng cường sự hiểu biết và liên kết giữa mọi người. Tiếp đó, với sự cộng tác này, chúng tôi sẽ thực hiện những nghiên cứu cơ bản, viết sách cho người mới học, giới thiệu những nghiên cứu mới, tạo dữ liệu và chia sẻ với mọi người. \
\
  Nếu bạn có sự quan tâm đến XLNNTV, hãy tham gia vào mailing list của chúng tôi.\
  Bạn có thể gửi mail về địa chỉ anh(a)jnlp.org. Chúng tôi xin trân trọng cảm ơn sự quan tâm của các bạn.\
\
Tác giả\
Website này được quản lý bởi Lưu Tuấn Anh, hiện đang học tập và làm việc tại Nagaoka University of Technology, Natural Language Processing Yamamoto-lab (Japan).'

print u'Chuỗi: ', sentence, u'\nKết quả:\n'

arr = sentence.split(' ')
print len(arr)
start = time.time()

_list = split_word(sentence)
for word in _list:
    print word.word, word.correct


print 'Total time: ', time.time() - start

check("input.txt")
