class Contact:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday

    def show_contact(self):
        print(f'{self.name}',
              f'address: {self.address}',
              f'phone: {self.phone}',
              f'birtday: {self.birthday}', sep='\n')  

    def __str__(self) -> str:
        return f'Contact: {self.name}'



lev = Contact(name='Lev Tolstoy',
              phone='+7 (123) 456-78-90',
              address='Clear Field',
              birthday='9.09.1828')

mike = Contact(name='Michael Bulgakov',
              phone='2-03-27',
              address='Russia, Moscow, Bolshaya Pirogovskaya, 35b, ap.6',
              birthday='15.05.1891')

vlad = Contact(name='Vladimir Mayakoskiy',
              phone='73-88',
              address='Russia, Moscow, Lubyanskiy Proezd, 3, ap.12',
              birthday='19.07.1893')

print(lev)
print(mike)
print(vlad)

mike.address = 'Russia, Moscow, Nashokiski Street, bld. 3, apt. 44'
mike.phone = 'K-058-67'

vlad.address = 'Russia, Moscow, Hendricks Way, bld. 15, apt. 5'
vlad.phone = '2-35-71'

print(mike)
print(vlad)

vlad.show_contact()