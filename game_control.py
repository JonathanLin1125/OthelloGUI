'''
Class that calls the two windows

@author: jonathanlin
'''
import welcome_gui
import game_gui

if __name__ == "__main__":
    welcome = welcome_gui.Welcome()
    welcome.run()
    
    if welcome.begin == True:
        game = game_gui.Game(welcome.row, welcome.col, welcome.turn, welcome.mode)
        game.run()

