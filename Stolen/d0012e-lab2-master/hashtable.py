# -*- coding: utf-8 -*-

""" En lista av satt längd.
"""

class hashtable:
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.table = [None] * int(tableSize)

    """ Kollar om positionen är tom.
    """
    def isEmpty(self, index):
        return self.table[index] is None

    """ Sätter in ett element på en position.
    """
    def insert(self, index, item):
        self.table[index] = item

    """ Returnerar elementet på positionen.
    """
    def getKey(self, index):
        return self.table[index]