from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    #
    # line = Line(Point(50, 50), Point(400, 400))
    # win.draw_line(line, "red")
    cell = Cell(Point(50, 50), Point(100, 100), win, has_top_wall=False)
    cell = Cell(Point(50, 50), Point(100, 100), win, has_right_wall=False)
    cell = Cell(Point(50, 50), Point(100, 100), win, has_bottom_wall=False)
    cell = Cell(Point(50, 50), Point(100, 100), win, has_left_wall=False)
    # cell2 = Cell(Point(0, 0), Point(-10, -10), win)
    cell.draw()
    # cell2.draw()
    #
    win.wait_for_close()


main()
