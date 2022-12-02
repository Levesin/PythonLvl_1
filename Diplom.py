#Дипломная работа
from Diplom_1 import Person_data

print("\n")
print("                ГЛАВНОЕ МЕНЮ:\n")
print("                1.Загрузка в базу данных\n")
print("                2.Расчет кол-во полных лет\n")
print("                3.Поиск по базе\n")
print("                4.Чтение базы данных\n")
print("                Для перехода по МЕНЮ введите номер операции\n")
print("                Хотите выйти? (Y/Д)\n")
i = 0
load_Per = Person_data()
while True:
    menu = input("Ввод: ")
    if menu.upper() in ('Y', 'Д'):
        break
    if not menu.isdigit() or int(menu) == 0:
        print("Вы ввели не корректный номер операции:", menu)
        continue

    menu = int(menu)
    if menu > 4:
        print("Такой оперции в МЕНЮ нет\n"
              "Потоврите ввод")

    elif menu == 2:
        name_year = input("Введите |Имя|: ")
        load_Per.years_preson(name_year)

        #Расчет полных лет

    elif menu == 3:
        # Поиск
        Search = input("Введите |Имя|: ")
        load_Per.unload_person(Search)

    elif menu == 4:
        load_Per.reading()
        # Чтение базы данных

    elif menu == 1 and i == 0:
        #Внесение в базу данных
        name = input("Введите Имя: ")
        surname = input("Введите Фамилию: ")
        patronymic = input("Введите Отчество: ")
        print("Формат даты: xx.yy.zz\nxx\yy\zz\nxx yy zz\nxx-yy-zz")
        date_birth = input("Введите дату рождения: ")
        date_death = input("Введите дату смерти: ")
        gender = input("Мужчина/Женщина: ")
        load_Per = Person_data(name, surname, patronymic, date_birth, date_death, gender)
        print(load_Per.load_person(name, surname, patronymic, date_birth, date_death, gender))
        i += 1

    elif menu == 1 and i > 0:
        print("_"*50)
        name_r = input("Введите Имя: ")
        surname_r = input("Введите Фамилию: ")
        patronymic_r = input("Введите Отчество: ")
        print("Формат даты: xx.yy.zz\nxx\yy\zz\nxx yy zz\nxx-yy-zz")
        date_birth_r = input("Введите дату рождения: ")
        date_death_r = input("Введите дату смерти: ")
        gender_r = input("Мужчина/Женщина: ")
        print(load_Per.twoload_person(name_r, surname_r, patronymic_r, date_birth_r, date_death_r, gender_r))

















