# Прочитать сохранённый json-файл из задания №16 и записать данные
# на диск в csv-файл, первой строкой которого озаглавив каждый
# столбец и добавив новый столбец “телефон”.


import json
import csv
from pprint import pprint




with open("umba_tumba.json", "r", encoding="utf-8") as f:
    chitaem = json.load(f)
    pprint(chitaem)
zaglav = ['Имя','Возраст','Телефон']
with open("umba_tumba.csv", "w", encoding="utf-8") as f:
    file_csv = csv.writer(f)
    file_csv.writerow(zaglav)
    number = 38099000
    for key in chitaem:
      file_csv.writerow(chitaem[key]+[number])
      number = number + 53

















