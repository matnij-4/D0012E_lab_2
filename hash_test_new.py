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
        self.maxChain = 0


    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        self.length += 1
        hashed_key = self._hash(key)
        flagCol = False
        currChain = 0
        
        while self.table[hashed_key] is not None:
            currChain = currChain + 1
            self.collJump = self.collJump + 1
            flagCol = True
            if self.table[hashed_key][0] == key:
                self.length -= 1
                break
            hashed_key = self._increment_key(hashed_key)


        if self.maxChain < currChain:
            self.maxChain = currChain

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
        return (((random.randint(1,10000) * key + random.randint(1,10000)) % 420691 ) % self.max_length)
        
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
        self.collNum = 0
        self.collJump = 0
        self.maxChain = 0

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):

        hashed_key = self._hash(key)
        if self.table[hashed_key] is not None:
            self.collNum = self.collNum + 1
            currChain = 0
            
            if self.table[hashed_key][3] >= self.table[hashed_key][2]:
                # [2] is down
                self.table[hashed_key] = (self.table[hashed_key][0], self.table[hashed_key][1],self.table[hashed_key][2] +1, self.table[hashed_key][3])
                while self.table[hashed_key] is not None:
                    currChain = currChain + 1
                    self.collJump = self.collJump + 1
                    if self.table[hashed_key][0] == key:
                        self.length -= 1
                        break
                    hashed_key = self._increment_key_down(hashed_key)

                    
            else:
                self.table[hashed_key] = (self.table[hashed_key][0], self.table[hashed_key][1],self.table[hashed_key][2], self.table[hashed_key][3]+1)
                while self.table[hashed_key] is not None:
                    currChain = currChain + 1
                    self.collJump = self.collJump + 1
                    if self.table[hashed_key][0] == key:
                        self.length -= 1
                        break
                    hashed_key = self._increment_key_up(hashed_key)
                    
            if self.maxChain < currChain:
                self.maxChain = currChain


        
        tuple = (key, value, 0, 0)
        self.table[hashed_key] = tuple

    def __getitem__(self, key):
        index = self._find_item(key)
        return self.table[index][1]

    def __delitem__(self, key):
        index = self._find_item(key)
        self.table[index] = None

    def _hash(self, key):
#        return key % self.max_length
                                                                            #Best Prime
        return (((random.randint(1,10000) * key + random.randint(1,10000)) % 420691 ) % self.max_length)
#        return key % self.max_length



    def _increment_key_up(self, key):
        return (key - 1) % self.max_length

        
    def _increment_key_down(self, key):
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










def randomList(n):
    randomlist = []
    for x in range(1, n+1, 1):
        randomlist.append(random.randint(0,5))
        
    return randomlist

def worstList(n, mod):
    randomlist = []
    for x in range(1, n+1, 1):
        randomlist.append(x * mod)
        
    return randomlist

def shufflist(n):
    shuff = []
    for x in range(1, n+1, 1):
        shuff.append(x)
    random.shuffle(shuff)
    return shuff



# Testerna

randomKeys = shufflist(1000000)
worstKeys = worstList(100000, 25000)

test_prob = HashTable_probe(400000)
test_var = HashTable_prob_var(400000)


timestp = time.time()
for x in range(0, 200000, 1):
    test_prob[randomKeys[x]] = x
print(time.time() - timestp)


timestp = time.time()
for x in range(0, 200000, 1):
    test_var[randomKeys[x]] = x
print(time.time() - timestp)


