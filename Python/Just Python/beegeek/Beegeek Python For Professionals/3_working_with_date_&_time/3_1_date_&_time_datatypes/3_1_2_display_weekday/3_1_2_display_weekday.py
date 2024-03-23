'''
TODO:   
        Hurricane Andrew, which struck Florida on August 24, 1992, was one of the costliest and deadliest hurricanes in U.S. history.

        Complete the code below to print the day of the week (starting at 0) on which Hurricane Andrew made landfall in the United States.    

'''
# import the date type from the datetime module
from datetime import date

# create an object corresponding to the date of the hurricane
hurricane_andrew = date(1992, 8, 24)

# display the day of the week
print(hurricane_andrew.weekday())