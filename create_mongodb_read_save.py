'''
cкрипт 

1) считывает csv файл 
2) сохраняет данные в коллекцию 
3) удаляет записи, в которых в третьем столбце первый символ буква
'''

import csv
from pymongo import MongoClient



cluster = MongoClient("mongodb+srv://Denis:<password>@cluster0.xsmy8.mongodb.net/randomdata?retryWrites=true&w=majority")

db = cluster['randomdata']
collection = db['randomcoll']    


''' удаление записей в которых в третьем столбце, первый символ буква '''
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

cnt = 1
while cnt <= 10:
    for i in collection.find({'_id':cnt},{'three'}):
        if i['three'][0] in alphabet:
            collection.update_one({'_id':cnt},{'$set' :{'three':' '}})
            cnt += 1
        else:
            cnt += 1
            continue
    

def main():
    pass
    
    ''' запись данных в бд ''' 
    # csv_file = 'random_data.csv'
    # with open(csv_file, 'r') as f:
    #     read = csv.reader(f)
        
        # cnt = 1
        # for i in read:    # i -> ['bEE267C8', '3E1A5A0D', 'D7Bb330E', '28ca9aCD', 'B64cA3eC', 'd68BFdCf'] ...                print(y)
        #     post = {'_id': cnt, 'one': i[0], 'two': i[1], 'three': i[2], 'four': i[3],'five': i[4],'six': i[5]}
        #     collection.insert_one(post)
        #     cnt += 1



if __name__ == "__main__":
    main()