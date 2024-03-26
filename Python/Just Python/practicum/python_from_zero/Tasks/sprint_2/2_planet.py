import math

class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.radius = radius
        
        self.surface_area = 4 * math.pi * pow(radius, 2)
        
        self.mean_temp_celcius = temp_celsius
        self.mean_temp_fahrenheit = temp_celsius * 9 / 5 + 32

    def show_info(self):
        print(f'Planet: {self.name} has surface area: {self.surface_area:.2f} square kilometers.')
        print(f'Average temperature on the surface: {self.mean_temp_fahrenheit:.2f} degrees by Fahrenheit\n')

jupiter = Planet('Jupiter', 69911, -108)
pluto = Planet('Pluto', 1187, -233.15)

jupiter.show_info()
pluto.show_info()