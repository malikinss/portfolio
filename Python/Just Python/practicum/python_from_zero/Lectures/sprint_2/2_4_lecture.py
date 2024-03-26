class Bird:
    def __init__(self, name, size):
        # Это конструктор, он вызывается при создании объекта
        self.name = name
        self.size = size

    def show(self):
        # Вызывается для вывода на экран всех свойств объекта
        print(f'{self.name} носит одежду размера {self.size}.')


class Parrot(Bird):
    def __init__(self, name, size, sound):
        super().__init__(name, size)
        self.sound = sound

    def show(self):
        # Вызывается для вывода на экран всех свойств объекта
        print(f'{self.name} носит одежду размера {self.size} и {self.sound}.')


# Создание объектов
sparrow = Bird('Воробей', 'S')
ara = Parrot('Попугай ара', 'XL', 'разговаривает')
nymphicus = Parrot('Попугай Корелла', 'S', 'щебечет')

# Теперь можно воспользоваться его внешним интерфейсом: методом show()
sparrow.show()
ara.show()
nymphicus.show()

# Результат:
# Воробей носит одежду размера S.
# Попугай ара носит одежду размера XL и разговаривает.
# Попугай Корелла носит одежду размера S и щебечет. 