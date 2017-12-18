import tkinter
import othello
import math

class Game:
    def __init__(self, row:int, col:int, turn:str, mode:str):
        """Initializes basic board settings and creates window and game_state
        """
        self.row = row
        self.col = col
        self.turn = turn
        self.mode = mode
        self.game_state = othello.Othello(self.row, self.col, self.turn, self.mode)
        self.root_window = tkinter.Tk()
        self.row_list = []
        self.col_list = []
        
        block = (self.root_window.winfo_screenheight())/19

        self.width = block * (self.col + 1)
        self.height = block * (self.row + 1)
                
        self.root_window.wm_title("Full Othello")
        self._add_widgets()
        self.root_window.columnconfigure(0, weight = 1)
        self.root_window.columnconfigure(1, weight = 1)
        self.root_window.columnconfigure(2, weight = 1)

        self._set_canvas()
     
    def _set_canvas(self):     
        """Initializes canvas
        """   
        self.canvas = tkinter.Canvas(master = self.root_window,
                                     width = self.width,
                                     height = self.height,
                                     background = "green4")
        self.canvas.grid(row = 1, column = 0, columnspan = 3,
                         sticky = tkinter.S + tkinter.N + tkinter.W + tkinter.E)

        
        self.canvas.bind("<Configure>", self._on_resize)
        
        self.root_window.rowconfigure(1, weight = 1)
        self.root_window.columnconfigure(0, weight = 1)

        self._set_board()
    
    def _add_widgets(self):
        """Adds all widgets
        """
        self._add_b_label()
        self._add_w_label()
        self._add_close_button()
        self._add_start_button()
        
    def _play_game(self):
        """Begins playing the game and unbinds canvas controls
        """
        self.instruction_one.destroy()
        self.instruction_two.destroy()
        self.start_button.configure(state = "disabled")

        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-2>")
        self.canvas.unbind("<Button-3>")
        
        if(self.game_state.check_end() == True):
            self.game_state.change_turn()
        
        if(self.game_state.check_end() == True):
            self._print_winner()
        else:
            self._add_turn_label()
            self._get_move()

    def _continue_game(self):
        """Continues looping the game until it is over
        """
        self.canvas.unbind("<Button-1>")
        if(self.game_state.check_end() == True):
            self.turn_label.destroy()
            self._print_winner()
        else:
            self._get_move()
        
    def _move_turn(self):
        """Moves turn when the user chooses a coordinate
        """
        row_input = self.move[0] - 1
        col_input = self.move[1] - 1
            
        self.game_state.get_list_moves(row_input, col_input)
            
        if(self.game_state.check_valid() == False):
            self._get_move()
        else:  
            self.game_state.turn_disks(row_input, col_input)
            self.game_state.count_disks()
            self._update_label()
            self._draw_disks()
            self.game_state.change_turn()
            self._add_turn_label()
            self._continue_game()
         
    def _get_move(self):
        """Rebinds mouse to let the user choose a a move
        """
        self.move = []
        self.canvas.bind("<Button-1>", self._return_cords)
         
    def _return_cords(self, event:tkinter.Event):
        """Returns the coordinate to which the user chose
        """
        self.canvas.unbind("<Button-1>")
        self.move = self._board_cord(event.x, event.y)
        self._move_turn()
         
    def _set_board(self):
        """Initializes the board information and binds the mouse inputs to add pieces
        """
        self.instruction_one = tkinter.Label(self.root_window, text = "Left Click: B", anchor = "center")
        self.instruction_two = tkinter.Label(self.root_window, text = "Right Click: W", anchor = "center")
        self.instruction_one.grid(row = 0, column = 1, sticky = tkinter.E + tkinter.W + tkinter.S + tkinter.N)
        self.instruction_two.grid(row = 2, column = 1, sticky = tkinter.E + tkinter.W + tkinter.S + tkinter.N)
        self.canvas.bind("<Button-1>", self._draw_disk_black)
        self.canvas.bind("<Button-2>", self._draw_disk_white)
        self.canvas.bind("<Button-3>", self._delete_disk)
        
    def _on_resize(self, event:tkinter.Event):
        """Redraws the board when the board is resized
        """
        self.canvas.delete(tkinter.ALL)
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self._draw_grid()
        self._draw_disks()
        
    def _update_label(self):
        """Updates the labels so the information is up to date
        """
        self.b_label.destroy()
        self.w_label.destroy()
        self._add_b_label()
        self._add_w_label()
        
    def _draw_disk_black(self, event:tkinter.Event):
        """Draws a black disk at where the user clicks
        """
        x_cord, y_cord = self._board_cord(event.x, event.y)
        self._draw_circle(x_cord, y_cord, "black")
        self.game_state.game_board[x_cord - 1][y_cord - 1] = "B"
        self.game_state.count_disks()
        self._update_label()
        
    def _draw_disk_white(self, event:tkinter.Event):
        """Draws a white disk at where the user clicks
        """
        x_cord, y_cord = self._board_cord(event.x, event.y)
        self._draw_circle(x_cord, y_cord, "white")
        self.game_state.game_board[x_cord - 1][y_cord - 1] = "W"
        self.game_state.count_disks()
        self._update_label()
     
    def _delete_disk(self, event:tkinter.Event):
        """Deletes a disk at where the user clicks
        """
        x_cord, y_cord = self._board_cord(event.x, event.y)
        self.game_state.game_board[x_cord - 1][y_cord - 1] = "."
        self.canvas.delete(tkinter.ALL)
        self._draw_grid()
        self._draw_disks()
        self.game_state.count_disks()
        self._update_label()
        
    def _draw_disks(self):
        """Draws the disk using information from othello.py 2D list
        """
        for row in range(self.game_state.row + 1):
            for col in range(self.game_state.col + 1):
                if self.game_state.game_board[row][col] == "B":
                    self._draw_circle(row + 1, col + 1, "black")
                elif self.game_state.game_board[row][col] == "W":
                    self._draw_circle(row + 1, col + 1, "white")      
                          
    def _print_winner(self):
        """Prints the winner with a label once the game is over
        """
        if self.mode == "<":
            if(self.game_state.bcount < self.game_state.wcount):
                winner = "Black"
            elif(self.game_state.bcount > self.game_state.wcount):
                winner = "White"
            else:
                winner = "None"
        elif self.mode == ">":
            if(self.game_state.bcount > self.game_state.wcount):
                winner = "Black"
            elif(self.game_state.bcount < self.game_state.wcount):
                winner = "White"
            else:
                winner = "None"
        self.winner = tkinter.Label(self.root_window, text = "Winner: " + winner)
        self.winner.grid(row = 0, column = 1, sticky = tkinter.E + tkinter.W + tkinter. N + tkinter.S)
 
 
    def _draw_grid(self):
        """Draws the grid and sets the coordinates in a list
        """
        self.row_list = [0]
        self.col_list = [0]
        for row in range(1, self.game_state.row + 1):
            self.row_list.append(row * (self.height/(self.game_state.row + 1)))
            self.canvas.create_line(0,
                                   row * (self.height/(self.game_state.row + 1)),
                                   self.width + 6,
                                   row * (self.height/(self.game_state.row + 1)),
                                   fill = "white")
        for col in range(1, self.game_state.col + 1):
            self.col_list.append(col * (self.width/(self.game_state.col + 1)))
            self.canvas.create_line(col * (self.width/(self.game_state.col + 1)),
                                    0,
                                    col * (self.width/(self.game_state.col + 1)),
                                    self.height, fill = "white")
        self.row_list.append(self.canvas.winfo_height())
        self.col_list.append(self.canvas.winfo_width())   
            
    def _board_cord(self, x_pixel:int, y_pixel:int) ->(int, int):
        """Given raw pixel coordinates, this function returns the board coordinates
        """
        x_frac = x_pixel/self.width
        y_frac = y_pixel/self.height
        return(math.floor((y_frac * (self.row + 1)) + 1), math.floor((x_frac * (self.col + 1)) + 1))
        
    def _draw_circle(self, x_cord:int, y_cord:int, color:str): 
        """Draws a circle at the given x_cord y_cord with color given in parameter
        """
        border = self.root_window.winfo_height() * 0.002
        self.canvas.create_oval(self.col_list[y_cord - 1] + border,
                                self.row_list[x_cord - 1] + border,
                                self.col_list[y_cord] - border,
                                self.row_list[x_cord] - border,
                                fill = color)

    
    def _add_b_label(self):
        """Adds the label for how many disks black has
        """
        self.b_label = tkinter.Label(self.root_window, text = "B: " + str(self.game_state.bcount),  padx = 15, pady = 5)
        self.b_label.grid(row = 0, column = 0, sticky = tkinter.W)

    def _add_w_label(self):
        """Adds the label for how many disks white has
        """
        self.w_label = tkinter.Label(self.root_window, text = "W: " + str(self.game_state.wcount),  padx = 15, pady = 5)
        self.w_label.grid(row = 0, column = 2, sticky = tkinter.E)
        
    def _add_turn_label(self):
        """Adds the label for whose turn it is
        """
        self.turn_label = tkinter.Label(self.root_window, text = "Turn: " + self.game_state.turn) 
        self.turn_label.grid(row = 0, column = 1, sticky = tkinter.E + tkinter.W)
         
    def _close_selected(self):
        """Destroys the window once it is clicked
        """
        self.root_window.destroy()

    def _add_close_button(self):
        """Adds the close button
        """
        self.close_button = tkinter.Button(self.root_window, text = "Close", command = self._close_selected, padx = 15, pady = 15)
        self.close_button.grid(row = 2, column = 0)
    
    def _add_start_button(self):
        """Adds the start button
        """
        self.start_button = tkinter.Button(self.root_window, text = "Start", command = self._play_game, padx = 15, pady = 15)
        self.start_button.grid(row = 2, column = 2)
    
    def run(self):
        """Puts the window into mainloop
        """
        self.root_window.mainloop() 
    
        