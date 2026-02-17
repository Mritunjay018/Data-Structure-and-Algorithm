class Hashing:
    def __init__(self, size):
        self.buckets = size
        self.hashtable = [[] for _ in range(size)]

    def hashvalue(self, key):
        return key % self.buckets  # division method
        
    def addKey(self, key):
        idx = self.hashvalue(key)
        self.hashtable[idx].append(key)
        print(idx)

    def searchKey(self, key):
        idx = self.hashvalue(key)
        # return index inside the list if found, otherwise None
        for i, val in enumerate(self.hashtable[idx]):
            if val == key:
                return i
        return None

    def deleteKey(self, key):
        idx = self.hashvalue(key)
        pos = self.searchKey(key)

        if pos is not None:   # key is present
            self.hashtable[idx].pop(pos)
            print(key, "is deleted")
        else:
            print("Key is not present in the hashtable")


# main()
h = Hashing(10)
h.addKey(5)
h.addKey(9)
h.addKey(3)
h.addKey(13)
h.addKey(5)


h.deleteKey(3)
h.deleteKey(3)
