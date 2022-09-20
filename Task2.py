import csv
from uuid import uuid4
import hashlib

salt = uuid4().hex


def new_hash():
    passwd = input('Введите пароль: ')
    result = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    print(f' В базе хранится строка: {result}')
    return result


def write_hash():
    result = new_hash()
    with open('hash_file.csv', mode='w') as w_file:
        file_write = csv.writer(w_file, delimiter=',', lineterminator='\r')
        file_write.writerow([salt, result])


def check_hash():
    check_result = new_hash()
    with open('hash_file.csv', mode='r') as r_file:
        file_read = csv.reader(r_file, delimiter=',')
        for i in file_read:
            if salt == i[0] and check_result == i[1]:
                print('Вы ввели правильный пароль')
            else:
                print('Пароль неверный')


write_hash()
check_hash()
