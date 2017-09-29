from dic_hashing import to_int


class Word:
    def __init__(self, _word, _correct):
        self.word = _word
        self.correct = _correct


def special_type(word):
    if is_mail_address(word) == 1:
        word = '?isName?'
    if is_marker(word) == 1:
        word = '?isDigit?'
    return word


def is_mail_address(word):
    try:
        is_email = word.index('@')
        print is_email
        for i in range(0, is_email):
            if word[i] != '.' and to_int(word[i]) == 0:
                return 0

        for j in range(is_email + 1, len(word)):
            if word[j] != '.' and to_int(word[j]) == 0:
                return 0

        return 1
    except ValueError:
        return 0


def is_marker(word):
    if word == "'" or word == '"' or word == '.' or word == ',' or word == '...' or word == '?' or word == '!'\
            or word == ':' or word == ';' or word == '-':
        return 1
    return 0
