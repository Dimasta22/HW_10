import re


ACTION_list = [
    'HELLO',
    'ADD',
    'CHANGE',
    'PHONE',
    'SHOW ALL',
    'GOOD BYE',
    'CLOSE',
    'EXIT',
    'REMOVE'
]


def parser(sentence: str):
    for key in ACTION_list:
        func = re.search(fr'^{key}\b', sentence.upper().strip())
        if func is not None:
            return func.group()


if __name__ == '__main__':
    sentence = 'goOd bye'
    print(parser(sentence))