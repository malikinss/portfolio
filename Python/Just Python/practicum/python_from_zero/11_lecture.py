def best_function_in_this_code():     # Объявление функции
    print('Других функций тут нет!')  # Тело функции

best_function_in_this_code()          # Вызов функции
best_function_in_this_code()          # Ещё один вызов функции

# В результате двух вызовов функции будет напечатано: 
# Других функций тут нет!
# Других функций тут нет! 


# Параметры функции - а и b
def never_print_result(a, b):
    pass

def never_print_result(a, b):
    ...

# Вызываем функцию с аргументами 5 и 4
never_print_result(5, 4) 



rating = 3.0

if rating > 4.7:
    print('Фильм крут')
elif rating > 3.5:
    print('Смотреть можно')
else:
    print('Так себе киношечка')
print('Проверка окончена')


def print_recommendation(rating):
    if rating > 4.7:
        return 'Фильм крут'
    if rating > 3.5:
        return 'Смотреть можно'
    # Если не сработало ни одно условие -
    # функция вернёт это сообщение:
    return 'Так себе киношечка'

result = print_recommendation(4.1)

print(result) 


def super_print(movies):
    print('Подготовка к печати')
    print(movies)
    print('Готово!')

movies_names = ['Хакеры', 'Сеть', 'Трон', 'Матрица']
# Вызов функции не нужно передавать в переменную:
# функция ничего не вернёт, записывать в переменную нечего.
super_print(movies_names)
# Вывод в терминал:
# Подготовка к печати 
# ['Хакеры', 'Сеть', 'Трон', 'Матрица'] 
# Готово! 


def get_mod_diff(a, b):
    """Функция возвращает результат разницы полученных значений по модулю."""
    # Функция abs вернет значение по модулю
    diff = abs(a - b)
    return diff

x = 3
y = 4
print(get_mod_diff(x))
# Вывод в терминал: TypeError: get_mod_diff() missing 1 required positional argument: 'b' 


# При указании значения по умолчанию 
# пробелы вокруг оператора в выражении b=1 не нужны. Так говорит PEP8.
def get_mod_diff(a, b=1):
    """Функция возвращает результат разницы полученных значений по модулю."""
    diff = abs(a - b)
    return diff

x = 3
y = 4
print(get_mod_diff(x))
# Вывод в терминал: 2 


def get_mod_diff(a, b=1):
    """Функция возвращает результат разницы полученных значений по модулю."""
    diff = abs(a - b)
    return diff

x = 3
y = 4
# Именованные аргументы можно передавать в любом порядке, функция всё поймёт и примет.
print(get_mod_diff(b=y, a=x)) 



# В функции get_boost() первый аргумент - позиционный,
# а остальные будут распакованы в последовательность с именем ratings
def get_boost(coeff, *ratings):
    for rating in ratings:
        print(coeff + rating)

x = 0.2
# Вызываем функцию и передаём в неё шесть аргументов
# Первый аргумент будет передан в параметр coeff, 
# а остальные будут преобразованы в последовательность
get_boost(x, 4.3, 4.5, 3.0, 2.5, 4.7)
# Вывод в терминал:
# 4.5
# 4.7
# 3.2
# 2.7
# 4.9 


def print_profile(character, **info):
    print(f'Персонаж: {character}')
    for key, value in info.items():
        print(f'{key}: {value}')

print_profile('Spider-man',
              name='Питер Паркер',
              talent=['Суперсила', 'Паучье чутье', 'Паутина'],
              sity='Нью-Йорк')
# Вывод в терминал:
# Персонаж: Spider-man
# name: Питер Паркет
# talent: ['Суперсила', 'Паучье чутье', 'Паутина']
# sity: Нью-Йорк 