#!/usr/bin/env python3

import re
import string
import location
import player
import item

class Game:

    def __init__(self):
        self.running = True
        self.player = player.Player(self)
        self.player.inventory = [item.Rock()]
        self.commands = self.player.commands
        self.worldmap = location.worldmap

    def run(self):
        ''' This method runs the game loop. '''
        while self.running:
            room = self.tileAt(self.player.x, self.player.y)
            print(room.introText())
            self.interpreter() 

    def interpreter(self):
        ''' This method interprets commands sent by the player. '''
        pinput = input("ACTION: ").lower()

        for command in self.commands:
            commandinput = r'^(' + command + r')(.*)'
            matchObj = re.match(commandinput, pinput)
            if matchObj:
                self.commands[command]()

    def tileAt(self, x, y):
        ''' This method checks to see if a tile exists at the given
            coordinates.
        '''
        if x < 0 or y < 0:
            return None 
        try:
            return self.worldmap[y][x]
        except IndexError:
            return None 
        
if __name__ == '__main__':
    g = Game()
    g.run()
