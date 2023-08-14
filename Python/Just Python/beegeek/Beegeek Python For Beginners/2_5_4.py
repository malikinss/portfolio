""" 
Task: The Mad Titan Thanos has collected all 6 Infinity Stones 
and intends to wipe out half the population of the universe 
with a snap of his fingers. 
Moreover, if the population of the Universe is an odd number, 
then the titan will show mercy and round the number of survivors up. 
Help the Avengers count the number of survivors.
"""
population = int(input())
population = population*(-1)
survivors = population//2*(-1)
print(survivors)