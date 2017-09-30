# -*- coding: utf-8 -*-


def get_word(dec):
    r_value = dec.split('\t')
    return r_value[0].strip()


def to_int(char):
    if char == 'a':
        return 21
    elif char.encode('utf-8') == u'á'.encode('utf-8'):
        return 22
    elif char.encode('utf-8') == u'à'.encode('utf-8'):
        return 23
    elif char.encode('utf-8') == u'ả'.encode('utf-8'):
        return 24
    elif char.encode('utf-8') == u'ã'.encode('utf-8'):
        return 25
    elif char.encode('utf-8') == u'ạ'.encode('utf-8'):
        return 26

    elif char.encode('utf-8') == u'ă'.encode('utf-8'):
        return 31
    elif char.encode('utf-8') == u'ắ'.encode('utf-8'):
        return 32
    elif char.encode('utf-8') == u'ằ'.encode('utf-8'):
        return 33
    elif char.encode('utf-8') == u'ẳ'.encode('utf-8'):
        return 34
    elif char.encode('utf-8') == u'ẵ'.encode('utf-8'):
        return 35
    elif char.encode('utf-8') == u'ặ'.encode('utf-8'):
        return 36

    elif char.encode('utf-8') == u'â'.encode('utf-8'):
        return 43
    elif char.encode('utf-8') == u'ấ'.encode('utf-8'):
        return 44
    elif char.encode('utf-8') == u'ầ'.encode('utf-8'):
        return 45
    elif char.encode('utf-8') == u'ẩ'.encode('utf-8'):
        return 46
    elif char.encode('utf-8') == u'ẫ'.encode('utf-8'):
        return 47
    elif char.encode('utf-8') == u'ậ'.encode('utf-8'):
        return 48

    elif char == 'b':
        return 64

    elif char == 'c':
        return 85

    elif char == 'd':
        return 106

    elif char.encode('utf-8') == u'đ'.encode('utf-8'):
        return 117

    elif char == 'e':
        return 132
    elif char.encode('utf-8') == u'é'.encode('utf-8'):
        return 133
    elif char.encode('utf-8') == u'è'.encode('utf-8'):
        return 134
    elif char.encode('utf-8') == u'ẻ'.encode('utf-8'):
        return 135
    elif char.encode('utf-8') == u'ẽ'.encode('utf-8'):
        return 136
    elif char.encode('utf-8') == u'ẹ'.encode('utf-8'):
        return 137

    elif char.encode('utf-8') == u'ê'.encode('utf-8'):
        return 142
    elif char.encode('utf-8') == u'ế'.encode('utf-8'):
        return 143
    elif char.encode('utf-8') == u'ề'.encode('utf-8'):
        return 144
    elif char.encode('utf-8') == u'ể'.encode('utf-8'):
        return 145
    elif char.encode('utf-8') == u'ễ'.encode('utf-8'):
        return 146
    elif char.encode('utf-8') == u'ệ'.encode('utf-8'):
        return 147

    elif char == 'g':
        return 160

    elif char == 'h':
        return 181

    elif char == 'i':
        return 202
    elif char.encode('utf-8') == u'í'.encode('utf-8'):
        return 203
    elif char.encode('utf-8') == u'ì'.encode('utf-8'):
        return 204
    elif char.encode('utf-8') == u'ỉ'.encode('utf-8'):
        return 205
    elif char.encode('utf-8') == u'ĩ'.encode('utf-8'):
        return 206
    elif char.encode('utf-8') == u'ị'.encode('utf-8'):
        return 207

    elif char == 'k':
        return 223

    elif char == 'l':
        return 244

    elif char == 'm':
        return 265

    elif char == 'n':
        return 286

    elif char == 'o':
        return 292
    elif char.encode('utf-8') == u'ó'.encode('utf-8'):
        return 293
    elif char.encode('utf-8') == u'ò'.encode('utf-8'):
        return 294
    elif char.encode('utf-8') == u'ỏ'.encode('utf-8'):
        return 295
    elif char.encode('utf-8') == u'õ'.encode('utf-8'):
        return 296
    elif char.encode('utf-8') == u'ọ'.encode('utf-8'):
        return 297

    elif char.encode('utf-8') == u'ô'.encode('utf-8'):
        return 302
    elif char.encode('utf-8') == u'ố'.encode('utf-8'):
        return 303
    elif char.encode('utf-8') == u'ồ'.encode('utf-8'):
        return 304
    elif char.encode('utf-8') == u'ổ'.encode('utf-8'):
        return 305
    elif char.encode('utf-8') == u'ỗ'.encode('utf-8'):
        return 306
    elif char.encode('utf-8') == u'ộ'.encode('utf-8'):
        return 307

    elif char.encode('utf-8') == u'ơ'.encode('utf-8'):
        return 322
    elif char.encode('utf-8') == u'ớ'.encode('utf-8'):
        return 323
    elif char.encode('utf-8') == u'ờ'.encode('utf-8'):
        return 324
    elif char.encode('utf-8') == u'ở'.encode('utf-8'):
        return 325
    elif char.encode('utf-8') == u'ỡ'.encode('utf-8'):
        return 326
    elif char.encode('utf-8') == u'ợ'.encode('utf-8'):
        return 327

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
        return 442
    elif char.encode('utf-8') == u'ú'.encode('utf-8'):
        return 443
    elif char.encode('utf-8') == u'ù'.encode('utf-8'):
        return 444
    elif char.encode('utf-8') == u'ủ'.encode('utf-8'):
        return 445
    elif char.encode('utf-8') == u'ũ'.encode('utf-8'):
        return 446
    elif char.encode('utf-8') == u'ụ'.encode('utf-8'):
        return 447

    elif char.encode('utf-8') == u'ư'.encode('utf-8'):
        return 452
    elif char.encode('utf-8') == u'ứ'.encode('utf-8'):
        return 453
    elif char.encode('utf-8') == u'ừ'.encode('utf-8'):
        return 454
    elif char.encode('utf-8') == u'ử'.encode('utf-8'):
        return 455
    elif char.encode('utf-8') == u'ữ'.encode('utf-8'):
        return 456
    elif char.encode('utf-8') == u'ự'.encode('utf-8'):
        return 457

    elif char == 'v':
        return 477

    elif char == 'x':
        return 488

    elif char == 'y':
        return 492
    elif char.encode('utf-8') == u'ý'.encode('utf-8'):
        return 493
    elif char.encode('utf-8') == u'ỳ'.encode('utf-8'):
        return 494
    elif char.encode('utf-8') == u'ỷ'.encode('utf-8'):
        return 495
    elif char.encode('utf-8') == u'ỹ'.encode('utf-8'):
        return 496
    elif char.encode('utf-8') == u'ỵ'.encode('utf-8'):
        return 497

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
