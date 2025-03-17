import re

FILE_PATH = 'task2.html'

if __name__ == '__main__':
    with open(FILE_PATH, 'r', encoding='utf-8') as html_file:
        source_code = html_file.read()
        tags = set(re.findall(r'[/]\w+', source_code))
print(tags)