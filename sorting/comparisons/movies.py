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


def sort_movies_by_year(lst_movies):

    for i in range(len(lst_movies)):

        for j in range(i + 1, len(lst_movies)):
            if lst_movies[i].year < lst_movies[j].year:
                lst_movies[i], lst_movies[j] = lst_movies[j], lst_movies[i]

    return lst_movies


def sort_movies_by_title(lst_movies):

    def get_title(movie):
        title = movie.title
        if title.startswith(('A ', 'An ', 'The ')):
            title = title[title.index(' ') + 1:]
        return title

    for i in range(len(lst_movies)):

        for j in range(i + 1, len(lst_movies)):
            if get_title(lst_movies[i]) > get_title(lst_movies[j]):
                lst_movies[i], lst_movies[j] = lst_movies[j], lst_movies[i]

    return lst_movies
