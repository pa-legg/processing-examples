import math
import time
import random

grid = []
grid_size = 40
grid_cell_size = 10
display_margin = 50
last_updated_x = -1
last_updated_y = -1
started = False

def setup():
    global grid
    size(800,500)
    grid = create_grid(grid_size)

def draw():
    background(80,20,200)
    if started:
        update_grid()
        time.sleep(0.1)
    draw_grid()
    draw_controls()

def create_grid(g_size):
    grid = []
    grid_row = [0] * g_size 
    for y in range(g_size):
        grid.append(grid_row[:])
    return grid

def update_grid():
    global grid
    new_grid = create_grid(grid_size)
    for y in range(len(grid)):
        for x in range(len(grid)):
            neighbour_count = 0
            for yy in range(-1,2):
                for xx in range(-1,2):
                    x_is_within_bounds = (x + xx > -1 and x + xx < len(grid)) 
                    y_is_within_bounds = (y + yy > -1 and y + yy < len(grid)) 
                    if xx == 0 and yy == 0:
                        pass
                    elif x_is_within_bounds and y_is_within_bounds:
                        if grid[y+yy][x+xx] == 1:
                            neighbour_count = neighbour_count + 1
            if grid[y][x] == 1:
                if neighbour_count < 2:
                    new_grid[y][x] = 0
                elif neighbour_count > 3:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = 1
            else:
                if neighbour_count == 3:
                    new_grid[y][x] = 1
    grid = new_grid
                
def draw_grid():
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == 0:
                fill(255)
            else:
                fill(255,0,0)
            rect(display_margin+(x*grid_cell_size),\
                 display_margin+(y*grid_cell_size),\
                 grid_cell_size,grid_cell_size)
            
def draw_controls():
    grid_edge = (display_margin+(len(grid)*grid_cell_size)) + 20
    fill(255)
    textSize(24);
    text("Start (Press 'Space Bar')", grid_edge, display_margin + 80); 
    textSize(24);
    text("Reset (Press 'r')", grid_edge, display_margin + 130); 
    
def clear_grid():
    global grid
    grid = create_grid(grid_size)
             
def mousePressed():
    grid_cell_x = (mouseX-display_margin) / grid_cell_size
    grid_cell_y = (mouseY-display_margin) / grid_cell_size
    if mouseButton == LEFT:
        set_grid_cell(grid_cell_x, grid_cell_y, 1)
    else:
        set_grid_cell(grid_cell_x, grid_cell_y, 0)

def mouseDragged():
    grid_cell_x = (mouseX-display_margin) / grid_cell_size
    grid_cell_y = (mouseY-display_margin) / grid_cell_size
    if mouseButton == LEFT:
        set_grid_cell(grid_cell_x, grid_cell_y, 1)
    else:
        set_grid_cell(grid_cell_x, grid_cell_y, 0)
    
def set_grid_cell(grid_cell_x, grid_cell_y, value):
    global grid
    if grid_cell_x < 0:
        grid_cell_x = 0
    if grid_cell_x >= len(grid):
        grid_cell_x = len(grid) - 1
    if grid_cell_y < 0:
        grid_cell_y = 0
    if grid_cell_y >= len(grid):
        grid_cell_y = len(grid) - 1
    grid[grid_cell_y][grid_cell_x] = value

def keyPressed():
    global started
    if keyCode == RIGHT:
        update_grid()
    if key == ' ':
        started = not started
        print started
    if key == 'r':
        clear_grid()
