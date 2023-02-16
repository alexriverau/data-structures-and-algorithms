from data_structures.linked_list import LinkedList, Node


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "None"


# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> None"


# @pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> None"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> None"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


# @pytest.mark.skip("TODO")
def test_reverse():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    linked_list.reverse()

    assert linked_list.head.value == 3
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 1

    linked_list.reverse()

    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3


# @pytest.mark.skip("TODO")
def test_ll_add_one():
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    linked_list.ll_add_one()

    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 4

    linked_list = LinkedList()
    linked_list.add(4)
    linked_list.add(9)
    linked_list.add(9)

    linked_list.ll_add_one()

    assert linked_list.head.value == 5
    assert linked_list.head.next.value == 0
    assert linked_list.head.next.next.value == 0

    linked_list = LinkedList()
    linked_list.add(9)
    linked_list.add(9)
    linked_list.add(9)

    linked_list.ll_add_one()

    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 0
    assert linked_list.head.next.next.value == 0
    assert linked_list.head.next.next.next.value == 0
