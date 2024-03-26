class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show(self):
        print(f'{self.name} носит одежду размера {self.size}.')


class Parrot(Bird):
    def __init__(self, name, size, sound):
        super().__init__(name, size)
        self.sound = sound

    def show(self):
        print(f'{self.name} носит одежду размера {self.size} и {self.sound}.')


class Predator(Bird):
    def __init__(self, name, size, claws_size):
        super().__init__(name, size)
        self.claws_size = claws_size

    def show(self):
        print(f'{self.name} носит одежду размера {self.size} и '
              f'когти размера {self.claws_size}.')


class Egg(Predator):
    def show(self):
        print(f'Из яйца вылупится птичка {self.name} размера {self.size} с '
              f'когтями размера {self.claws_size}.') 