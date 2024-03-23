'''
TODO:   
        From 1950 to 2017, Florida was hit by a total of 235 hurricanes.

        The florida_hurricane_dates variable stores a list of dates on which a hurricane occurred.

        The Atlantic hurricane season officially begins on June 1st.

        Complete the code below to print the number of hurricanes since 1950 that hit Florida before the official start of hurricane season.

NOTE:   
        Assume that the florida_hurricane_dates variable is declared and available to your program.
        
        Assume that the date type is already imported into the program. 

'''
# counter for the required number of hurricanes
early_hurricanes = 0

# cycle by dates on which there was a hurricane
for hurricane in florida_hurricane_dates:
    # if the month of the hurricane is less than June (ordinal number 6)
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)