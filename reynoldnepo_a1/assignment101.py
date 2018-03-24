"""
Replace the contents of this module docstring with your own details.
"""

import csv

input_movies = open('movies.csv',"r")
movie_reader = csv.reader(input_movies, delimiter=',')
output_movies = open('movies2.csv',"w")
movie_writer = csv.writer(output_movies,delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
#movies_writelist = csv.writer(movies_file, delimiter=',')

#print(movies_readlist[-1])
#List each line in readMovie =['Count','Movie','year','watched')
#Add counter for sum_of_movies and determine if watched or not watched

movies = []
total_movies = 0

def main():
    create_movies()

    print("Movies To Watch 1.0 - by Reynold Nepomuceno")
    print("{} movies loaded".format(sum_of_movies))
    menu = """\n L - List movies\n A - Add a new movie\n W - Watch a Movie\n Q - Quit"""
    print(menu)
    choice = input(">>>").upper()

    while choice != "Q":
        if choice == "L":
            list_movie()
        elif choice == "A":
            add_movie()
        elif choice == "W":
            print('movie_counter()')
        else:
            print("Invalid option, please choose again.")
        print(menu)
        choice = input(">>>".upper())
    print("Enjoy your movie!")

    input_movies.close()
    output_movies.close()

def create_movies():
    for row in movie_reader:
        total_movies += 1
        movies.append(row)

def list_movie():
    total_watched = 0
    for row in movies:
        if row[3] == 'y':
            total_watched += 1
            watched = " "
        elif row[3] == 'n':
            watched = "*"
        print("{:}. {} {:<40} - {:>4} ({})".format(total_movies, watched, row[0], row[1], row[2]))
    print("{} movies watched,{} movies still to watch".format(total_watched,total_movies-total_watched))
    print(movies)


def add_movie():
    movie_title = input("Title of Movie:")
    movie_year = input("Year of Movie:")
    movie_genre = input("Genre of Movie:")
    movie_watched = input("Have you watched this Movie? y or n")
    new_movie = [movie_title, movie_year, movie_genre, movie_watched]

    movies.append(new_movie)
    print(movies)
    for item in movies:
        movie_writer.writerow([item[0],item[1],item[2],item[3]])

#if __name__ == '__main__'


main()
#add_movie()
#list_movie()

