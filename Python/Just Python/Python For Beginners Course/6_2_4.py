""" 
Task: The names of three cities are given. Write a program that determines the shortest and longest city names.
"""
city_1, city_2, city_3 = input(), input(), input()

shortest_cityname = min(city_1, city_2, city_3, key=len)
longest_cityname = max(city_1, city_2, city_3, key=len)

print(shortest_cityname)
print(longest_cityname)