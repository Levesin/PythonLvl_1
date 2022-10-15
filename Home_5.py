# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for


while True:
    num = input("Введите число: ")
    if not num.isdigit() or int(num) == 0:
        print("Ошибка, повторите ввод")

    continue



    num = int(num)


    while shag <= num:
        shag = + 1
        if shag % 3 == 0:
            continue
    else:

     a = shag ** 3
     suma = a + suma

     print(suma)
     break


