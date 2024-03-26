class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name} ({self.phone})')


# объявляем класс Friend, дочерний по отношению к классу User
class Friend(User):
    def show(self):
        print(f'Имя: {self.name} || Телефон: {self.phone}')


# создаём объекты User и Friend
father = User('Дюма-отец', '+33 3 23 96 23 30')
son = Friend('Дюма-сын', '+33 3 23 96 23 30') 

# вызываем метод show() класса User (родительского)
father.show()
# результат: 
# Дюма-отец (+33 3 23 96 23 30)

# вызываем метод show() класса Friend (дочернего)
son.show() 
# результат выглядит иначе, чем у объекта User: 
# Имя: Дюма-сын || Телефон: +33 3 23 96 23 30