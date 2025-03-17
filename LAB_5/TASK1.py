import re

FILE_RU = 'task1-ru.txt'
FILE_EN = 'task1-en.txt'

if __name__ == '__main__':
    with open(FILE_EN, encoding='utf-8') as file:
        print(re.findall(r'[A-Z][a-z]+|[a-z]+[:]', file.read()))
    with open(FILE_RU, encoding='utf-8') as file:
        print(re.findall(r'[А-Я][а-я]+|[а-я]+[:]', file.read()))