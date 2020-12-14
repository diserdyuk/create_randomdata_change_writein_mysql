'''
скрипт

1) считывает содержимое файла в формате csv 
2) создает программно базу данных mysql
3) сохраняет все данные в таблицу
4) средствами sql удаляет записи, в которых во втором столбце первый символ цифра
'''

import csv
import mysql.connector 



mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'denis',
    password = 'diS031087!',
    database = 'dbrandnums'
)

mycursor = mydb.cursor()

''' create dbrand '''
# mycursor.execute('CREATE DATABASE dbrandnums')    

''' show dbrand '''
# mycursor.execute('SHOW DATABASES')    
# for db in mycursor:     
#     print(db)    # ('dbrandnums',)

''' created id & 6 columns '''
# mycursor.execute('CREATE TABLE dbrandnums (id INT AUTO_INCREMENT PRIMARY KEY, one VARCHAR(255), two VARCHAR(255), three VARCHAR(255), four VARCHAR(255), five VARCHAR(255), six VARCHAR(255))')

# ''' views tables '''
# mycursor.execute('SHOW TABLES')    
# for t in mycursor:
#     print(t)    #  ('nums',)    

'''views datas in table'''
# mycursor.execute("SELECT * FROM dbrandnums")    
# myresult = mycursor.fetchall()
# for res in myresult:
#     print(res)    # res -> (1, 'bEE267C8', '3E1A5A0D', 'D7Bb330E', '28ca9aCD', 'B64cA3eC', 'd68BFdCf') ...


''' sql удаляет записи, в которых во втором столбце первый символ цифра '''
''' after https://i.imgur.com/kJGi11c.png, before https://i.imgur.com/xC2ckfB.png '''
mycursor.execute("UPDATE dbrandnums SET two = ' ' WHERE two REGEXP '^[0-9]'")
mydb.commit()


def main():
    pass
    # csv_file = 'random_data.csv'

    # with open(csv_file, 'r') as f:
    #     read = csv.reader(f)
    #     for i in read:    # i -> ['bEE267C8', '3E1A5A0D', 'D7Bb330E', '28ca9aCD', 'B64cA3eC', 'd68BFdCf'] ...
    #         sql = 'INSERT INTO dbrandnums (one, two, three, four, five, six) VALUES (%s, %s, %s, %s, %s, %s)'
    #         val = i
    #         mycursor.execute(sql, val)

    #         mydb.commit()



if __name__ == "__main__":
    main()
