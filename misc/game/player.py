#!/usr/bin/env python3

class Player:

    def __init__(self, game):
        self.game = game
        self.x = 1
        self.y = 2 
        self.commands = self.commands() 
        self.inventory = []

    def commands(self):
        return {
            'north': self.moveNorth,
            'south': self.moveSouth,
            'east': self.moveEast,
            'west': self.moveWest,
            'fart': self.fart,
            'quit': self.quit,
            'inv': self.showInventory,
        }
    
    def showInventory(self):
        for item in self.inventory:
            print('\n----- INVENTORY ----- ')
            print('| ITEM\tDESCRIPTION')
            print('| ' + item.name + '\t' + item.description)
        print('--------------------- \n')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy 

    def moveNorth(self):
        self.move(dx=0, dy=-1)

    def moveSouth(self):
        self.move(dx=0, dy=1)

    def moveEast(self):
        self.move(dx=1, dy=0)

    def moveWest(self):
        self.move(dx=-1, dy=0)
    
    def fart(self):
        ''' This causes the player to fart. '''
        print("You fart loudly.")
    
    def quit(self):
        ''' This quits the player from the game. '''
        self.game.running = False
