# Сделать программу в виде функций в которой нужно будет угадывать число.
import random
value_random = random.randint(0, 100)
print(value_random)
attempts = 0
print("Приветики, угадаешь число от 0 до 100? У тебя 10 попыток =)")
for i in range(10):
    attempts_2 = int(input("Введи число сюда => "))
    if attempts_2 > value_random:
        print("Акела промохнулся. Попробуй меньшее число ;) ")
    elif attempts_2 < value_random:
        print("К сожелению мимо. Давай еще разок =) ")
    else:
        print("Вы угадали число и ГЛАВНЫЙ ПРИЗ ААААААААААААААААААААААААж ничего =) ")
        break
    attempts += 1
if attempts >= 10:
    print("Попытки закончились 10/10. Ну ничего в любви повезет. ", sep="")
    print("А число было такое: ", value_random, "Нэ рООсстраивайся)" )
