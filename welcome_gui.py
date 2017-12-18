'''
Opens the initial Game option menu
Reads in the basic user inputs through widgets

@author: jonathanlin
'''
import tkinter

OPTION_LIST = ("4")

class Welcome:
    """Welcome Menu
    """
    def __init__(self):
        """Initializes the screen to set in the middle and not adjustable 
        """
        self.begin = False
        self.root_window = tkinter.Tk()
        self.root_window.resizable(width = False, height = False)
        self.root_window.wm_title("Othello Game Menu")
        
        self._add_widgets()
    
    def _row_selected(self, event:tkinter.Event):
        """Sets the # of rows the user selected to a list compatible integer
        """
        self.row = self.var.get() - 1
        
    def _col_selected(self, event:tkinter.Event):
        """Sets the # of columns the user selected to a list compatible integer
        """
        self.col = self.var2.get() - 1
    
    def _turn_selected(self):
        """Sets which player starts first
        """
        self.turn = self.var3.get()
        
    def _mode_selected(self):
        """Sets the game type ">" or "<"
        """
        self.mode = self.var4.get()
        
    def _close_selected(self):
        """Closes window if the close button is pressed
        """
        self.begin = False
        self.root_window.destroy()
    
    def _start_selected(self):
        """Closes window and sets begin to True, which lets the game_control know to 
            Start the othello game
        """
        self.begin = True
        self.root_window.destroy()

    def _add_widgets(self):
        """Adds all the widgets and labels onto the root_window
        """
        self._add_title()
        self._add_row_label()
        self._add_col_label()
        self._add_row_menu()
        self._add_col_menu()
        self._add_start_button()
        self._add_close_button()
        self._add_turn_label()
        self._add_mode_label()
        self._add_turn_radiobutton()
        self._add_mode_radiobutton()
    
    def _add_title(self):
        """Adds title 
        """
        title = tkinter.Label(self.root_window, text = "Othello Menu", font = ("Helvetica", 20))
        title.grid(row = 0, column = 0, columnspan = 4)

    def _add_row_label(self):
        """Adds Row label
        """
        row_label = tkinter.Label(self.root_window, text = "Rows")
        row_label.grid(row = 1, column = 0)

    def _add_col_label(self):
        """Adds Column Label
        """
        column_label = tkinter.Label(self.root_window, text = "Cols")
        column_label.grid(row = 1, column = 1)

    def _add_row_menu(self):
        """Adds drop down menu for rows
        """
        self.var = tkinter.IntVar()
        self.var.set(4)
        self.row = self.var.get() - 1
        row_option = tkinter.OptionMenu(self.root_window, self.var, 4, 6, 8, 10, 12, 14, 16, command = self._row_selected)
        row_option.grid(row = 2, column = 0)
        
    def _add_col_menu(self):
        """Adds drop down menu for columns
        """
        self.var2 = tkinter.IntVar()
        self.var2.set(4)
        self.col = self.var2.get() - 1
        col_option = tkinter.OptionMenu(self.root_window, self.var2, 4, 6, 8, 10, 12, 14, 16, command = self._col_selected)
        col_option.grid(row = 2, column = 1)

    def _add_start_button(self):
        """Adds the start button
        """
        start_button = tkinter.Button(self.root_window, text = "Start", command = self._start_selected)
        start_button.grid(row = 4, column = 3)
        
    def _add_close_button(self):
        """Adds the close button
        """
        close_button = tkinter.Button(self.root_window, text = "Close", command = self._close_selected)
        close_button.grid(row = 4, column = 0)
   
    def _add_turn_label(self):
        """Adds the turn label
        """
        turn_label = tkinter.Label(self.root_window, text = "Turn")
        turn_label.grid(row = 1, column = 2)

    def _add_mode_label(self):
        """Adds the mode label
        """
        mode_label = tkinter.Label(self.root_window, text = "Mode")
        mode_label.grid(row = 1, column = 3)

    def _add_turn_radiobutton(self):
        """Adds the radiobutton for the turn label
        """
        self.var3 = tkinter.StringVar()
        self.var3.set("B")
        self.turn = self.var3.get()
        b_button = tkinter.Radiobutton(self.root_window, text = "B", variable = self.var3, value = "B", command = self._turn_selected)
        w_button = tkinter.Radiobutton(self.root_window, text = "W", variable = self.var3, value = "W", command = self._turn_selected)
        
        b_button.grid(row = 2, column = 2)
        w_button.grid(row = 3, column = 2)
    
    def _add_mode_radiobutton(self):
        """Adds the radiobutton for the mode label
        """
        self.var4 = tkinter.StringVar()  
        self.var4.set(">")
        self.mode = self.var4.get()
        greater_button = tkinter.Radiobutton(self.root_window, text = ">", variable = self.var4, value = ">", command = self._mode_selected)
        less_button = tkinter.Radiobutton(self.root_window, text = "<", variable = self.var4, value = "<", command = self._mode_selected)
        
        greater_button.grid(row = 2, column = 3)
        less_button.grid(row = 3, column = 3)     
        
    def run(self):
        """Function to call to let tkinter run the window
        """
        self.root_window.mainloop()
