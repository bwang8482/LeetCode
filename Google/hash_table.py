class hash_map(object):
    # list[(key, value)]
    def __init__(self):
        self.size = 128
        self.table = [None]*self.size

    def get(self, key):
        index = key % self.size
        while self.table[index] != None and self.table[index][0] != key:
            index = (index + 1) % self.size
        if self.table[index] == None:
            return -1
        else:
            return self.table[index][1]

    def put(self, key, value):
        index = key % self.size
        while self.table[index] != None and self.table[index][0] != key:
            index = (index + 1) % self.size
        self.table[index] = (key, value)
        