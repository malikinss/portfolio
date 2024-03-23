'''
TODO:
        Calorie counting is a standard feature of fitness trackers, and Unicorn's runaway tracker is no exception.
        Flow can be calculated using different algorithms, and Unicorn took the formula derived by scientists at Southern Methodist University in Dallas.
        
        The formula says: 
            kilocalorie consumption per minute of movement is equal to the sum
                0.035 user weight
                and the product of two values:
                    the square of the speed in km/h divided by the user’s height;
                    0.029 user weight.
        
        Write a formula that calculates the kilocalorie consumption in two hours: the source data is in the code.
'''

def calories_per_minute(weight, height, dist, hours):
    speed = dist / hours
    result = (speed ** 2) / height
    result *= (0.029 * weight)
    result += (0.035 * weight)
    return result

weight = 75
height = 181

dist = 15.2
hours = 2.15
minutes = hours * 60

speed = (dist / hours)

spent_calories = calories_per_minute(weight, height, dist, hours) * minutes
print(spent_calories)
