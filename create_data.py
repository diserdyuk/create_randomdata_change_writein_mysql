'''
скрипт

1) генерирyет csv файл из 1024 записей по 6 столбцов,
заполненных строками случайных символов (цифры и латинские буквы) 
длиной по 8 символов
2) записывает данные в новый файл 
'''

import random
import string
import csv


# func generate random datas 
def random_data(k: int, ntokens: int, pool: str=string.ascii_letters) -> set:
    seen = set()
    while len(seen) < ntokens:
        token = ''.join(random.choices(pool, k=k))
        seen.add(token)
    return seen


def generate_row_col():
    rows = [ ]
    cnt = 1
    nums = 1025    # get 1024 rows
    while cnt < nums:
        symbols = (random_data(8, 6, string.hexdigits))
        symb_l = list(symbols)
        rows.append(symb_l)
        cnt += 1
    return rows


def write_csv(data):
    with open('random_data.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow(data)


def main():
    for i in generate_row_col():
        write_csv(i)



if __name__ == "__main__":
    main()