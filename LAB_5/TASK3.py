import re
import csv

PARAMS = ('ID', 'Surname', 'Mail', 'Reg Date', 'Site')

if __name__ == '__main__':
    with open('task3.txt', encoding='utf-8') as file:
        data = file.read().replace('\n', ' ')

    mails = re.findall(r'\w*@[a-z0-9-]+\.[a-z]{2,}', data)
    families = re.findall(r'[A-Z][a-z]+', data)
    date = re.findall(r'\d{4}-\d{2}-\d{2}', data)
    site = re.findall(r'https?://[a-zA-Z0-9.-]+/', data)


    with open('task_3.csv', 'w', newline='') as f:
        file = csv.writer(f)
        file.writerow(PARAMS)
        for i in range(len(mails)):
            file.writerow((i, families[i], mails[i], date[i], site[i]))