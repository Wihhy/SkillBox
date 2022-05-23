print('Введите общее количество фильмов:')
movies_amount = (int(input()))
for i in range(movies_amount):
    movies = set(range(1, movies_amount + 1))
    movies_list = set(movies)
print('Введите номера фильмов которые у вас уже есть:')
available_movies = input()
available_movies = set(available_movies)
for item in available_movies:
    if item in movies_list:
        movies_list.remove(item)

