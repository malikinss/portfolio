'''
TODO: 
        The online cinema sends Anton a list of films recommended for viewing.
        
        Help Anton choose highly rated films and add them to his favorites.

        If a recommended movie has a rating below 4.0, remove it from the recommended_movie dictionary.
        
        In this case, the program should display a message
            The movie "<film_name>" is not interesting: "<review_of_the_film>". 
            The film has been removed from recommendations.

        The program should add all films with a rating above 4.0 to the favorites_movie dictionary with favorite films and display a message
            The movie "<film_name>" has a good review: "<film_review>". The movie has been added to your favorites.

        Print the resulting collection of your favorite movies.
'''
def display_bad_movie_msg(movie, review):
    print(f'The movie "{movie}" is not interesting: "{review}". \nThe film has been removed from recommendations.\n')

def display_good_movie_msg(movie, review):
    print(f'The movie "{movie}" has a good review: "{review}". \nThe movie has been added to your favorites.\n')

def delete_records(given_dict, records_to_delete):
    for record in records_to_delete:
        if record in given_dict:
            del given_dict[record]
    
    return given_dict

def get_favorite_movies(movies):
    favorite_movies = {}
    bad_movies = []

    for movie, data in movies.items():
        cur_review = data['review']

        if data['rating'] < 4.0:
            display_bad_movie_msg(movie, cur_review)
            bad_movies.append(movie)
            continue
        
        display_good_movie_msg(movie, cur_review)
        favorite_movies[movie] = data

    movies = delete_records(movies, bad_movies)

    return favorite_movies


recommended_movies = {
    'Hancock': {'rating': 4.7, 'review': 'Cool'},
    'Matrix': {'rating': 4.7, 'review': 'Cool'},
    'Hackers':  {'rating': 4.5, 'review': 'Good'},
    'Tron':  {'rating': 3.8, 'review': 'Good'},
    'Cyber':  {'rating': 2.5, 'review': 'Bad'},
    'Fifth Wave':  {'rating': 4.1, 'review': 'Good'},
    'Avengers': {'rating': 4.8, 'review': 'Cool'},
    'Green Elephant':  {'rating': 2.0, 'review': 'Bad'}
}

print(get_favorite_movies(recommended_movies))


