'''
Created on May 17, 2017

@author: jonathanlin
'''

class Othello:
    """
    Othello class holds all information on the current Othello game being played
    """
    def __init__(self, row:int, col:int, turn:str, mode:str):
        """
        Initializes all the variables that will be stored within the Othello class
        """
        self.row = row
        self.col = col
        self.turn = turn
        self.mode = mode
        self.bcount = 0
        self.wcount = 0
        self.game_board = self._create_board()

        self.list_replace = []
   
        
    def _create_board(self)->[[]]:
        """
        Creates the board given the user input's board and returns the 2D list
        """
        game_board = []
        for row in range(self.row + 1):
            row_list = []
            for col in range(self.col + 1):
                row_list.append(".")
            game_board.append(row_list)
        return game_board
    
    def change_turn(self):
        """
        Changes turn only if the other color has a valid move
        """
        if self.turn == "B":
            self.turn = "W"
            if self.check_end():
                self.turn = "B"
        elif self.turn == "W":
            self.turn = "B"
            if self.check_end():
                self.turn = "W"
                
    def count_disks(self):
        """
        Counts the number of disks for each color in the current game state
        """
        self.bcount = 0
        self.wcount = 0
        for y in range(self.row + 1):
            for x in range(self.col + 1):
                if self.game_board[y][x] == "B":
                    self.bcount += 1
                elif self.game_board[y][x] == "W":
                    self.wcount += 1
                    
    def get_list_moves(self, row:int, col:int):
        """
        Gets a list of pieces to flip given the user's input
        Appends each direction onto the list, each method either returns a coordinate pair or None(for no move)
        """
        self.list_replace = []
        if(self.game_board[row][col] == "."):
            self.list_replace.append(self._check_left(row, col))
            self.list_replace.append(self._check_right(row, col))
            self.list_replace.append(self._check_up(row, col))
            self.list_replace.append(self._check_down(row, col))
            self.list_replace.append(self._check_back_diag_up(row, col))
            self.list_replace.append(self._check_back_diag_down(row, col))
            self.list_replace.append(self._check_forward_diag_up(row, col))
            self.list_replace.append(self._check_forward_diag_down(row, col))
       
    def check_valid(self)->bool:
        """
        If there is a valid move in the list, return True, otherwise return False as the move is not valid
        """
        valid = False
        for move in self.list_replace:
            if move != None:
                valid = True
        
        return valid
    
    def turn_disks(self, row_input:int, col_input:int):
        """
        Flips all the disks between the list of endpoints and the user's input
        """
        for coord in self.list_replace:
            if coord != None:
                self._flip_line(coord[0], coord[1], row_input, col_input)
        
    def _flip_line(self, row:int, col:int, row_input:int, col_input:int): 
        """
        Private variable, given two sets of coordinates, method will flip all the pieces in between to the player's color
        """
        if row - row_input < 0:
            constant_row = -1
        elif row - row_input > 0:
            constant_row = 1
        else:
            constant_row = 0
            
        if col - col_input < 0:
            constant_col = -1
        elif col - col_input > 0:
            constant_col = 1
        else:
            constant_col = 0
        
        if constant_col == 0:
            iterate = abs(row - row_input)
        elif constant_row == 0:
            iterate = abs(col - col_input)
        else:
            iterate = abs(row - row_input)
            
        for disk in range(iterate):
                self.game_board[row_input][col_input] = self.turn     
                row_input += constant_row
                col_input += constant_col 
         
    def check_end(self)->bool:
        """
        Makes sure that there is still a valid move on the board, if not, return True as the game is over, else return False
        """
        for y in range(self.row + 1):
            for x in range(self.col + 1):
                if(self.game_board[y][x] == "."):
                    self.get_list_moves(y, x)
                    if(self.check_valid() == True):
                        return False
        return True
    
    def _check_left(self, row:int, col:int)->(int, int):
        """
        Checks if users's move has a move to the left, if so return coordinates, else return None
        """
        if col == 0:
            return None
        else:
            if(self.game_board[row][col - 1] != self.turn and self.game_board[row][col - 1] != "."):
                for coord in range(1, col):
                    if(self.game_board[row][col - 1 - coord] == self.turn):
                        return (row, col - 1 - coord)
                    elif(self.game_board[row][col - 1 - coord] == "."):
                        return None
                return None
                    
    def _check_right(self, row:int, col:int)->(int, int):
        """
        Checks if users's move has a move to the right, if so return coordinates, else return None
        """
        if col == self.col:
            return None
        else:
            if(self.game_board[row][col + 1] != self.turn and self.game_board[row][col + 1] != "."):
                for coord in range(1, self.col - col):
                    if(self.game_board[row][col + 1 + coord] == self.turn):
                        return (row, col + 1 + coord)
                    elif(self.game_board[row][col + 1 + coord] == "."):
                        return None
                return None
        
    def _check_up(self, row:int, col:int)->(int, int):
        """
        Checks if users's move has a move up, if so return coordinates, else return None
        """
        if row == 0:
            return None
        else:
            if(self.game_board[row - 1][col] != self.turn and self.game_board[row - 1][col] != "."):
                for coord in range(1, row):
                    if(self.game_board[row - 1 - coord][col] == self.turn):
                        return(row - 1 - coord, col)
                    elif(self.game_board[row - 1 - coord][col] == "."):
                        return None
                return None
        
    def _check_down(self, row:int, col:int)->(int, int):
        """
        Checks if users's move has a move down, if so return coordinates, else return None
        """
        if row == self.row:
            return None
        else:
            if(self.game_board[row + 1][col] != self.turn and self.game_board[row + 1][col] != "."):
                for coord in range(1, self.row - row):
                    if(self.game_board[row + 1 + coord][col] == self.turn):
                        return (row + 1 + coord, col)
                    elif(self.game_board[row + 1 + coord][col] == "."):
                        return None
                return None
        
    def _check_back_diag_up(self, row:int, col:int)->(int, int):
        """
        Checks if the user's move has a move in the top left direction, if so return coordinates, else return None
        """
        if row == 0 or col == 0:
            return None
        else:
            if(self.game_board[row - 1][col - 1] != self.turn and self.game_board[row - 1][col - 1] != "."):
                if col <= row:
                    for coord in range(1, col): #LEFT METHOD
                        if(self.game_board[row - 1 - coord][col - 1 - coord] == self.turn):
                            return (row - 1 - coord, col - 1 - coord)
                        elif(self.game_board[row - 1 - coord][col - 1 - coord] == "."):
                            return None
                else:
                    for coord in range(1, row): #UP METHOD
                        if(self.game_board[row - 1 - coord][col - 1 - coord] == self.turn):
                            return(row - 1 - coord, col - 1 - coord)
                        elif(self.game_board[row - 1 - coord][col - 1 - coord] == "."):
                            return None
                return None

    def _check_back_diag_down(self, row:int, col:int)->(int, int):
        """
        Checks if the user's move has a move in the bottom right direction, if so return coordinates, else return None
        """
        if row == self.row or col == self.col:
            return None
        else:
            if(self.game_board[row + 1][col + 1] != self.turn and self.game_board[row + 1][col + 1] != "."):
                if self.col - col <= self.row - row:
                    for coord in range(1, self.col - col): #RIGHT METHOD
                        if(self.game_board[row + 1 + coord][col + 1 + coord] == self.turn):
                            return (row + 1 + coord, col + 1 + coord)
                        elif(self.game_board[row + 1 + coord][col + 1 + coord] =="."):
                            return None
                else:
                    for coord in range(1, self.row - row): #DOWN METHOD
                        if(self.game_board[row + 1 + coord][col + 1 + coord] == self.turn):
                            return (row + 1 + coord, col + 1 + coord)
                        elif(self.game_board[row + 1 + coord][col + 1 + coord] == "."):
                            return None
                    
                return None

    def _check_forward_diag_up(self, row:int, col:int)->(int, int):
        """
        Check if the user's move has a move in the top right direction, if so return coordinates, else return None
        """
        if row == 0 or col == self.col:
            return None
        else:
            if(self.game_board[row - 1][col + 1] != self.turn and self.game_board[row - 1][col + 1] != "."):
                if self.col - col >= row:
                    for coord in range(1, row):
                        if(self.game_board[row - 1 - coord][col + 1 + coord] == self.turn):
                            return (row - 1 - coord, col + 1 + coord)
                        elif(self.game_board[row - 1 - coord][col + 1 + coord] == "."):
                            return None
                else:
                    for coord in range(1, self.col - col):
                        if(self.game_board[row - 1 - coord][col + 1 + coord] == self.turn):
                            return (row - 1 - coord, col + 1 + coord)
                        elif(self.game_board[row - 1 - coord][col + 1 + coord] == "."):
                            return None
                return None
                    
    def _check_forward_diag_down(self, row:int, col:int)->(int, int):
        """
        Check if the user's move has a move in the bottom right direction, if so return coordinates, else return None
        """
        if row == self.row or col == 0:
            return None
        else:
            if(self.game_board[row + 1][col - 1] != self.turn and self.game_board[row + 1][col - 1] != "."):
                if col >= self.row - row:
                    for coord in range(1, self.row - row):
                        if(self.game_board[row + 1 + coord][col - 1 - coord] == self.turn):
                            return (row + 1 + coord, col - 1 - coord)
                        elif(self.game_board[row + 1 + coord][col - 1 - coord] =="."):
                            return None
                else:
                    for coord in range(1, col):
                        if(self.game_board[row + 1 + coord][col - 1 - coord] == self.turn):
                            return (row + 1 + coord, col - 1 - coord)
                        elif(self.game_board[row + 1 + coord][col - 1 - coord] == "."):
                            return None
                return None
            
    def draw_disks(self):
        """
        Prints the board at its current state
        """
        for y in self.game_board:
            print(" ".join(y))