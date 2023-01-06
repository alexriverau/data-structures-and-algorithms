movies = [
  {
    "title": "Beetlejuice",
    "year": 1988,
    "genres": ["Comedy", "Fantasy"],
  },
  {
    "title": "The Cotton Club",
    "year": 1984,
    "genres": ["Crime", "Drama", "Music"],
  },
  {
    "title": "The Shawshank Redemption",
    "year": 1994,
    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Crocodile Dundee",
    "year": 1986,
    "genres": ["Adventure", "Comedy"],
  },
  {
    "title": "Valkyrie",
    "year": 2008,
    "genres": ["Drama", "History", "Thriller"],
  },
  {
    "title": "Ratatouille",
    "year": 2007,
    "genres": ["Animation", "Comedy", "Family"],
  },
  {
    "title": "City of God",
    "year": 2002,
    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Memento",
    "year": 2000,
    "genres": ["Mystery", "Thriller"],
  },
  {
    "title": "The Intouchables",
    "year": 2011,
    "genres": ["Biography", "Comedy", "Drama"],
  },
  {
    "title": "Stardust",
    "year": 2007,
    "genres": ["Adventure", "Family", "Fantasy"],
  },
]


# implementing merge sort to sort movies by year
def merge_sort_year(lst_movies):
    n = len(lst_movies)

    if n > 1:
        mid = n // 2
        left = lst_movies[:mid]
        right = lst_movies[mid:]

        merge_sort_year(left)
        merge_sort_year(right)
        merge_year(left, right, lst_movies)

    return lst_movies


def merge_year(left, right, lst_movies):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i]['year'] < right[j]['year']:
            lst_movies[k] = right[j]
            j = j + 1
        else:
            lst_movies[k] = left[i]
            i = i + 1

        k = k + 1

    if i == len(left):
        for idx in range(j, len(right)):
            lst_movies[k] = right[idx]
            k = k + 1

    else:
        for idx in range(i, len(left)):
            lst_movies[k] = left[idx]
            k = k + 1


# function that returns a list of movies sorted by year
def sort_movies_by_year(lst_movies):
    movies_by_year = []
    for movie in merge_sort_year(lst_movies):
        movies_by_year.append(movie['title'])
    return movies_by_year


# implementing merge sort to sort movies by title
def merge_sort_title(lst_movies):
    n = len(lst_movies)

    if n > 1:
        mid = n // 2
        left = lst_movies[:mid]
        right = lst_movies[mid:]

        merge_sort_title(left)
        merge_sort_title(right)
        merge_title(left, right, lst_movies)

    return lst_movies


def merge_title(left, right, lst_movies):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i]['title'] < right[j]['title']:
            lst_movies[k] = right[j]
            j = j + 1
        else:
            lst_movies[k] = left[i]
            i = i + 1

        k = k + 1

    if i == len(left):
        for idx in range(j, len(right)):
            lst_movies[k] = right[idx]
            k = k + 1

    else:
        for idx in range(i, len(left)):
            lst_movies[k] = left[idx]
            k = k + 1


# function that returns a list of movies sorted by title
def sort_movies_by_title(lst_movies):
    movie_titles = []
    for movie in merge_sort_title(lst_movies):
        movie_titles.append(movie['title'])
    return movie_titles
