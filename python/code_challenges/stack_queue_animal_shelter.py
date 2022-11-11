from data_structures.queue import Queue


class AnimalShelter:

    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, animal):

        if animal.kind == 'dog':
            self.dog.enqueue(animal)
        elif animal.kind == 'cat':
            self.cat.enqueue(animal)
        else:
            return None

    def dequeue(self, pref):

        if pref == 'dog':
            return self.dog.dequeue()
        elif pref == 'cat':
            return self.cat.dequeue()
        else:
            return None


class Dog:

    def __init__(self):
        self.kind = 'dog'


class Cat:

    def __init__(self):
        self.kind = 'cat'
