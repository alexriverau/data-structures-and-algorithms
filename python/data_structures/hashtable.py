class Hashtable:
    """
    Create the following methods:
    set()
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
    get()
        Arguments: key
        Returns: Value associated with that key in the table
    has()
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
    keys()
        Returns: Collection of keys
    hash()
        Arguments: key
        Returns: Index in the collection for that key
    """

    def __init__(self, size=1024):
        self.size = size
        self.bucket = size * [None]

    def set(self, key, value):

        index = self.hash(key)

        # if there is no key at that bucket's index set key/value pair in the table
        if self.bucket[index] is None:
            self.bucket[index] = (key, value)

        # if there is a key at that bucket's index overwrite with new key/value pair in the table
        elif self.bucket[index] is not None:
            self.bucket[index] = (key, value)

    # returns value associated with that key in the table
    def get(self, key):

        index = self.hash(key)

        if self.bucket[index] is None:
            return None
        elif self.bucket[index] is not None:
            return self.bucket[index][1]

    # returns a boolean indicating if the key exists in the table already
    def has(self, key):
        index = self.hash(key)

        if self.bucket[index] is None:
            return False
        else:
            if self.bucket[index] is not None:
                return True

    # returns a list of keys
    def keys(self):

        keys_list = []
        for key in self.size:
            keys_list.append(key)
        return keys_list

    # hashes the key and returns its index in the collection
    def hash(self, key):

        sum_hash = 0
        for char in key:
            sum_hash += ord(char)  # ord() method returns ascii/unicode value

        primed = sum_hash * 599  # multiplies by a prime number
        index = primed % self.size
        return index


