'''
TODO:   
        Write a program that will read three numbers and display them in a specific format. 
        
        The first number is an integer, the second is a floating point number, the third is a non-negative integer. 
        
        Using the examples, you need to determine the required data format.

INPUT:
        Numbers

OUTPUT:
        Numbers in the required data format 
'''

def get_binary_formatted_string(number):
    number_binary = f"{number:016b}"
    number_binary_formatted = '_'.join(number_binary[i:i+4] for i in range(0, len(number_binary), 4))

    return number_binary_formatted

def get_float_formatted_string(float_number):
    return "{:10.2f}".format(float_number).replace(" ", "#")

def get_integer_formatted_string(integer_number):
    return "{:+010d}".format(integer_number)

integer_number = int(input(""))
float_number = float(input(""))
non_negative_integer = int(input(""))

print(get_integer_formatted_string(integer_number))
print(get_float_formatted_string(float_number))
print(get_binary_formatted_string(non_negative_integer))