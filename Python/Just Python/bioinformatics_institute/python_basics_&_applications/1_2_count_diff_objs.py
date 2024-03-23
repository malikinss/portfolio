'''
TODO:
        Implement a program that will calculate the number of distinct objects in a list.
        
        Two objects a and b are considered different if a is b is False.

        Your program has access to a variable called objects, which refers to a list of up to 100 objects. 
        
        Print the number of different objects in this list.
'''

def count_diff_objs(objects):
    diff_objects = []
    
    for obj in objects:
        if obj not in diff_objects:
            diff_objects.append(obj)
    
    return len(diff_objects)

def count_diff_objs2(objects):
    unique_objects = set()
    
    for obj in objects:
        unique_objects.add(obj)
    
    return len(unique_objects)