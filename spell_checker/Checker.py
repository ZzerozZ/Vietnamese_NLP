# -*- coding: utf-8 -*-


from Split_world import split_word


def check(input_file_path):
    input_file = open(input_file_path, "r")

    str_ = input_file.readlines()
    input_file.close()
    split = []

    for i in range(0, len(str_)):
        split.append(split_word(str_[i].decode('utf-8')))

    output_file = open("output.txt", "w")

    for sentence in split:
        for i in range(0, len(sentence)):
            str_ = ' '
            if i < len(sentence) - 1 and sentence[i + 1].word == '\n':
                str_ = ''
            output_file.write((sentence[i].word + str_).encode('utf-8'))
    output_file.close()
