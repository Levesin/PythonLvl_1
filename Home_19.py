# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class auto:
    brand = "Toyota"
    age = 6
    color = "Blue"
    makr = "Сrossover"
    weight = 1800

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

    def birthday(self):
        self.age+=1




call_auto = auto(8,"Mazda","coupe")

call_auto.move()
call_auto.stop()
call_auto.birthday()
print(call_auto.age)
call_auto.birthday()
print(call_auto.age)
call_auto.birthday()
print(call_auto.age)