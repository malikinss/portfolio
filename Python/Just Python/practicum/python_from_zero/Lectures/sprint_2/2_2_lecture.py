class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name} ({self.phone})')


# наследуем класс Friend от User
class Friend(User):
    # Пишем конструктор класса-наследника,
    # чтобы он принимал все нужные параметры
    def __init__(self, name, phone, address):
        # наследуем функциональность конструктора из класса-родителя
        super().__init__(name, phone)
        # добавляем новую функциональность: свойство address
        self.address = address

    # полностью переопределяем родительский метод show()
    def show(self):
        print(f'Имя: {self.name} || '
              f'Телефон: {self.phone} || '
              f'Адрес: {self.address}')