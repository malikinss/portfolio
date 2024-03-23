'''
TODO:   
        Implement the choose_plural() function, which takes two arguments in the following order:
            - amount — natural number, quantity
            - declensions — a tuple of three declension variants of a noun

        The function should return a string obtained by combining a suitable noun from the declensions tuple and the amount amount, in the following format:
            <quantity> <noun>

NOTE:   
        The tuple passed to the function is easy to make according to the mnemonic rule: one, two, five.
'''

def choose_plural(amount, declensions):
    nouns = {1:0, 2:1, 3:1, 4:1, 
             5:2, 6:2, 7:2, 8:2, 
             9:2, 0:2}
    
    last_digit = amount % 10
    last_two_digits = amount % 100

    if last_two_digits in range(11, 20):
        output_string = str(amount) + ' ' + declensions[2]
    else:        
        output_string = str(amount) + ' ' + declensions[nouns[last_digit]]
    
    return output_string

assert (choose_plural(21, ('пример', 'примера', 'примеров'))) == '21 пример'
assert choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')) == '92 гвоздя'
assert (choose_plural(8, ('яблоко', 'яблока', 'яблок'))) == '8 яблок'
assert (choose_plural(111223, ('копейка', 'копейки', 'копеек'))) == '111223 копейки'
assert (choose_plural(763434, ('рубль', 'рубля', 'рублей'))) == '763434 рубля'
assert (choose_plural(512312, ('цент', 'цента', 'центов'))) == '512312 центов'
assert (choose_plural(59, ('помидор', 'помидора', 'помидоров'))) == '59 помидоров'
assert (choose_plural(23424157, ('огурец', 'огурца', 'огурцов'))) == '23424157 огурцов'
assert (choose_plural(240, ('курица', 'курицы', 'куриц'))) == '240 куриц'
assert (choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов'))) == '49324 плюмбуса'
assert (choose_plural(505, ('утка', 'утки', 'уток'))) == '505 уток'
assert (choose_plural(666, ('шкаф', 'шкафа', 'шкафов'))) == '666 шкафов'
assert (choose_plural(11, ('стул', 'стула', 'стульев'))) == '11 стульев'
assert (choose_plural(3458438435812, ('доллар', 'доллара', 'долларов'))) == '3458438435812 долларов'
assert (choose_plural(2, ('пример', 'примера', 'примеров'))) == '2 примера'
assert (choose_plural(111, ('пример', 'примера', 'примеров'))) == '111 примеров'
assert (choose_plural(1223123111, ('пример', 'примера', 'примеров'))) == '1223123111 примеров'

