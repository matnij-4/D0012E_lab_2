# -*- coding: utf-8 -*-

import key
import hashtable

""" De olika probefunktionerna med tillhörande hjälpfunktioner
"""
class hashing():
    def __init__(self, tableSize, valueC = 50, rehashMultiplyer = 2):
        self.ldown = 0
        self.lup = 0
        self.tableSize = tableSize
        self.hashtable = hashtable.hashtable(tableSize)
        self.valueC = valueC
        self.rehashMultiplyer = rehashMultiplyer
        self.numProbes = 0
        self.rehashes = 0
        self.maxCollisionChain = 0
        self.collisionCounter = 0
        self.curCollisionChain = 0

    """ Räknar collisions och uppdaterar maximal collision chain
    """
    def collisionCount(self, collision):
        if collision:
            self.collisionCounter += 1
            self.curCollisionChain += 1
            if self.curCollisionChain > self.maxCollisionChain:
                self.maxCollisionChain = self.curCollisionChain
        else:
            self.curCollisionChain = 0

    """ Tar ett element och sätter hashed_key och function_key till h(key) med pythons inbygda hash function
        (som i det här fallet inte gör något)
    """
    def hashfunction(self, keyObj):
        keyObj.hashed_key = (hash(keyObj.key) % self.hashtable.tableSize)
        keyObj.function_key = (hash(keyObj.key) % self.hashtable.tableSize)

    """ Skapar ett nytt hashtable som är rehashMultiplyer gånger så stor. insertar sedan alla element från det gamla
        till det nya.
    """
    def rehash(self):
        self.rehashes = self.rehashes + 1
        old_hashtable = self.hashtable
        self.tableSize = int(self.tableSize*self.rehashMultiplyer)
        self.hashtable = hashtable.hashtable(self.tableSize)
        for item in old_hashtable.table:
            if isinstance(item, key.key):
                self.rehashProbing(item, False)

    """ Implementation av variant 1 från labspec.
    """
    def closestProbing(self, keyObj):
        self.hashfunction(keyObj)
        collision = False
        i = 0
        if self.ldown <= self.lup:
            direction = 1 #down
            self.ldown += 1
        else:
            direction = -1 #up
            self.lup += 1

        while not self.hashtable.isEmpty(keyObj.hashed_key):
            keyObj.hashed_key = ((keyObj.hashed_key+direction) % self.hashtable.tableSize)
            i += 1
            collision = True
        self.hashtable.insert(keyObj.hashed_key, keyObj)

        self.collisionCount(collision)
        return i

    """ implementation av variant 2 från labspec.
    """
    def rehashProbing(self, keyObj, collision):
        self.hashfunction(keyObj)
        hX_step = 0 # antalet steg från h(key) till tom position. 
        position = 0 # itterator

        while True:
            if self.hashtable.isEmpty(keyObj.hashed_key): 
                if hX_step <= self.valueC: 
                    self.hashtable.insert(keyObj.hashed_key, keyObj)
                    self.collisionCount(collision)
                    return hX_step + position
                else: 
                    posJ = hX_step + keyObj.function_key
                    while position <= self.valueC:
                        keyY = self.hashtable.getKey(keyObj.function_key)
                        fir = abs(posJ - keyY.function_key)                         # Om abs(tomma positionen - h(y) <= C
                        sec = (self.hashtable.tableSize - posJ) + keyY.function_key # eller om hashtableLength - tomma positionen + h(y) <= C 
                        if fir <= self.valueC or sec <= self.valueC:                # så ska de swappas
                            self.hashtable.insert(keyObj.hashed_key, keyY)
                            self.hashtable.insert(keyObj.function_key, keyObj)
                            self.collisionCount(collision)
                            return hX_step + position

                        keyObj.function_key = ((keyObj.function_key + 1) % self.hashtable.tableSize) # kollar h(y) på nästa position
                        position += 1

                    self.rehash() # Rehash genomförs
                    self.rehashProbing(keyObj, collision) # keyn sätts in på nytt
                    self.collisionCount(collision)
                    return hX_step + position
            else:
                collision = True
                keyObj.hashed_key = ((keyObj.hashed_key + 1) % self.hashtable.tableSize)
                hX_step += 1
                if keyObj.hashed_key == keyObj.function_key: # om ingen tom position hittas så reshashas även så
                    self.rehash()
                    self.rehashProbing(keyObj, collision)
                    self.collisionCount(collision)
                    return hX_step + position

    """ Vanlig linjär probing
    """
    def defaultProbing(self, keyObj):
        self.hashfunction(keyObj)
        collision = False
        i = 0
        while not self.hashtable.isEmpty(keyObj.hashed_key):
            i += 1
            keyObj.hashed_key = ((keyObj.hashed_key+1) % self.hashtable.tableSize)
            collision = True
        self.hashtable.insert(keyObj.hashed_key, keyObj)

        self.collisionCount(collision)
        return i


    def getLoadFactor(self):
        totalItems = 0.0
        for curItem in self.hashtable.table:
            if isinstance(curItem, key.key):
                totalItems += 1
        return (totalItems / len(self.hashtable.table))

    def getNumProbes(self):
        return self.numProbes


    def setNumProbes(self, incrVal):
        self.numProbes += incrVal


    def getRehashes(self):
        return self.rehashes


    def getMaxCollosionChain(self):
        return self.maxCollisionChain


    def getCollisionCounter(self):
        return self.collisionCounter

    def getUpDown(self):
        return [self.lup, self.ldown]



def test():
    testa = hashing(20)
    for x in range(1,20):
        newKey = key.key(10, x)
        testa.rehashProbing(newKey, False)
        print (testa.hashtable.table)
    print (testa.hashtable.table)

test()

