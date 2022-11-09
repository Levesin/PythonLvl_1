# Прочитать сохранённый json-файл из задания №16 и записать данные
# на диск в csv-файл, первой строкой которого озаглавив каждый
# столбец и добавив новый столбец “телефон”.


import json
import csv
from pprint import pprint




with open("umba_tumba.json", "r", encoding="utf-8") as f:
    chitaem = json.load(f)
    pprint(chitaem)
zaglav = ["id",'Имя','Возраст','Телефон']
with open("umba_tumba.csv", "w", encoding="utf-8") as f:
    file_csv = csv.writer(f)

    file_csv.writerow(zaglav)
    file_csv.writerow(chitaem['111111'])
    file_csv.writerow(chitaem['222222'])
    file_csv.writerow(chitaem['333333'])
    file_csv.writerow(chitaem['444444'])
    file_csv.writerow(chitaem['555555'])
    file_csv.writerow(chitaem['666666'])














# with open("umba_tumba.csv", "w", newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     for line in chitaem:
#         writer.writerow(line)
