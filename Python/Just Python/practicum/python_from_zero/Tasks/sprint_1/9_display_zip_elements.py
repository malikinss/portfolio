'''
TODO: 
        Objects of type zip are iterable. 
        Loop through the elements of the movies_info object and print them.
'''

movie_ratings= [4.7, 5.0, 4.3, 4.0]
movies = ['Matrix', 'Hackers', 'Tron', 'Cyber']

movies_info = zip(movies, movie_ratings)

for element in movies_info:
    print(element)
