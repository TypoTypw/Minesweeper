from tkinter import *
from cell import Cell
import settings


window = Tk()
window.configure(bg='black')
window.geometry(f'{settings.window_width}x{settings.window_height}')
window.title('Minesweeper')
window.resizable(False,False)

top_Penal = Frame(window, bg='green', 
                  width=settings.window_width, 
                  height=settings.window_height/5
                  )
top_Penal.place(x=0, y=0)

bottom_Penal = Frame(window, 
                     bg='blue', 
                     width=settings.window_width, 
                     height=settings.window_height/8
                     )
bottom_Penal.place(x=0, y=settings.window_height-(settings.window_height/8))

title = Label(bottom_Penal,text='MINESWEEPER' ,bg='blue',fg='white',font=('Garamond',20))
title.place(x=settings.window_width/3,y=(settings.window_height/8)/4)

center_Penal = Frame(window,
                     bg='red',
                     width=settings.window_width,
                     height=settings.window_height - ((settings.window_height/8) + (settings.window_height/5))
                     )
center_Penal.place(x=0,y=settings.window_height/5)


for row in range(settings.grid_height):
    
    for collumn in range(settings.grid_width):
      
        cell = Cell(row,collumn)
        cell.create_Button_Cell(center_Penal)
        
        cell.cell_button_object.grid(
            row=row,
            column=collumn,
            sticky=N+S+E+W
        )


Cell.create_cell_counter_label(top_Penal)
Cell.cell_count_label.place(x=0,y=(settings.window_height/5)/4) 
Cell.remdomize_mine()

# Keep the window open until user clicks close
window.mainloop()