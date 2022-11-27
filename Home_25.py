#Создать генератор геометрической прогрессии

def MyGenerator(n, b_first, q):
    print(b_first)
    b_prev = b_first
    for i in range(1, n):
        b_cur = b_prev * q
        print(b_cur)
        b_prev = b_cur
    yield print("Результат: ", b_prev)



n = int(input('Введите число элементов прогрессии: '))
b_first = int(input('Введите первый элемент прогрессии: '))
q = int(input('Введите знаменатель прогрессии: '))

a = MyGenerator(n, b_first, q)
for item in a:
    print(item)