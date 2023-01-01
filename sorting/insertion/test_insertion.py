import pytest
from insertion import insertion_sort


# @pytest.mark.skip('TODO')
def test_insertion_sort():
    actual = insertion_sort([8, 4, 23, 42, 16, 15])
    assert actual == [4, 8, 15, 16, 23, 42]


# @pytest.mark.skip('TODO')
def test_reverse_sorted():
    actual = insertion_sort([20, 18, 12, 8, 5, -2])
    assert actual == [-2, 5, 8, 12, 18, 20]


# @pytest.mark.skip('TODO')
def test_few_uniques():
    actual = insertion_sort([5, 12, 7, 5, 5, 7])
    assert actual == [5, 5, 5, 7, 7, 12]


# @pytest.mark.skip('TODO')
def test_nearly_sorted():
    actual = insertion_sort([2, 3, 5, 7, 13, 11])
    assert actual == [2, 3, 5, 7, 11, 13]


# @pytest.mark.skip('TODO')
def test_empty_list():
    actual = insertion_sort([])
    assert actual == []


# @pytest.mark.skip('TODO')
def test_single_element():
    actual = insertion_sort([1])
    assert actual == [1]
