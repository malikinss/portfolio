
def is_cool_movie(rating):
    if rating > 4.7:
        print('Фильм крут')
    elif rating > 3.5:
        print('Смотреть можно')
    else:
        print('Так себе киношечка')

    print('Проверка окончена')

is_cool_movie(4.9)
is_cool_movie(4.1)
is_cool_movie(2.9)

def has_rating(rating):
    if rating: # Переменная rating равна 1.1, значит условие вернет True
        print('Оценка поставлена')
    else:
        print('У фильма нет оценки')

has_rating(0)
has_rating(1.1)