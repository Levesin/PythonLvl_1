# Дан список состоящий из данных разного типа.
# Вернуть новый список, где при помощи функции map() каждый элемент типа int
# первоначального списка приведён к типу str, элементы всех остальных типов
# передаются в новый список без изменения их типа.
# В качестве функции в map использовать lambda

list_1 = [1, 2, '3', 'forth', 'end', 99, True, None]
new_listr = map(lambda x: str(x) if type(x) == int else x, list_1)
print(list(new_listr))
