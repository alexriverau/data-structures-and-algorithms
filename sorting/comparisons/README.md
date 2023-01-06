# Code Challenge: Class 28

## Sorting: Comparisons

---

* Write comparator functions that sort domain objects.
  * **Input:** List of Movie objects, with the following properties:
    * title (string)
    * year (number)
    * list of genres (list of strings)
* Function one, sorts movies by most recent year first.
* Function two, sorts movies, alphabetical by title. (ignoring any leading “A”s, “An”s, or “The”s).
* Write tests for the comparator functions.
  * Tests will need to call the comparator functions directly, and make assertions about the response values given test inputs.

### Solution

* [code](movies.py)

### Tests

* [tests](test_movies.py)
