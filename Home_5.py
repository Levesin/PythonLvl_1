# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for

while True:
    num = input("Введите число: ")
    if not num.isdigit() or int(num) == 0:
        print("Ошибка, повторите ввод")
        continue
# While
    num = int(num)
    i = 0
    sum = 0
    while i < num:
        i += 1
        if i % 3 == 0:
            continue
        else:
            sum += i**3
        print(sum)

    print("-"*50)

# For

    sum = 0
    for num in range(num):
        if num % 3 == 0:
            continue
        sum += num ** 3
        print(sum)

# Exit
    pakeda = input("Хотите выйти? (Y/Д) ")
    if pakeda.upper() in ('Y', 'Д'):
        break







