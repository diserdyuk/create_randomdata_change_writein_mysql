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



def random_data(k: int, ntokens: int, pool: str=string.ascii_letters):
    return ((''.join(random.choices(pool, k=k))) for i in range(ntokens))  


def generate_row_col():
    nums = 1024

    return (random_data(8, 6, string.hexdigits) for i in range(nums))    # 1 CB63E6DE ... 66 5753A878


def main():
    for i in generate_row_col():
        with open('random_data_v2.csv', 'a') as f:
            write = csv.writer(f)
            write.writerow(i)



if __name__ == "__main__":
    main()