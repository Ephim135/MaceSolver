from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
     
    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(100, 300, 100, 300)

    c3 = Cell(win)
    c3.has_right_wall = False
    c3.has_top_wall = False
    c3.draw(400, 600, 400, 600)   
        
    win.wait_for_close()

main()