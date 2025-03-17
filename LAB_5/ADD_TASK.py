import re


if __name__ == '__main__':
    with open('task_add.txt', 'r', encoding='utf-8') as file:
        rand_symbols = file.read()

    emails = re.findall(r'\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})', rand_symbols)
    dates = re.findall (r"\b(\d{2,4}[./-]\d{2,4}[./-]\d{2,4})", rand_symbols)
    adresses = re.findall(r'\s(https?://[a-zA-Z0-9.-]+)', rand_symbols)

    print(*emails)
    print(*dates)
    print(*adresses)

