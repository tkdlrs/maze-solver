import time 
from cell import Cell 

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._cells = []
        #
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        #
        self._create_cells()
        #
        self._break_entrance_and_exit()
        #
    #
    def _create_cells(self):
        for _ in range(self._num_cols):
            column_cells = []
            for _ in range(self._num_rows):
                current_cell = Cell(self._win)
                column_cells.append(current_cell)
            #
            self._cells.append(column_cells)
        #        
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)
        #
        return 
    
    def _draw_cell(self, i, j):
        # guard clause
        if self._win is None:
            return
        #
        tl_x = self._x1 + (i * self._cell_size_x)
        tl_y = self._y1 + (j * self._cell_size_y)
        #
        br_x = tl_x + self._cell_size_x
        br_y = tl_y + self._cell_size_y
        #
        self._cells[i][j].draw(tl_x, tl_y, br_x, br_y)
        self._animate()
        #
    
    def _animate(self):
       # guard clause
        if self._win is None:
            return 
        self._win.redraw()
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell((self._num_cols - 1), (self._num_rows - 1))

    #
