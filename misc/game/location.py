#!/usr/bin/env python3

class MapTile:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def introText(self):
        raise NotImplementedError("Create a subclass instead!")

class StartTile(MapTile):

    def introText(self):
        return ''' This is the start tile. ''' 

class BoringTile(MapTile):

    def introText(self):
        return ''' This is a boring tile. '''

class VictoryTile(MapTile):

    def introText(self):
        return ''' This is the victory tile. You have won! '''

worldmap = [
    [None, VictoryTile(1,0), None],
    [None, BoringTile(1,1), None],
    [BoringTile(0,2), StartTile(1,2), BoringTile(2,2)],
    [None, BoringTile(1,3), None],
]
