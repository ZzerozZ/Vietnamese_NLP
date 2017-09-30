# -*- coding: utf-8 -*-


from Split_world import split_word
# from Word import Word


def check(input_file_path):
    input_file = open(input_file_path, "r")

    str_ = input_file.readlines()
    input_file.close()
    split = []

    for i in range(0, len(str_)):
        split.append(split_word(str_[i].decode('utf-8')))

    output_file = open("output.txt", "w")

    for sentence in split:
        for word in sentence:
            output_file.write((word.word + ' ').encode('utf-8'))
    output_file.close()
