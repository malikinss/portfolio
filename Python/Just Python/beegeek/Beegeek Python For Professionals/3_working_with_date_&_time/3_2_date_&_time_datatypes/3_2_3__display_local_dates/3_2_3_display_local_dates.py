'''
TODO:   
        The variable florida_hurricane_dates stores a list of dates (type date) on which a hurricane occurred in Florida from 1950 to 2017.

        Complete the code below to print the earliest date in the florida_hurricane_dates list in three different formats:
            in ISO standard (YYYY-MM-DD)
            in a typical Russian style (DD.MM.YYYY)
            in typical American style (MM/DD/YYYY)

NOTE: 
        Assume that the florida_hurricane_dates variable is declared and available to your program.

        Assume that the date type is already imported into the program.
'''
# assign the earliest date of the hurricane to the first_date variable
first_date = min(florida_hurricane_dates)

# convert the date to ISO and RU format
iso = 'Date of first hurricane in ISO format: ' + first_date.isoformat()
ru = 'Date of the first hurricane in RU format: ' + first_date.strftime('%d.%m.%Y')
us = 'Date of the first hurricane in US format: ' + first_date.strftime('%m/%d/%Y')

print(iso)
print(ru)
print(us)
