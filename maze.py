from cell import Cell
import time
import random
class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None
                 ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            self._seed = random.seed(seed)

        self._create_Cells()
        self._break_entrance_and_exit()
        self._break_walls(0, 0)
        self._reset_cells_visited()
        self.solve()

    def _create_Cells(self):
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + self._cell_size_x * i
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + self._cell_size_y * j
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, x2, y1, y2)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1 )

    def _break_walls(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            have_to_visit = self._adjacent_cells(i, j)
            #add adjacent cells where visited is False to list to visit later
            #if no adjacent cellls draw cell and return
            if len(have_to_visit) == 0:
                self._draw_cell(i, j)
                return
            #random direction kill walls of cell we go to and own cell
            index_next_cell = random.randrange(len(have_to_visit))
            next_index = have_to_visit[index_next_cell]

            #check wich wall to break
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            #call _break_walls with the chosen cell
            self._break_walls(next_index[0], next_index[1])

    def _adjacent_cells(self, i, j):
        adjacent_cells = []
        # left
        if i > 0 and not self._cells[i - 1][j]._visited:
            adjacent_cells.append((i - 1, j))
        # right
        if i < self._num_cols - 1 and not self._cells[i + 1][j]._visited:
            adjacent_cells.append((i + 1, j))
        # up
        if j > 0 and not self._cells[i][j - 1]._visited:
            adjacent_cells.append((i, j - 1))
        # down
        if j < self._num_rows - 1 and not self._cells[i][j + 1]._visited:
            adjacent_cells.append((i, j + 1)) 
        return adjacent_cells
    

    def _reset_cells_visited(self):
        for rows in self._cells:
            for cell in rows:
                cell._visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i , j):
        self._animate()
        self._cells[i][j]._visited = True
        #at goal return True
        if i == self._num_cols - 1 and j == self._num_rows -1:
            return True
        # there is a cell, no wall , not visited
        #left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j]._visited:
            self._cells[i][j].draw_move(self._cells[i-1][j]) #draw move between cells
            if self._solve_r(i-1, j): #call solve_r
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True) #undo draw move
        #right
        if i < self._num_cols -1 and not self._cells[i][j].has_right_wall and not self._cells[i+1][j]._visited:
            self._cells[i][j].draw_move(self._cells[i+1][j]) #draw move between cells
            if self._solve_r(i+1, j): #call solve_r
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True) #undo draw move
        #up
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1]._visited:
            self._cells[i][j].draw_move(self._cells[i][j-1]) #draw move between cells
            if self._solve_r(i, j-1): #call solve_r
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True) #undo draw move
        #bottom
        if j < self._num_rows -1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1]._visited:
            self._cells[i][j].draw_move(self._cells[i][j+1]) #draw move between cells
            if self._solve_r(i, j+1): #call solve_r
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True) #undo draw move
        #if no way worked return False
        return False