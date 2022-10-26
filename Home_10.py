# Дан список состоящий из данных разного типа.
# Вернуть новый список, где при помощи функции map() каждый элемент типа int
# первоначального списка приведён к типу str, элементы всех остальных типов
# передаются в новый список без изменения их типа.
# В качестве функции в map использовать lambda

list_1 = [1, "Yes", 2, "No"]

#new_listr = map(lambda x: str(x) , list_1)
#print(list(new_listr))

new_list = map(lambda x: x.remove(x) if x == 1 else x, list_1)
print(list(new_list))
