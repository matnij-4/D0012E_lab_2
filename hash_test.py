import random
import time

class HashTable_probe(object):

    def __init__(self, max_length):
        self.max_length = max_length
        self.max_load_factor = 0.75
        self.length = 0
        self.table = [None] * self.max_length
        self.collNum = 0
        self.collJump = 0


    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        self.length += 1
        hashed_key = self._hash(key)
        flagCol = False
        
        while self.table[hashed_key] is not None:
            self.collJump = self.collJump + 1
            flagCol = True
            if self.table[hashed_key][0] == key:
                self.length -= 1
                break
            hashed_key = self._increment_key(hashed_key)

        if flagCol:
            self.collNum = self.collNum + 1
        tuple = (key, value)
        self.table[hashed_key] = tuple


    def __getitem__(self, key):
        index = self._find_item(key)
        return self.table[index][1]

    def __delitem__(self, key):
        index = self._find_item(key)
        self.table[index] = None

    def _hash(self, key):
        return key % self.max_length
    

    def _increment_key(self, key):
        return (key + 1) % self.max_length

    def __str__(self):
        return str(self.table)

    def _find_item(self, key):
        hashed_key = self._hash(key)
        if self.table[hashed_key] is None:
            raise KeyError
        if self.table[hashed_key][0] != key:
            original_key = hashed_key
            while self.table[hashed_key][0] != key:
                hashed_key = self._increment_key(hashed_key)
                if self.table[hashed_key] is None:
                    raise KeyError
                if hashed_key == original_key:
                    raise KeyError
        return hashed_key






####################################
######                #################
                ##################




class HashTable_prob_var(object):

    def __init__(self, max_length):
        self.max_length = max_length
        self.max_load_factor = 0.75
        self.length = 0
        self.table = [None] * self.max_length
        self.cCount = 0
        self.collNum = 0
        self.collJump = 0

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):

        
        self.length += 1
        hashed_key = self._hash(key)
        if self.table[hashed_key] == None:
            flag = True
        else:
            self.collNum = self.collNum + 1
            flag = self.table[hashed_key][2]
            self.table[hashed_key] = (self.table[hashed_key][0], self.table[hashed_key][1], not flag)


        while self.table[hashed_key] is not None:
            self.collJump = self.collJump + 1
            self.cCount = self.cCount + 1
            if self.table[hashed_key][0] == key:
                self.length -= 1
                break
            hashed_key = self._increment_key(hashed_key, flag)


        
        tuple = (key, value, True)
        self.table[hashed_key] = tuple

    def __getitem__(self, key):
        index = self._find_item(key)
        return self.table[index][1]

    def __delitem__(self, key):
        index = self._find_item(key)
        self.table[index] = None

    def _hash(self, key):
#        return key % self.max_length


        return key % self.max_length

    def _increment_key(self, key, flag):

        if flag:
            return (key + 1) % self.max_length
        
        else:
            return (key - 1) % self.max_length

    def __str__(self):
        return str(self.table)

    def _find_item(self, key):
        hashed_key = self._hash(key)
        if self.table[hashed_key] is None:
            raise KeyError
        if self.table[hashed_key][0] != key:
            original_key = hashed_key
            while self.table[hashed_key][0] != key:
                hashed_key = self._increment_key(hashed_key)
                if self.table[hashed_key] is None:
                    raise KeyError
                if hashed_key == original_key:
                    raise KeyError
        return hashed_key










def randomList(n):
    randomlist = []
    for x in range(1, n+1, 1):
        randomlist.append(random.randint(0,5))
        
    return randomlist

def worstList(n):
    randomlist = []
    for x in range(1, n+1, 1):
        randomlist.append(random.randint(1,5001))
        
    return randomlist

def shufflist(n):
    shuff = []
    for x in range(1, n+1, 1):
        shuff.append(x)
    random.shuffle(shuff)
    return shuff




# Testerna

randomKeys = shufflist(1000000)

test_prob = HashTable_probe(200000)
test_var = HashTable_prob_var(200000)


timestp = time.time()
for x in range(0, 200000, 1):
    test_prob[randomKeys[x]] = x
print(time.time() - timestp)


timestp = time.time()
for x in range(0, 200000, 1):
    test_var[randomKeys[x]] = x
print(time.time() - timestp)


