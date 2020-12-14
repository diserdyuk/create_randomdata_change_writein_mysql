'''
скрипт

1) считывает содержимое файла и заменяет нечетные цифры символом #, 
2) удаляет записи, в которых любая из шести строк начинается с гласной буквы,
3) сохраняет отредактированный файл с другим именем
'''

import csv



def read_csv_2(file):
    reader = csv.reader(file)
    return reader


def change_nums():
    one_row = [ ]
    cnt = 1
    with open('random_data.csv', 'r') as f:
        for i in read_csv_2(f):
            for s in i:    # s -> b E E 2 6 7 C 8 3 E ... 8 B F d C f
                for y in s: 
                    if y.isdigit():
                        y = int(y)
                        if y % 2 != 0:
                            y = '#'
                            one_row.append(y)
                        else:
                            one_row.append(y)
                    else:
                        one_row.append(y)  
            row_l = one_row
        
        block = [ ]
        cnt = 0
        for i in row_l:
            cnt += 1
            block.append(i)
            if cnt == 8:
                block.append(' ')    # block -> ['b', 'E', 'E', 2, 6, '#', 'C', 8, ' ', ... , ' ', 'B', 6, 4, 'c', 'A', '#',]
                cnt = 0

        res_row = ''.join(map(str, block))    # res_row -> bEE26#C8 #E#A#A0D D#Bb##0E 28ca#aCD B64cA#eC d68BFdCf ... 
        return res_row


def prepare_data():
    all_symb = change_nums()    # all_symb -> bEE26#C8 #E#A#A0D D#Bb##0E 28ca#aCD B64cA#eC d68BFdCf eEd6##DE a88A6b## ... 
    
    one_symb = [ ]
    symb = [ ]
    cnt = 0
    for i in all_symb:
        if i == ' ':
            print(end='')
        else:
            one_symb.append(i)
            cnt += 1
            if cnt == 8:
                symb.append(''.join(map(str, one_symb)))
                cnt = 0
                one_symb = []
    
    cnt_2 = 0
    six_symb = [ ]
    for i in symb:
        if cnt_2 != 6:
            six_symb.append(i) 
            cnt_2 += 1
        if cnt_2 == 6:
            write_csv(check_vowel(six_symb))    
            six_symb = [ ]
            cnt_2 = 0


def check_vowel(row):
    vowel = ['a','A','e','E','o','O','i','I','u','U']
    
    result = [ ]
    for word in row:
        w = word[0]
        if w in vowel:
            continue
        else:
            result.append(word)

    if len(result) != 6:
        result = []
        return result
    else:
        return result


def write_csv(d):
    with open('changed_random_data.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow(d)
    

def main():
    prepare_data()



if __name__ == "__main__":
    main()
    