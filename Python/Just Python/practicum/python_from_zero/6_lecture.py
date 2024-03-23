name_movie = list('Матрица')
print(name_movie)
# Вывод в терминал: ['М', 'а', 'т', 'р', 'и', 'ц', 'а']

# Такая запись создаст пустой список:
movies = list()
print(movies)
# Вывод в терминал: [] 


# Литеральное объявление переменных int и float:
count = 5
proportion = 4.1

# А вот уже не литеральное объявление числа:
summa = count + proportion

# При литеральном объявлении строки последовательность символов замыкают в кавычки:
name = 'Игорь'
title = "McDucken’s"

# А нелитеральным объявлением будет, например, объявление строки через функцию:
proportion_str = str(proportion)

# Литералом для объявления списка будет 
# запись элементов через запятую в квадратных скобках
movies = ['Матрица', 'Хакеры', 'Трон']

# Литеральное объявление пустого списка
movie_ratings= [] 


movie_ratings= [4.7, 5.0, 4.3, 3.8]
# Объявляем новый список, в него будем складывать измененные оценки
new_movie_ratings = []

# Перебор списка в цикле:
for rating in movie_ratings:
    rating += 0.2 # Значение элемента исходного списка увеличивается на 0.2
    new_movie_ratings.append(rating) # Значение добавляется в новый список

print(new_movie_ratings)
# Вывод в терминал: [4.9, 5.2, 4.5, 4.0]
# Хм, неловко вышло: накрутили рейтинг так, что получили 5.2 по пятибалльной шкале.
# TODO Ладно, позже починим. 


movie_ratings= [4.7, 5.0, 4.3, 3.8]
new_movie_ratings = [rating + 0.2 for rating in movie_ratings]
print(new_movie_ratings)
# Вывод в терминал: [4.9, 5.2, 4.5, 4.0] 


movie_ratings= [4.7, 5.0, 4.3, 3.8]
new_movie_ratings = [
   rating + 0.2 if rating < 4.9 else rating for rating in movie_ratings
]
print(new_movie_ratings)
# Вывод в терминал: [4.9, 5.0, 4.5, 4.0] 


movie_ratings= [4.7, 5.0, 4.3, 3.8]
new_movie_ratings = [rating for rating in movie_ratings if rating > 4.5]
print(new_movie_ratings)
# Вывод в терминал:[4.7, 5.0] 


week = [
    'Понедельник', 'Втроник', 'Среда', 
    'Четверг', 'Пятница', 'Суббота', 'Воскресенье'
]

mon, tue, wed, thu, fri, sat, sun = week

print(wed)
# Вывод в терминал: Среда 


week = [
    'Понедельник', 'Втроник', 'Среда', 
    'Четверг', 'Пятница', 'Суббота', 'Воскресенье'
]

mon, tue, wed, thu, fri, sun = week

print(wed)
# Вывод в терминал: ValueError: too many values to unpack (expected 6) 


movies = ['Матрица', 'Хакеры', 'Трон']
movies.append('Тихушники')
print(movies)
# Вывод в терминал: ['Матрица', 'Хакеры', 'Трон', 'Тихушники'] 


movies = ['Матрица', 'Хакеры', 'Трон']

# Бессмысленно присваивать результат работы метода переменной
new_movies = movies.append('Тихушники')

print(new_movies)
# Вывод в терминал: None

# Метод и не должен был ничего возвращать, он молодец, он выполнил свою работу: 
# изменил исходный список. 
print(movies)
# Вывод в терминал: ['Матрица', 'Хакеры', 'Трон', 'Тихушники'] 


movie_ratings = [4.7, 5.0, 4.3, 3.8]
movies = ['Матрица', 'Хакеры', 'Трон']
print(id(movies))
# Вывод в терминал: 2217539360448

movies.extend(movie_ratings)
print(movies)
# Вывод в терминал: ['Матрица', 'Хакеры', 'Трон', 4.7, 5.0, 4.3, 3.8]
print(id(movies))
# Вывод в терминал: 2217539360448


movies = ['Матрица', 'Хакеры', 'Трон']
movies.insert(1, 'Тихушники')
print(movies)
# Вывод в терминал: ['Матрица', 'Тихушники', 'Хакеры', 'Трон'] 


movies = ['Матрица', 'Тихушники', 'Хакеры', 'Трон']
movies.remove('Хакеры')
print(movies)
# Вывод в терминал: ['Матрица', 'Тихушники', 'Трон']

# Попытка удалить несуществующий объект
# вызовет исключение
movies.remove('Сеть')
# Вывод в терминал: ValueError: list.remove(x): x not in list 


movies = ['Матрица', 'Тихушники', 'Хакеры', 'Трон']
movie = movies.pop(2)
print(movie)
# Вывод в терминал: Хакеры
print(movies)
# Вывод в терминал: ['Матрица', 'Тихушники', 'Трон'] 


movie_ratings= [4.7, 5.0, 4.3, 3.8]
rating = movie_ratings.index(4.3)
print(rating)
# Вывод в терминал: 2 


movie_ratings= [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
rating_count = movie_ratings.count(4.7)
print(rating_count)
# Вывод в терминал: 2 


movie_ratings= [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
movie_ratings.sort()
print(movie_ratings)
# Вывод в терминал: [3.8, 4.1, 4.3, 4.7, 4.7, 5.0]

movies = ['Матрица', 'Хакеры', 'Трон']
movies.sort(reverse = True)
print(movies)
# Вывод в терминал: ['Хакеры', 'Трон', 'Матрица'] 


movie_ratings= [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
print(id(movie_ratings))
# Вывод в терминал: 27337512

# Развоврот списка методом reverse()
movie_ratings.reverse()
print(id(movie_ratings))
# Вывод в терминал: 27337512

print(movie_ratings)
# Вывод в терминал: [4.1, 4.7, 3.8, 4.3, 5.0, 4.7] 


movie_ratings= [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
print(id(movie_ratings))
# Вывод в терминал: 2028420139712

# Разворот списка с помощью среза
movie_ratings = movie_ratings[::-1]
print(movie_ratings)
# Вывод в терминал: [4.1, 4.7, 3.8, 4.3, 5.0, 4.7]

# Список инвертирован, но...
print(id(movie_ratings))
# Вывод в терминал: 2028420159168
# Это уже другой объект! 


movie_ratings= [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
copy_movie_ratings = movie_ratings.copy()
print(id(movie_ratings))
# Вывод в терминал: 38282024

print(id(copy_movie_ratings))
# Вывод в терминал: 38281640

# Применим сортировку к исходному списку
movie_ratings.sort()
print(movie_ratings)
# Вывод в терминал: [3.8, 4.1, 4.3, 4.7, 4.7, 5.0]

# Элементы списка-копии остались неотсортированными
print(copy_movie_ratings)
# Вывод в терминал: [4.7, 5.0, 4.3, 3.8, 4.7, 4.1] 


movie_ratings= [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
movie_ratings.clear()
print(movie_ratings)
# Вывод в терминал: [] 