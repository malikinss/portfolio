'''
TODO: Write a function get_month(language, number), which takes as input two arguments language - language ru or en and number - month number (from 1 to 12) and returns the name of the month in Russian or English.
'''


def get_month(language, number):
    month_ru = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
    month_eng = ['january','february','march','april','may','june','july','august','september','october','november','december']
    

    if language == 'ru':
        month_name = month_ru[number - 1]
    
    elif language == 'eng':
        month_name = month_eng[number - 1]
    
    return month_name    



language = input()
number_of_month = int(input())

print(get_month(language, number_of_month))