from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.win = win

    def draw(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.x1 > self.x2:
            big_x = self.x1
            small_x = self.x2
        else:
            big_x = self.x2
            small_x = self.x1
        if self.y1 > self.y2:
            big_y = self.y1 
            small_y = self.y2
        else:
            big_y = self.y2
            small_y = self.y1
        if self.has_left_wall:
            left_wall = Line(Point(small_x, big_y), Point(small_x, small_y))
            self.win.draw_line(left_wall)
        if self.has_right_wall:
            right_wall = Line(Point(big_x, big_y), Point(big_x, small_y))
            self.win.draw_line(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(small_x, small_y), Point(big_x, small_y))
            self.win.draw_line(bottom_wall)
        if self.has_top_wall:
            top_wall = Line(Point(small_x, big_y), Point(big_x, big_y))
            self.win.draw_line(top_wall)