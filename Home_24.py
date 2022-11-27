# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень
# и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких
# исключений, как минимум деление на 0.
# Создать своё исключение, к примеру возведение в отрицательную степень.
class ErrorDegree(Exception):
    ...



class calculator():
        def __init__(self, x, y, s):
            try:

                self.x = int(x)
                self.y = int(y)
                self.s = int(s)

            except (ValueError, AttributeError):
                print("Ошибочка")

        def __add__(self):
            try:

                resault = self.x + self.y
                return resault

            except (ValueError, AttributeError):
                print("Ошибочка")


        def __sub__(self):
            try:

                resault = self.x - self.y
                return resault

            except (ValueError, AttributeError):
                print("Ошибочка")

        def multi(self):
            try:

                resault = self.x * self.y
                return resault

            except (ValueError, AttributeError):
                print("Ошибочка")

        def division(self):
            try:

                resault = self.x // self.y
                return resault

            except ZeroDivisionError:
                resault = 0
                print(resault)

            except (ValueError, AttributeError):
                print("Ошибочка")


        def exponentiation(self):
            try:

                x = self.x ** self.s
                y = self.y ** self.s
                return print(f"Результат первого возведения в степень {x},\n"
                             f"Результат второго возведения в степень {y}")

            except ErrorDegree:
                print("Отрицательная степень")
            except (ValueError, AttributeError):
                print("Ошибочка")


        def root(self):
            try:
                quatro = 0.5
                x = self.x ** quatro
                y = self.y ** quatro
                return print("Квадратный корень числа", self.x, f"равен = {x},\n"
                             "Квадратный корень числа", self.y, f"равен = {y}")
            except (ValueError, AttributeError):
                print("Ошибочка")




x = input("Первое число x: ")
y = input("Второе число y: ")
s = input("Степень s:")
z = input("1.Сложение \n"
          "2.Вычитание \n"
          "3.Умножение \n"
          "4.Деление  \n"
          "5.Возведение в степень \n"
          "6.Извлечение квадраного корня \n"
          "Для выбора операции введите ее номер: ")

call_calcu = calculator(x, y, s)
z = int(z)
if z == 1:
    print(call_calcu.__add__())

elif z == 2:
    print(call_calcu.__sub__())

elif z == 3:
    print(call_calcu.multi())

elif z == 4:
    print(call_calcu.division())

elif z == 5:
    print(call_calcu.exponentiation())

elif z == 6:
    print(call_calcu.root())
