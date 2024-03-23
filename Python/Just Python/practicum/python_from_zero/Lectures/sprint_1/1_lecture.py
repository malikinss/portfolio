x = 231  # Готово, x - это int
y = 0  # И y - это int
z = -100  # z - тоже int

# Согласно правилам оформления кода PEP8 операторы отделяются пробелами.
# Отсутствие пробелов не приведёт к ошибке, но правила лучше соблюдать.
x = 40 - 11
print(x)
# Вывод в терминал: 29

x = 7 + 12
print(x)
# Вывод в терминал: 19

# К предыдущему значению steps прибавляем единицу и полученное значение
# перезаписываем в ту же самую переменную steps
steps = 0
steps = steps + 1 

# Выражение
steps = steps + 1
# можно записать через комбинированный оператор присваивания:
steps += 1

x = 5 * 2
print(x)
# Вывод в терминал: 10 

x = 5**2
print(x)
# Вывод в терминал: 25

y = 22 // 3
print(y)
# Вывод в терминал: 7 
# Это результат деления с остатком. 
# Возвращается только неполное частное.

z = 2 // 3
print(z)
# Вывод в терминал: 0
# Неполное частное - 0, остаток - 2, но он не возвращается.

x = 11 % 3
print(x)
# Вывод в терминал: 2

x = 20 / 2
print(x)
# Вывод в терминал: 10.0

x = 11 / 3
print(x)
# Вывод в терминал: 3.6666666666666665

twelve = 4 * 3
print('twelve = ', twelve)

two = 4 * 3
print('two = ', two)
print(type(two))

# Всё это переменные типа float
a = 2.345
b = 2.
c = 2.0
x = .07
y = 0.07 

excellent = 0.4 + 0.4 + 0.2
print('excellent = ', excellent)

badly = 0.3 + 0.3 + 0.3 + 0.1
print('badly = ', badly)



input_data_1 = 3.3
input_data_2 = 4.18

input_data = input_data_1 + input_data_2
print(input_data)

input_data = (input_data_1 * 100 + input_data_2 * 100) / 100
print(input_data)



day_1 = 1.434
day_2 = 2.12
day_3 = 1.632
day_4 = 5.59
day_5 = 2.542
day_6 = 1.1
day_7 = 1.324

week_dist = ((day_1 * 1000) + (day_2 * 1000) + (day_3 * 1000) + (day_4 * 1000) + (day_5 * 1000) + (day_6 * 1000) + (day_7 * 1000)) / 1000
print(week_dist)

days_dist = [1.434, 2.12, 1.632, 5.59, 2.542, 1.1, 1.324]
week_dist = 0
rounder = 1000

for day in days_dist:
    week_dist += (day * rounder)
week_dist  /= rounder

print(week_dist)

from decimal import Decimal

x = Decimal('3.3')
print(type(x))

i = 3.3 + 4.1
print(i)

i = Decimal('3.3') + Decimal('4.1')
print(i)

print(1 + 2*3)
# Вывод в терминал: 7 
# Но 
print((1 + 2) * 3)
# Вывод в терминал: 9 




