from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win

    def __repr__(self):
        return f"self.x1: {self._x1}\nself.x2: {self._x2}\nself.y1: {self._y1}\nself.y2: {self._y2}\nhas_top_wall: {self.has_top_wall}"

    def draw(self, x1, x2, y1, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        line_color_left = 'white'
        line_color_right = 'white'
        line_color_bottom = 'white'
        line_color_top = 'white'
        if self.has_left_wall:
            line_color_left = 'black'
        if self.has_right_wall:
            line_color_right = 'black'
        if self.has_bottom_wall:
            line_color_bottom = 'black'
        if self.has_top_wall:
            line_color_top = 'black'
        self._win.draw_line(left_wall,fill_color=line_color_left)
        self._win.draw_line(right_wall,fill_color=line_color_right)
        self._win.draw_line(bottom_wall,fill_color=line_color_bottom)
        self._win.draw_line(top_wall,fill_color=line_color_top)

    def draw_move(self, to_cell, undo=False):
        self.center = self.get_center()
        to_cell.center = to_cell.get_center()
        if not undo:
            color = "red"
        else:
            color = "grey"
        line = Line(self.center, to_cell.center)
        self._win.draw_line(line, fill_color=color)

    def get_center(self):
        center = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        return center