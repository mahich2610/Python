import csv


FILE_NAME = 'books-en.csv'
BOOK_NAME_COLUMN = 'Book-Title'
NAME_COLUMN = 'Book-Author'
BOOK_YEAR = 'Year-Of-Publication'


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


# first task 
def book_count(dataset, name_column):
     with open(FILE_NAME) as dataset:
        title = get_title(dataset)
        k = 0
        for line in dataset:
            res = get_object(line, title)
            if len(res[name_column]) > 30:
                k+= 1
        return k


# second task
def find_book(dataset, author, name_column):
    with open(FILE_NAME) as dataset:
        title = get_title(dataset)
        book_list = []
        for line in dataset:
            res = get_object(line, title)
            if (res[NAME_COLUMN] == author) and ((int(res[BOOK_YEAR]) == 1991) or (int(res[BOOK_YEAR]) == 1996)):
                book_list.append(res[name_column])
        return book_list if len(book_list) != 0 else "Oh, book's year is not 1991 or 1996 :("


# third task
def library_gen(dataset):
    with open(FILE_NAME) as dataset:
        title = get_title(dataset)
        c = 1
        random_d, random_str = [], []
        for line in dataset:
            if c % 470 == 0:
                random_d.append(get_object(line, title))
            c +=1
        for s in random_d:
            random_str.append(f'{s[NAME_COLUMN]}. {s[BOOK_NAME_COLUMN]} - {s[BOOK_YEAR]}')
    with open('Library_request.txt', 'w') as file:
        for i in range(len(random_str)):
            file.write(f'{i}: {random_str[i]}\n')



if __name__ == '__main__':
   print(book_count(FILE_NAME, BOOK_NAME_COLUMN))
   print(find_book(FILE_NAME, "Carlo D'Este" ,BOOK_NAME_COLUMN))
   library_gen(FILE_NAME)