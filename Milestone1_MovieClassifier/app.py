"""
enter 'a' to add a movie
enter 'l' to see your movies
enter 'f' to find your movies
enter 'q' to quit

Tasks:
(x) show main interface
(x) allow users to add movies
() where do we store movies?
(x) what is the format of a movie?
(x) show all movies
() find a movie
(x) stop running the program
"""

movies = []

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find your movies, or 'q' to quit \n")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input.lower() == 'l':
            show_movie_list(movies)
        elif user_input.lower() == 'f':
            find_movies()
        elif user_input.lower() == 'q':
            print('Stopping program...')
        else:
            print('invalid comment, please enter a, l, f or q')
        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find your movies, or 'q' to quit \n")

    
def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the movie director: ')
    year = int(input('Enter the movie release year: '))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })

def show_movie_list(movies_list):
    for movie in movies:
        show_movie_details(movie)
    
def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")

def find_movies():
    find_by = input ("What property of the movie are you looking for? 'm' for movie, 'd' for director or 'y' for year")
    looking_for = input ("What are you searching for?")
    
    found_movies = find_by_attribute(looking_for, lambda x: x[find_by])
    show_movie_list(found_movies)

def find_by_attribute(expected, finder):
    found = []
    for i in movies:
        if finder[i] == expected:
            found.append(i)

    return found

menu()
print(add_movie)