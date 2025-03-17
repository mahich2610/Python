ASTHMA = 1
INFECTION = 0
SCORE = 10
FILE = 'item_list.txt'
BAG_SIZE = (3, 3)


def read_obj_list(path):
    with open(path, encoding='utf-8') as file:
        items = sorted([[ int(i.replace('|', '').split()[5])/ int(i.replace('|', '').split()[3]), 
                i.replace('|', '').split()[2],
                int(i.replace('|', '').split()[3]),
                int(i.replace('|', '').split()[5]),] 
                for i in file.readlines()], 
            key=lambda x: (-x[0], x[2] ,-x[3]))
    return items


def check_ill(items, bag, asthma, infec):
    global SCORE
    if asthma:
        id = min([items.index(c) for c in items if c[1] == 'i'])
        bag[len(bag)-1][len(bag)-1] = items[id][1]
        SCORE += items[id][BAG_SIZE[0]]
        items.pop(id)
    if infec:
        id = min([items.index(c) for c in items if c[1] == 'd'])
        bag[len(bag)-1][len(bag)-1] = items[id][1]
        items.pop(id)
        SCORE += items[id][[BAG_SIZE[0]]]


def fill_bag(items, bag):
    global SCORE
    cur_item_id = 0
    recently_del = []
    for i in range(len(bag)):
        count = 0
        while count < 3:
            empty = 0
            for j in range(items[cur_item_id][2]):
                if bag[i][count] == 0:
                    bag[i][count] = items[cur_item_id][1]
                    empty = 1
                count += 1
            if empty == 1: recently_del += [items.pop(cur_item_id)]
            if 0 in bag[i]:
                last_pos = bag[i].index(0)
                while (3 - last_pos < items[cur_item_id][2]) and (cur_item_id < len(items)):
                    cur_item_id+=1
            else: 
                break
    for i in recently_del:
        SCORE += i[3]
    for i in items:
        SCORE -= i[3]


def print_bag(bag):
    for i in range(len(bag)):
        for j in range(len(bag)):
            print(f'[{bag[i][j]}]', end=' ')
        print()
    print(f'Итоговые очки выживания - {SCORE}')


if __name__ == '__main__':
    bag = [[0 for i in range(BAG_SIZE[0])] for j in range(BAG_SIZE[1])]
    items = read_obj_list(FILE)
    check_ill(items, bag, ASTHMA, INFECTION)
    fill_bag(items, bag)
    print_bag(bag)
    
