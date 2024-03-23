'''
TODO:   
        There are systems of likes in various social networks, which, depending on the number of people who rated the post, show relevant information.

        Implement the likes() function, which takes a single argument:
            names — list of names

        The function should return a string according to the examples below, the content of which depends on the number of names in the names list.

NOTE:   
        The names in the string generated and returned by the function must be in their original order.

        Note that if there are more than three names in the list passed to the function, then only the first two of them are explicitly specified.
'''

def print_case_1(names):
    return (f'{names[0]} оценил(а) данную запись')

def print_case_2(names):
    return (f'{names[0]} и {names[1]} оценили данную запись')

def print_case_3(names):
    return (f'{names[0]}, {names[1]} и {names[2]} оценили данную запись')

def print_case_4(names, number_of_likes):
    remaining_quantity = number_of_likes - 2
    return (f'{names[0]}, {names[1]} и {remaining_quantity} других оценили данную запись')


def likes(names):
    output_string = ''
    number_of_likes = len(names)
    cases_of_message = {0: 'Никто не оценил данную запись',
                        1: print_case_1,
                        2: print_case_2,
                        3: print_case_3,
                        4: print_case_4}
    
    if 0 == number_of_likes:
        output_string = cases_of_message[number_of_likes]
    elif 4 > number_of_likes:
        output_string = cases_of_message[number_of_likes](names)    
    elif 4 <= number_of_likes:
        output_string = cases_of_message[4](names, number_of_likes)

    return output_string