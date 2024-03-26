'''
TODO: 
        Create a class 'User' that will have the properties: name, phone. 
        
        Add a show() method to this class that will display information about the instance.

        Create a class 'Friend' that will be a child class of the parent class 'User'. 
        
        For the 'Friend' class, override the show() method so that it displays information about the instance in a different way.

        Create an instance of each of the classes. 
        
        Display information about instances to the terminal using the show() method. 
        
        Compare the results.
'''
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name} ({self.phone})')

class Friend(User):
    def show(self):
        print(f'name: {self.name} || Phone: {self.phone}')

user = User('Sam Malikin', '+9720585566532')
friend = Friend('Vladimir Rogalev', '+79219618213')

user.show()
friend.show()