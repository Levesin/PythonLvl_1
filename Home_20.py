# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение
# обязательного атрибута max_load.
# Создать по 2 объекта для каждого из классов truck и car,
# проверить все их методы и атрибуты.
import time

class Auto:
    brand = "Toyota"
    age = 6
    makr = "Сrossover"

    def __init__(self, age, brand, mark, color="Blue", weight=1800):
        self.age = age
        self.brand = brand
        self.makr = mark
        self.color = "Blue"
        self.weight = "1800"


    def move(self):
        print("move")

    def stop(self):
        print("stop")
#_________________________________________________________________________________
class Truck(Auto):
    def __init__(self, max_load):
        super().__init__(max_load, brand="Volvo", mark="24t")
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()


    def load(self):
        time.sleep(1)
        print("load...")
        time.sleep(1)
#_________________________________________________________________________________
class Car(Auto):
    def __init__(self, max_speed, max_load="Twenty minutes"):
        super().__init__(age=4, brand="Honda", mark="Hatchback",)
        self.max_speed = max_speed
        self.max_load = max_load
        print(max_load)

    def move(self):
        super().move()
        print("max speed is max_speed")


call_auto = Auto(8, "Mazda", "coupe")
call_auto.move()
call_auto.stop()

print("-"*50)

call_Truck = Truck("Twenty minutes")
call_two_Truck = Truck("Thirty minutes")

call_Truck.move()
call_two_Truck.move()

call_Truck.load()
call_two_Truck.load()

print("-"*50)

call_Car = Car("140")
call_two_car = Car("180")

call_Car.move()
call_two_car.move()

