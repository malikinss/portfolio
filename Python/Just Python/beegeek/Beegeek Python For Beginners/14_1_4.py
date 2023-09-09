'''
TODO: Write a function number_to_words_ru(num), which takes a natural number num as an argument and returns its verbal description in Russian.
NOTE: Consider that the number 1 ≤ num ≤ 99.
'''


def number_to_words_ru(num):
    ed = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']
    od = ['одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
    ds = ['десять','двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    dss = [10,20,30,40,50,60,70,80,90]
    
    if num < 10:
        d = ed[num]
    elif num > 10 and num < 20:
        z = int(num % 10 - 1)
        d = od[z]
    elif num in dss:
        x = int(num // 10 - 1)
        d = ds[x]
    elif num > 19:
        a = int(num // 10 - 1)
        b = int(num % 10)
        d = ds[a] + ' ' + ed[b] 
    return d


n = int(input())

print(number_to_words_ru(n))