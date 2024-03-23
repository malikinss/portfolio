'''
TODO:   
        You have access to the list times_of_purchases, which contains the dates (datetime type) on which purchases were made in some online store.
        
        Complete the code below to display the text "Before Noon" if more purchases were made before noon, or the text "Afternoon" otherwise.

NOTE:   
        It is guaranteed that no purchase was made at exactly 12:00:00

        It is guaranteed that different numbers of purchases are made before noon and after noon.

'''
from datetime import datetime

def is_before_noon(datetime_obj):
    return datetime_obj.hour < 12

def is_after_noon(datetime_obj):
    return datetime_obj.hour >= 12

def print_purchase_activity(times_of_purchases):
    before_noon_purchases = list(filter(is_before_noon, times_of_purchases))
    after_noon_purchases = list(filter(is_after_noon, times_of_purchases))

    if len(before_noon_purchases) > len(after_noon_purchases):
        print('До полудня')
    else:
        print('После полудня')   

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26), 
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59), 
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53), 
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3), 
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5), 
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54), 
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45), 
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57), 
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42), 
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12), 
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27), 
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41), 
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44), 
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

print_purchase_activity(times_of_purchases)