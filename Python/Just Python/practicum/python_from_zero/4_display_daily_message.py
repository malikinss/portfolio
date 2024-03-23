'''
TODO:
        It's time to teach the fitness tracker to display information messages and calculation results.

        The software module takes as input the number of steps, but subsequently the distance traveled by the user is described in kilometers.

        Teach the program to convert steps to kilometers.

        Display the values of the distance traveled and kilocalories expended, rounded to the nearest hundredth. Use f-strings in your solution.

        Depending on the distance traveled, the program should print “congratulations”:
            Today you walked <number_of_steps> steps.
            Distance traveled <distance_in_km> km.
            You burned <number_of_calories> kcal.
            <congratulations>
'''

def convert_steps_to_distance(steps):
    MEAN_STEP_LENGTH_M = 0.65
    TRANSFER_COEFF = 1000 

    result = steps * MEAN_STEP_LENGTH_M / TRANSFER_COEFF
    
    return result
    
def calculate_spent_calories(weight, height, dist, hours):
    mean_speed = dist / hours
    spent_minutes = hours * 60

    result = (0.035 * weight +(mean_speed ** 2 / height) * 0.029 * weight)
    result *= spent_minutes

    return result

def congrat_user(distance_km):
    GOAL_ACHIEVED = 6.9
    PRODUCTIVE_DAY = 3.9
    NEEDS_IMPROVEMENT = 2.0
    
    if GOAL_ACHIEVED <= distance_km:
        return 'Excellent result! The goal has been achieved.'
    elif PRODUCTIVE_DAY <= distance_km:
        return 'Not bad! The day was productive.'
    elif NEEDS_IMPROVEMENT <= distance_km:
        "Not enough, but we'll catch up tomorrow!"
    else:
        'Lying down is also useful. The main thing is participation, not victory!'

def display_daily_message(steps):
    weight = 75
    height = 175
    hours = 24

    distance = convert_steps_to_distance(steps)
    calories = calculate_spent_calories(weight, height, distance, hours)
    congratulation = congrat_user(distance)

    print(f"""Today you walked {steps} steps.
Distance traveled {distance:.2f} km.
You burned {calories:.2f} kcal.
{congratulation}""")

display_daily_message(18462)