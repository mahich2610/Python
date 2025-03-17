import csv
import copy


FILE_NAME = 'books-en.csv'
NAME_COLUMN = 'Book-Author'
BOOK_YEAR = 'Year-Of-Publication'
DOWNLOADS = 'Downloads'


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(";")
    title = [col.strip() for col in title] 
    return title


def get_object(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    result = next(reader)
    return result


def publishers(file):
    with open(file) as dataset:
        title = get_title(dataset)
        return set([get_object(line, title)['Publisher'] for line in dataset])


def popular_book(file):
    with open(file) as dataset:
        main_d = {}
        downloads_numbers, pop_book = [], []
        title = get_title(dataset)
        for line in dataset:
            res = get_object(line, title)
            downloads_numbers.append(int(res[DOWNLOADS]))
            main_d[res[NAME_COLUMN]] = int(res[DOWNLOADS])
        downloads_numbers = list(set(sorted(downloads_numbers)))[::-1]
        for i in downloads_numbers:
            for key, value in main_d.items():
                if value == i:
                    pop_book.append(key)
                if len(pop_book) == 20:
                    return pop_book
    
                
if __name__ == '__main__':
    print(publishers(FILE_NAME))
    print(popular_book(FILE_NAME))
