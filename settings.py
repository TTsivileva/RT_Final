import os
import random
import string

valid_email = 'tebalashova@gmail.com'
valid_password = 'Enrfdghele&09'
valid_login = 'rtkid_1688036056193'
valid_phone = '9265881010'
valid_ls = '655798899999'
not_valid_email = 'tiana536@gmail.com'
not_valid_phone = '9856746655'
not_valid_login = 'rtkid_1688036056193'
not_valid_ls = '655798899991'
not_valid_password = 'ZXCVBn&09'
new_email = 'tebalashova@mail.ru'
cyrillic = ['К','З','Н','Р','С','Ч','М']
cyrillic2 = ''.join(random.choices(cyrillic, k=1))
print(cyrillic2)
def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
special = ''.join(random.choices(string.punctuation , k=9))
print(special)
eng = ''.join(random.choices(string.ascii_uppercase+string.ascii_letters, k=9))
number = ''.join(random.choices(string.digits, k=9))
numb_abc = ''.join(random.choices(string.ascii_letters+string.digits, k=9))
sym255 = ''.join(random.choices(string.ascii_letters, k=255))
sym1001 = ''.join(random.choices(string.ascii_letters, k=1001))
names = ["Ирина", "Наталья", "Ольга", "Жанна", "Катерина", "Кристина"]
name = ''.join(random.choices(names, k=1))
lastnames = ['Котикова', 'Собакина', 'Хомякова', 'Зайкина', 'Коровина', 'Канарейкина']
lastname = ''.join(random.choices(lastnames, k=1))