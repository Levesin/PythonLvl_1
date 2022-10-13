name = input("Введите ваше имя: ")

while True:
    age = input("Введите ваш возраст: ")
    if not age.isdigit() or 0 >= int(age):
        print("Ошибка, повторите ввод")
        continue

    if 0 < int(age) < 10:
      print("Привет, Шкет", name)

    elif 10 < int(age) < 18 + 1:
        print("Как жизнь,", name, "?")

    elif 18 < int(age) < 100 + 1:
        print("Что желаете,", name, "?")

    elif 100 < int(age):
        print(name, ", вы лжете - в наше время столько не живут...")

    pakeda = input("Хотите выйти? (Y/Д) ")
    if pakeda.upper() in ('Y', 'Д'):
        break


