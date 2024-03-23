tpl = (1, 3, 2)
tpl[0] = 500

'''
Попытка изменить значение элемента с индексом 0 в кортеже
Интерпретатор завершит выполнение программы с ошибкой:
измениять элементы объекта типа tuple нельзя

tpl[0] = 500
TypeError: 'tuple' object does not support item assignment
'''


package = ('2:00:01', 15000)
print(package) # Вывод в терминал: ('2:00:01', 15000)
print(type(package)) # Вывод в терминал: <class 'tuple'> 


# Функция tuple() преобразует строку с текстом о достижении в кортеж
achievement = 'Отлично!'
tpl_achiv = tuple(achievement)
print(tpl_achiv) #Вывод в терминал: ('О', 'т', 'л', 'и', 'ч', 'н', 'о', '!')


# Если передать в функцию неитерируемый объект (например, число),
# Python сообщит, что не может выполнить такое преобразование.
steps = 15000
tpl_steps = tuple(15000) #Вывод в терминал: TypeError: 'int' object is not iterable


# Литеральное объявление кортежа
package_1 = ('2:00:01', 15000)

# Значения, перечисленные через запятую и присвоеные одной переменной,
# будут упакованы в кортеж
package_2 = '2:00:01', 15000

print(package_1)
# Вывод в терминал: ('2:00:01', 15000)
print(type(package_1))
# Вывод в терминал: <class 'tuple'>

print(package_2)
# Вывод в терминал: ('2:00:01', 15000)
print(type(package_2))
# Вывод в терминал: <class 'tuple'>


tpl_steps = 15000,
steps = 15000

print(type(tpl_steps))
# Вывод в терминал: <class 'tuple'>
print(type(steps))
# Вывод в терминал: <class 'int'> 

package = ('2:00:01', 15000)

time, steps = package

print(steps)
# Вывод в терминал: 15000
print(time)
# Вывод в терминал: '2:00:01' 



not_srtd_tpl = (5**5, 5**2, 5**1, 5**4, 5**0, 5**3)
print(not_srtd_tpl)
# Вывод в терминал: (3125, 25, 5, 625, 1, 125)

srtd_tpl = sorted(not_srtd_tpl)
print(srtd_tpl)
# Вывод в терминал: [1, 5, 25, 125, 625, 3125]
# Отсортировали, но вместо кортежа получили список.
# Исходный кортеж остался неизменённым. 


week = (
    'Понедельник', 'Втроник', 'Среда',
    'Четверг', 'Пятница', 'Суббота', 'Воскресенье'
)

del week

print(week)
'''
Traceback (most recent call last):
  File "D:/Dev/course/examples/main.py", line 5, in <module>
    print(week)
NameError: name 'week' is not defined 
'''