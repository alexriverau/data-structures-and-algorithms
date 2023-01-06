import pytest
from movies import sort_movies_by_year, sort_movies_by_title, movies


def test_sort_movies_by_year():
    actual = sort_movies_by_year(movies)
    expected1 = ["The Intouchables", "Valkyrie", "Ratatouille", "Stardust", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
    assert actual == expected1


def test_sort_movies_by_title():
    actual = sort_movies_by_title(movies)
    expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank  edemption", "Stardust", "Valkyrie"]
    assert actual == expected2
