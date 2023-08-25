'''
TODO: Write a print_fio(name, surname, patronymic) function that takes three parameters:

-- name - the name of the person;
-- surname - the surname of the person;
-- patronymic - patronymic of a person;

and then prints out the name of the person.

NOTE: Provide for the fact that all three letters in the full name must be uppercase.
'''


def print_fio(name, surname, patronymic):
    print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())


name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)