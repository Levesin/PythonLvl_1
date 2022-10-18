# Сделать программу в виде функций в которой нужно будет угадывать число.
def cycle():
    attempts = 0
    while True:
        attempts_two = input("Введите чило: ")
        if not attempts_two.isdigit():
            print("Ошибка, повторите ввод")
            continue
        attempts_two = int(attempts_two)
        for i in range(10):
          if attempts_two > value_random:
            print("Акела промохнулся. Попробуй МЕНЬШЕ число ;) ")
          elif attempts_two < value_random:
            print("К сожелению мимо. Теперь чутка БОЛЬШЕ =) ")
          else:
            print("Вы угадали число и ГЛАВНЫЙ ПРИЗ ААААААААААААААААААААААААж ничего =) ")
          break
        attempts += 1
        if attempts >= 10:
         print("Попытки закончились 10/10. Ну ничего в любви повезет. ", sep="")
         print("А число было такое: ", value_random, "Нэ рООсстраивайся)")
         exit()
         break


def exit ():
 while True:
    pakeda = input("Хотите выйти? (Y/Д) ")
    if pakeda.upper() in ('Y', 'Д'):
     break


import random
value_random = random.randint(0, 100)
print("Приветики, угадаешь число от 0 до 100? У тебя 10 попыток =)")
cycle()



