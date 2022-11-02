# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.
one_str = input("Позишен намбер ван: ")
two_str = input("Позишен намбер ту: ")
thee_str = input("Три: ")
four_str = input("Четыре: ")
lines = [one_str,two_str,thee_str,four_str]


file = open("test.txt", "w")
file.write(one_str + '\n')
file.write(two_str + '\n')
file.close()
file = open("test.txt", "a")
file.write(thee_str + '\n')
file.write(four_str + '\n')
file.close()
