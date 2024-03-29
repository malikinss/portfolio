# Последовательность типа list (список); 
# значения элементов списка - числа типа float.
movie_ratings = [4.7, 5.0, 4.3, 3.8]

# Последовательность типа list (список); 
# значения элементов списка - строки (str)
movies = ['Матрица', 'Хакеры', 'Трон']

# Последовательность типа cтрока (str); 
# элементы этой последовательности - символы, составляющие строку
name_movie = 'Джонни Мнемоник' 

# Последовательности могут иметь элементы разных типов
# Например, одновременно элемент типа str и float
movie_info = ['Трон', 4.7]
# Элементами последовательности могут быть другие последовательности
movies_info = [['Трон', 4.7], ['Хакеры', 5.0], ['Матрица', 4.5]]

# Чтобы получить значение определённого элемента, 
# его индекс следует указать в квадратных скобках после имени последовательности.
print(movie_ratings[2])
# Вывод в терминал: 4.3

print(name_movie[0])
# Вывод в терминал: Д

# При попытке обратиться несуществующему элементу интерпретатор вернет ошибку:
#print(movies[10])
# Вывод в терминал: IndexError: list index out of range

print([1, 2, 3] < [1, 2, 4])
# Вывод в терминал: True

print('Слон' < 'слон')
# Вывод в терминал: True
# Элемент с индексом 0 первой строки - это буквенный символ в верхнем регистре,
# его числовой код меньше той же буквы в нижнем регистре

print('1b' > 'fb')
# Вывод в терминал: False
# Элемент с индексом 0 первой строки - цифра. Её числовой код меньше, чем у букв. 

print('a' < 'ADC')
# Вывод в терминал: False

print([1, 2, 4] > [1, 2, 3, 4])
# Вывод в терминал: True 

my_string = '12345'
print(max(my_string))
# Вывод в терминал: 5

my_list = ['abc', 'Abc']
print(min(my_list))
# Вывод в терминал: Abc 

first_baggage_list = ['Диван', 'Чемодан', 'Саквояж', 'Картина']

second_baggage_list= ['Корзина', 'Картонка', 'Маленькая собачонка']

full_baggage_list = first_baggage_list + second_baggage_list
print(full_baggage_list)
# Вывод в терминал: 
# ['Диван', 'Чемодан', 'Саквояж', 'Картина', 'Корзина', 'Картонка', 'Маленькая собачонка'] 

pump = 'насос' * 4
print(pump)
# Вывод в терминал: насоснасоснасоснасос

small_baggage_list = ['Корзина', 'Картонка', 'Маленькая собачонка']
double_baggage_list = small_baggage_list * 2
print(double_baggage_list)

# Вывод в терминал:
# ['Корзина', 'Картонка', 'Маленькая собачонка', 'Корзина', 'Картонка', 'Маленькая собачонка'] 

movies = ['Матрица', 'Хакеры', 'Трон', 'Тихушники', 'Сеть']
print(len(movies))
# Вывод в терминал: 5 

movies = ['Матрица', 'Хакеры', 'Трон', 'Тихушники', 'Сеть']
# Шаг должен иметь отрицательное зачение
print(movies[5:0:-1])
# Вывод в терминал: ['Сеть', 'Тихушники', 'Трон', 'Хакеры']

# Можно не указывать границы, а задать только отрицательное значение шага
print(movies[::-1])
# Вывод в терминал: ['Сеть', 'Тихушники', 'Трон', 'Хакеры', 'Матрица']
# Инвертирован весь список 

name_movie = 'Джонни Мнемоник'
# Взять срез с седьмого элемента и до конца последовательности
print(name_movie[7:])
# Вывод в терминал: Мнемоник

name_movie = 'Джонни Мнемоник'
# Взять срез от начала последовательности до шестого элемента (не включая шестой)
print(name_movie[:6])
# Вывод в терминал: Джонни 

movies = ['Матрица', 'Хакеры', 'Трон', 'Тихушники', 'Сеть']
print(movies[0:5:2])
# Вывод в терминал: ['Матрица', 'Трон', 'Сеть'] 

movie_ratings = [4.7, 5.0, 4.3, 3.1]
print(4.7 in movie_ratings)
# Вывод в терминал: True

name_movie = 'Джонни Мнемоник'
print('ж' in name_movie)
# Вывод в терминал: True 

full_baggage_list = ['Диван', 'Чемодан', 'Саквояж', 'Картина', 'Корзина', 'Картонка']

# Если собачонки нет
if 'Маленькая собачонка' not in full_baggage_list:
    # ...устраиваем скандал:
    print('— Товарищи! Где собачонка?') 

num_allowed_views = 5

while num_allowed_views != 0:  # Пока количество разрешенных просмотров не равно 0
    print('Включить фильм "Матрица"')  # В терминал будет выводиться эта фраза
    # После каждого вывода число разрешённых показов уменьшаем на единицу
    num_allowed_views -= 1


movie_ratings = [4.7, 5.0, 4.3, 3.1]

# Вне цикла объявляем переменную-счётчик
i = 0
while i < len(movie_ratings):
    # Вместо индекса элемента подставляем переменную-счётчик
    if movie_ratings[i] > 4.7:
        # Код обработчика.
        ...
    # После выполнения кода
    # увеличиваем счётчик на единицу
    i += 1
    # И цикл выполнит следующую итерацию,
    # если условие, указанное после while, истинно. 

recommended_movies = [
    'Хатико', '23', 'Достучаться до небес', 'Хакеры', 'Трон', '1408'
]

print(dir(recommended_movies))
# Вывод в терминал:
'''['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
'__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']'''

movie_ratings = [4.7, 5.0, 4.3, 3.1]

# Переменная rating поочерёдно принимает элементы
# последовательности movie_ratings
for rating in movie_ratings:
    # Теперь переменную rating можно обработать в теле цикла
    if rating > 4.7:
        print('Фильм крут')

rng = range(1, 10, 2)
print(rng)

# Вывод в терминал: range(1, 10, 2)
# А где числа-то?

rng = range(1, 10, 2)
print(rng[3])

# Вывод в терминал: 7 

movies = ['Матрица', 'Хакеры', 'Трон', 'Тихушники', 'Сеть']
movie_ratings = [4.7, 5.0, 4.3, 4.9, 3.4]

# В качестве верхней границы диапазона 
# передаётся длина списка movies.
print('Рейтинг пользователей')
for index in range(len(movies)):
    print(movies[index]+':', movie_ratings[index])