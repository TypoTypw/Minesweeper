import math

window_width = 680
window_height = 430

grid_width = 20
grid_height = 10

mine_count = math.floor((grid_height+grid_width)*0.25)
cell_count = (grid_height*grid_width) - mine_count