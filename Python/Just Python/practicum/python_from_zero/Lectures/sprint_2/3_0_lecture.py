 # Создана переменная, ей присвоено значение типа string
var = "string here"

# Переменной присваивается новое значение, и вот уже тип данных — integer
var = 1234


def we_crash_all(name):
    return 'Привет, ' + name + ', мы всё сломали!'


print(we_crash_all('Наташа'))


print(we_crash_all(True))
# >>> TypeError: can only concatenate str (not "bool") to str

class WeirdObject:
    def work(self):
        print('Работает')


def dependency_func(obj):
    obj.work()


dependency_func(WeirdObject())
>>> Работает

dependency_func(11) # AttributeError: 'int' object has no attribute 'work'


# Без аннотации: объявили переменную, 
# а Python сам догадался, какой в ней тип данных
birth_year = 1971

# С аннотацией: объявили переменную и указали, 
# что это переменная - только для целых чисел
birth_year: int = 1971 


# Переменная var_for_bool аннотирована как булева, но в неё передана строка
var_for_bool: bool = 'Чистая правда, клянусь'

# Python не обратит внимания на это несоответствие 
# и продолжит выполнять код, как ни в чём не бывало.


# Аннотация переменной name: "это строка"
name: str = 'Наташа'

# Аннотация переменной var_for_bool: "это булева переменная"
var_for_bool: bool = True

# Можно напечатать аннотации переменных из глобальной области видимости
print(__annotations__)
# >>> {'name': <class 'str'>, 'var_for_bool': <class 'bool'>} 


# <имя переменной>: <принимаемый тип> = <значение>

var_integer: int = 10  # Только целочисленные значения
var_float: float = 10.0  # Числа с плавающей точкой (включая целые, можно передать 10)
var_flag: bool = True  # Логический тип
var_string: str = 'Йя строка'  # Строки
 

# Вариант 1
# <имя переменной>: <принимаемый тип>
# <имя переменной> = <значение>
# Вариант 2: тип данных указывается после символа # 
#<имя переменной> = <значение>  # type: <принимаемый тип>

# На примере birth_year типа int со значением 1971 синтаксис будет выглядить так:
# Вариант 1 
birth_year: int 
birth_year = 1971

# Вариант 2 (устаревший, использовался до python 3.5)
birth_year = 1971  # type: int 


#def <имя функции>(<аргумент>: <тип>) -> <возвращаемый тип>:

def is_rhomb(a_size: float, b_size: float) -> bool:
    """Проверяет, является ли параллелограмм ромбом."""
    # Вернёт True или False в зависимости от истинности выражения
    return a_size == b_size  
 

# Функция print_hi() ожидает строковый аргумент, 
# значение этого аргумента по умолчанию - 'stranger'.
# Функция ничего не возвращает, и для неё тип возвращаемых данных - None
def print_hi(name: str = 'stranger') -> None:
    print('Hi,' + name + '!')

# Можно напечатать типы данных функций
print(is_rhomb.__annotations__)
#>>> {'a_size': <class 'float'>, 'b_size': <class 'float'>, 'return': <class 'bool'>}

print(print_hi.__annotations__)
#>>> {'name': <class 'str'>, 'return': <class 'None'>} 

# class <имя класса>:
#     <имя переменной>: <принимаемый тип>
#     def __init__(self, <имя переменной>: <принимаемый тип>) -> None:
#         self.<имя переменной> = <имя переменной>

# В классе Hello инциализирована строчная переменная x
# со значением по умолчанию 'привет'.
# self в классах никогда не аннотируется.
# __init__ ничего не возвращает.
class Hello:
    x: str # Если здесь не указывать тип переменной,
           # аннотация для x не отобразится в словаре __annotations__,
           # однако анализатор возьмёт аннотацию из __init__ и корректно отработает

    def __init__(self, x: str = 'Привет') -> None:
        self.x = x

# Вывод на экран словаря __annotations__ из области видимости класса Hello
print(Hello.__annotations__)
>>> {'x': <class 'str'>} 