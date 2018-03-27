budget.py
---------
You enter the movie number from https://www.themoviedb.org/. The program prints the movie's budget.

my_base.py
----------
The program creates a database of movies (my_base.json), that contains movies' details from https://www.themoviedb.org/. The number of movies in the database is 1000 by default, but you can change it.

my_base.json
------------
A database of movies, created by my_base.py. It contains movies' details from https://www.themoviedb.org/. The number of movies in the database is 1000. This database is required for original_title.py and recommendation_list.py.

original_title.py
-----------------
You enter the character sequence. The program prints original titles of movies from the database of movies (my_base.json), which contain this character sequence.

recommendation_list.py
----------------------
You enter the original title of any film from the database of movies (my_base.json). You answer two questions: "How many common keywords do you want? (at least)" and "Do you want movies with similar titles? Y/N". According to your answers, the program creates a recommendation list for you and prints the original titles of the movies it includes.
