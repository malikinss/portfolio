'''
TODO:   
        Write a program that will read sequences of measurements. 
        
        In each sequence you need to select the maximum value, and ultimately display a list of these maximum values, sorted in descending order, separated by the “;” symbol. 
        
        The input data in the first line will contain a positive integer number - how many records need to be processed, and there may be more records themselves than this number, this must be taken into account. 
        
        Values within one record are separated by a space, the minimum number of values in a record is 1. 
        
        Records are separated by a line break.
'''
max_values  = []

for _ in range(int(input())):
    given_sequence = list(map(int, input().split()))
    max_values.append(max(given_sequence))

max_values.sort(reverse=True)

print(";".join(map(str, max_values)))