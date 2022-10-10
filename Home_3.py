
Predlog = input("Предложение из 2-х слов: " )
ones = Predlog.split()[0]    #ones - первое слово
twos = Predlog.split()[1]    #twos - второе слово
source_file = open('test.txt', 'w')

a = "! %s,%s ?" % (ones.upper()[::-1], twos.capitalize()[::-1])
print(a, file=source_file)

b = "! {0} {1} ?".format(ones.upper()[::-1], twos.capitalize()[::-1])
print(b, file=source_file)

c = (f'! {ones.upper()[::-1]} , {twos.capitalize()[::-1]} ?')
print(c, file=source_file)
source_file.close()
