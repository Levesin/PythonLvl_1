# Прочитать сохранённый csv-файл из задания №17 и сохранить данные
# в excel-файл, кроме возраста – столбец с этими данными не нужен.
import csv

import openpyxl
from pprint import pprint

with open("umba_tumba.csv", "r", encoding="utf-8") as f:
    open_data = csv.reader(f)
    for row in open_data:
        pprint(row)


