'''
TODO:   
        At the BEEGEEK online school, employees are provided with a corporate email, which is formed as follows:
            <first name-last name>@beegeek.bzz
        
        For example,
            timyr-guev@beegeek.bzz

        With this approach, there is a problem of namesakes.
        To solve this problem, it was decided to assign a number to the right.
        Then:
            The first Timur Guev receives the mailbox timyr-guev@beegeek.bzz (no number)
            second — timyr-guev1@beegeek.bzz
            the third - timyr-guev2@beegeek.bzz, and so on.

        You are given a list of already occupied boxes in the order in which they are issued and the first and last names of new employees in a pre-prepared form (in Latin letters with a symbol between them).
        Write a program that distributes corporate boxes to new school employees.

NOTE:   
        The input to the program in the first line is a non-negative integer n - the number of issued boxes.

        The next n lines list the boxes themselves in order of issue, one per line.

        The next line contains a non-negative integer m — the number of new employees to whom corporate boxes need to be distributed.

        Each of the next m lines represents the employee's first and last name in ready-to-use format.
'''

def get_list_from_input_strings(strings_quantity):
    input_list = []
    
    for _ in range(strings_quantity):
        row = input()
        input_list.append(row)

    return input_list

def get_new_email_box(username, suffix):
    return username + suffix + '@beegeek.bzz'

def create_possible_suffixes_pool(size):
    return [i for i in range(1, size)]

def get_new_suffix(occupied_suffixes):
    new_suffix = ''

    if new_suffix in occupied_suffixes:
        possible_suffixes = create_possible_suffixes_pool(20)
        
        for suffix in occupied_suffixes:
            if suffix != new_suffix:
                possible_suffixes.remove(int(suffix))

        new_suffix = str(min(possible_suffixes))        

    return new_suffix


def get_occupied_suffixes(name, occupied_boxes):
    suffixes = []

    for email in occupied_boxes:
        if name in email:
            at_index = email.find('@')
            suffix = email[len(name):at_index]
            suffixes.append(suffix)

    return suffixes 

def get_namesakes_boxes(name, occupied_boxes):
    return [email for email in occupied_boxes if name in email]

def create_new_emailboxes(usernames, occupied_boxes):
    new_emailboxes = []

    for name in usernames:
        namesakes_boxes = get_namesakes_boxes(name, occupied_boxes)
        occupied_suffixes = get_occupied_suffixes(name, namesakes_boxes)
        new_suffix = get_new_suffix(occupied_suffixes)
        newuser_email = get_new_email_box(name, new_suffix)

        occupied_boxes.append(newuser_email)
        new_emailboxes.append(newuser_email)

    return new_emailboxes

def assign_corporate_emailboxes():
    occupied_boxes  = get_list_from_input_strings(int(input()))
    new_workers = get_list_from_input_strings(int(input()))
    new_email_boxes = create_new_emailboxes(new_workers, occupied_boxes)
    
    return new_email_boxes
    
print(*assign_corporate_emailboxes(), sep='\n')