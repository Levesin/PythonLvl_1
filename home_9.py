# Написать лямбда-функцию определяющую чётное/нечётное.
# Функция принимает параметр (число) и если чётное,
# то выдаёт слово “чётное”, если нет - то “не чётное”.

while True:
    num = input("Введите число: ")
    if not num.isdigit() or int(num) == 0:
        print("Ошибка, повторите ввод")
        continue
    num = int(num)

    trynot = lambda num: "Четное" if num % 2 == 0 else "Нечетное"
    print(trynot(num))

    pakeda = input("Хотите выйти? (Y/Д) ")
    if pakeda.upper() in ('Y', 'Д'):
        break

