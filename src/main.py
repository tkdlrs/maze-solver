from graphics import Window
from maze import Maze

import sys 

def main():
    screen_x = 800
    screen_y = 600
    sys.setrecursionlimit(1000)
    win = Window(screen_x, screen_y)
    #
    num_rows = 12 
    num_cols = 16
    margin = 50 
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    #
    # maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze created")
    is_solvable = maze.solve()
    # Something about this is confusing me.
    if is_solvable:
        print("It is not possible to solve this maze.")
    else:
        print("Maze solved!")
    #
    win.wait_for_close()
    #
#
main()
