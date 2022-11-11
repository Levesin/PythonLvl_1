# Прочитать сохранённый csv-файл из задания №17 и сохранить данные
# в excel-файл, кроме возраста – столбец с этими данными не нужен.
import csv
import openpyxl



with open("umba_tumba.csv", "r", encoding="utf-8") as f:
    open_data = csv.reader(f)

    print(open_data)
    for row in open_data:
        print(row)







