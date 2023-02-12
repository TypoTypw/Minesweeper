from tkinter import Button, Label,messagebox
import settings
import random
import sys


class Cell:
  
    list_of_cells = []
    cell_counter = settings.cell_count
    cell_count_label = None
    
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_button_object = None
        self.is_open = False
        self.is_possible_mine = False
        self.x =  x
        self.y = y
        # Append each instance of a cell
        Cell.list_of_cells.append(self)
        
        
    def create_Button_Cell(self, location):
        button = Button(
            location,
            width=1,
            height=1,
            highlightthickness=0,
            bg='white'
        )
        # Left click event
        button.bind('<Button-1>', self.left_click_event)
        # Right click event
        button.bind('<Button-3>', self.Right_click_event)
        
        self.cell_button_object = button
        
        
    def left_click_event(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.get_surrounding_cells_mine_count == 0:
                for cells in self.get_surrounding_cells:
                    cells.show_cell()
            self.show_cell()
            # If number of cells left equals number of mines the player wins
            if Cell.cell_counter == 0:
                messagebox.showinfo('Congratulations', 'You Won the Game')
                sys.exit()
        # Cancel event if cell is opened
        self.cell_button_object.unbind('<Button-1>')
        self.cell_button_object.unbind('<Button-3>') 
        
        
    def Right_click_event(self, event):
        
        if not self.is_possible_mine and not self.is_open:
            self.cell_button_object.configure(bg='orange')
            self.is_possible_mine = True
        else:
            self.cell_button_object.configure(bg='white')
            self.is_possible_mine = False
        
        
    def show_mine(self):
        self.cell_button_object.configure(bg='red')
        messagebox.showinfo('Game Over', 'You clicked on a mine')
        sys.exit()
          
    
    @property
    def get_surrounding_cells(self):
        surrounding_cells = [
            
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x+1, self.y),
            
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y-1),
            
            
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1),
        ]
        # Remove any None value
        surrounding_cells = [cell for cell in surrounding_cells if cell is not None]
        return surrounding_cells
        
        
    @property    
    def get_surrounding_cells_mine_count(self):
        counter = 0
        for cell in self.get_surrounding_cells:
            if cell.is_mine:
                counter+=1
        return counter
    
        
    def show_cell(self):
        if not self.is_open:
            Cell.cell_counter -= 1
            self.cell_button_object.configure(text=self.get_surrounding_cells_mine_count)
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(text=f'Cells Left: {Cell.cell_counter}')
            self.cell_button_object.configure(bg='white')
        # Mark the selected cell as open 
        self.is_open = True     
        
        
    def get_cell_by_axis(self, x, y):
        for cell in Cell.list_of_cells:
            if cell.x == x and cell.y == y:
                return cell
    
    
    @staticmethod
    def remdomize_mine():
        mine_list = random.sample(Cell.list_of_cells, settings.mine_count)
        for mines in mine_list:
            mines.is_mine = True
    
    
    @staticmethod
    def create_cell_counter_label(location):
        label = Label(
            location,
            text=f'Cells Left: {Cell.cell_counter}',
            fg='white',
            bg='green',
            font=('Garamond',20)
        )
        Cell.cell_count_label = label
    
    
    def __repr__(self) -> str:
        return f'Cell({self.x},{self.y}) '