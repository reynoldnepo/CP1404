"""
Replace the contents of this module docstring with your own details.
"""

import csv

movies_file = open('movies.csv')
movies = csv.reader(movies_file, delimiter=',')


#List each line in readMovie =['Count','Movie','year','watched')
#Add counter for sum_of_movies and determine if watched or not watched



def main():
    print("Movies To Watch 1.0 - by Reynold Nepomuceno")
    #print("{} movies loaded".format(sum_of_movies))#sum(1 for line in readMovie)
    menu = """    L - List movies
    A - Add a new movie
    W - Watch a Movie
    Q - Quit"""
    print(menu)

    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            list_movie()
        elif choice == "A":
            print('add_Qmovie()')
        elif choice == "W":
            print('movie_counter()')
        else:
            print("Invalid option, please choose again.")
        print(menu)
        choice = input(">>>".upper())
    print("Enjoy your movie!")
    movies_file.close()


def list_movie():
    total_movies = 0
    total_watched = 0
    for row in movies:
        total_movies += 1
        if row[3] == 'y':
            total_watched += 1
            watched = " "
        elif row[3] == 'n':
            watched = "*"
        print("{:}. {} {:<40} - {:>4} ({})".format(total_movies, watched, row[0], row[1], row[2]))
    print("{} movies watched,{} movies still to watch".format(total_watched,total_movies-total_watched))


def add_movie():
    movie_title = input("Title of Movie:")
    movie_year = input("Year of Movie:")
    movie_genre = input ("Genre of Movie:")

    movies_file.write("{},{},{},n".format(movie_title,movie_year,movie_genre))
    #if __name__ == '__main__'

#main()
#add_movie()
list_movie()