'''
TODO:
        The recommended_movies variable stores a list of recommended movies, and hackers_movies stores a list of “Top 12 movies about coders and hackers.”
        
        Display in the terminal only those recommended films that are in the top list. For each movie, the line must be printed. 
        
        We recommend that programmers watch the movie "<movie_name>"
'''
def display_only_hacker_movies(recommended_movies):
    hackers_movies = ['The Tron', 'the Millitary Games', 'Sneakers', 'Jonny Mnemonic', 'The Hackers', 'Nirvana', '23', 'Enemy of the State', 'Who Am I', 'Takedown', 'Web', 'Swordfish']

    recommended_hacker_movies = []

    for cur_movie in recommended_movies:
        if cur_movie in hackers_movies:
            recommended_hacker_movies.append(cur_movie)

    for cur_movie in recommended_hacker_movies:
        print(f' We recommend that programmers watch the movie {cur_movie}')

recommended_movies = ['Hatiko', 'Knocking on the Heaven Doors', '23', 'The Hackers', 'The Tron', '1408']

display_only_hacker_movies(recommended_movies)