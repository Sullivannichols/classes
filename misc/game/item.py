#!/usr/bin/env python3

class Item:

    def __init__(self):
        self.name = ''
        self.description = ''
        
    def __str__(self):
        return self.name

class Rock(Item):

    def __init__(self):
        self.name = 'Rock'
        self.description = 'A large rock suitable for smashing faces.'

    def __str__(self):
        return self.name
