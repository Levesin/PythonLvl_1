# Написать декоратор к 2-м любым функциям, который бы считал и
# выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()


def time_decar(func_2):
    def timecod():
        import time
        from datetime import datetime
        start_time = datetime.now()
        func_2()
        time.sleep(0)
        print("Время выполнения:", datetime.now() - start_time)
    return timecod


@time_decar
def func_1():
    while True:
        num = input("Введите число: ")
        if not num.isdigit() or int(num) == 0:
            print("Ошибка, повторите ввод")
            continue
        num = int(num)
        return
@time_decar
def exit():
    while True:
       pakeda = input("Хотите выйти? (Y/Д) ")
       if pakeda.upper() in ('Y', 'Д'):
        break

func_1()

exit()