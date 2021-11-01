
#This class allows us to create a hash table object with size 19.
#We will store our data here.
class ChainHash(object):
    #This is the function called by default when creating a ChainHash object.  It sets the hash table size to 19
    #Time complexity: O(N)
    def __init__(self, size = 19):
        self.hash_table = [[] for _ in range(size)]

    #It calculates the key value for the hash table
    #Time complexity: O(1)
    def hashing(self, keyvalue):
        return int(keyvalue) % len(self.hash_table)


    #It inserts the value in the hash table using the hash key
    #Time complexity: O(1)
    def insert(self, keyvalue, value):
        hash_key = self.hashing(keyvalue)
        self.hash_table[hash_key].append(value)

        
    #It removes a value from the hash table using the hash key and desired value
    #Time complexity: O(N)
    def remove(self, keyvalue):
        hash_key = self.hashing(keyvalue)
        for item in self.hash_table[hash_key]:
            if int(item[0]) == keyvalue:
                self.hash_table[hash_key].pop(keyvalue)

    #It returns the hash table
    #Time complexity: O(1)
    def get_hash_table(self):
        return self.hash_table
    
    #It looks for a value in the hash table
    #Time complexity: O(N^2)
    def lookup(self, ID):
        for i in range(len(self.hash_table)):
            for j in self.hash_table[i]:
                if ID == int(j.get_ID()):
                    return j
                    break



