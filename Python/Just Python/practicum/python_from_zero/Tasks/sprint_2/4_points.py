from math import radians, sin, cos, acos
'''
TODO: 
        Create a "Point" class that has the properties "latitude" and "longitude".
            Implement the “distance” method inside it, which will calculate the distance from the current point to the specified one.

        Create a "City" class that will be a child of the "Point" class.
            Add new properties "name" and "population" to it.
            Implement a show() method in it, which will provide information about the instance.

        Create a "Mountain" class that will be a child of the "Point" class.
            Add new properties "name" and "height" to it.
            Implement a show() method in it, which will provide information about the instance.

        Create an instance of the "city" class for any city you know.
        Create an instance of the "mountain" class for any mountain you know.
        Calculate and display the distance between these two instances.
'''
class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    def distance(self, other):
        latitude_sins_product = sin(self.latitude) * sin(other.latitude)
        latitude_coss_product = cos(self.latitude) * cos(other.latitude)
        longitude_diff = self.longitude - other.longitude

        cos_d = latitude_sins_product  + latitude_coss_product * cos(longitude_diff)

        return 6371 * acos(cos_d)

class City(Point):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population
    
    def show(self):
        print(f'City: {self.name}, has population: {self.population} people.')

class Mountain(Point):
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height

    def show(self):
        print(f'Mount: {self.name}, has height: {self.height} meters.')

moscow = City(55.75, 37.61, 'Moscow', 13_154_708)
moscow.show()

everest = Mountain(27.59, 86.55,'Everest', 8848)
everest.show()

print(f'The Distance between Mount Everest and Moscow is {everest.distance(moscow):.2f} kilometers')