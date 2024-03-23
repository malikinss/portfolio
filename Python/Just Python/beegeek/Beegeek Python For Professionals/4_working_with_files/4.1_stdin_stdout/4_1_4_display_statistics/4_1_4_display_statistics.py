'''
TODO:   
        A list of numbers is given, each of which is the height of another student at the BEEGEEK online school. 
        
        Write a program that determines the height of the shortest and tallest students and the average height of all students.

        The program receives an arbitrary number of lines as input; each line contains a natural number - the height of the next student of the BEEGEEK online school.

        The program should determine the height of the shortest and tallest students, as well as the average height among all students.

        The results obtained should be output in the following format:
            Height of the shortest student: <height of the shortest student>
            Height of the tallest student: <height of the tallest student>
            Average height: <average height among all students>

NOTE:   
        If nothing is supplied to the program as input, then it should output the text 'no students'


'''
import sys

def read_student_heights():
    heights = [line.strip() for line in sys.stdin.readlines()]
    return list(map(int, heights)) 

def calculate_average(list_of_nums):
    return sum(list_of_nums)/len(list_of_nums)

def display_statistics():
    heights = read_student_heights()

    if heights:
        print('Height of the shortest student:', min(heights))
        print('Height of the tallest student:', max(heights))
        print('Average height:', calculate_average(heights))
    else:
        print('no students')    

display_statistics()
