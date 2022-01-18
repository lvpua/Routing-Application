# Class that will create a hash table from a packaged csv file import.
# Referenced from C950 - Webinar 1 - Let's Go hashing : https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71
class HashTable:

    # Constructor with initial capacity as parameter.
    # Assigns all the buckets to an empty list.
    # Space Complexity = O(n)
    # Time Complexity = O(n)

    def __init__(self, initial_capacity=40):
        self.table = []
        for bucket in range(initial_capacity):
            self.table.append([])

# Creates hash key to be inserted in hash table
    @staticmethod
    def hash_key(key):
        key_hash = int(key) % 10
        return key_hash

    # Function tha will insert the specified packaged as an item into the hash table
    # Space Complexity = O(n)
    # Time Complexity = O(n)
    def insert(self, key, value):
        bucket = self.hash_key(key)
        key_value = [key, value]
        self.table[bucket].append(key_value)

    # Function that will search for a  certain package if a matching key from the hash table is found.
    # Space Complexity = O(n)
    # Time Complexity = O(n)
    def return_package(self, key):
        bucket = self.hash_key(int(key))
        for pair in self.table[bucket]:
            if pair[0] == key:
                return pair[1]

    # Function that will search for a package if a matching key from the hash table is found.
    # Space Complexity = O(n)
    # Time Complexity = O(n)
    def return_all_package(self):
        return self.table

