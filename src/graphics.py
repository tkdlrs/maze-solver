from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False        

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
    
    def close(self):
        self.__running = False

#
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#
class Line:
    def __init__(self, point_one, point_two):
        self.p1 = point_one
        self.p2 = point_two
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x,self.p1.y, self.p2.x,self.p2.y, fill=fill_color, width=2)

#
class Cell: 
    def __init__(self, p1, p2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        #
        self._x1 = p1.x 
        self._y1 = p1.y
        #
        self._x2 = p2.x
        self._y2 = p2.y
        #
        self._win = win 
        #
    def draw(self):
        wall = {
            "t": self.has_top_wall,
            "r": self.has_right_wall,
            "b": self.has_bottom_wall,
            "l": self.has_left_wall
        }

        print('cell called draw')
        print(wall["t"], 'wall["t"]')

        if wall["t"]:
         line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
         self._win.draw_line(line)
        #
        if wall["r"]:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        #
        if wall["b"]:
            line = Line(Point(self._x2, self._y2), Point(self._x1, self._y2))
            self._win.draw_line(line)
        #
        if wall["l"]:
            line = Line(Point(self._x1, self._y2), Point(self._x1, self._y1))
            self._win.draw_line(line)
 

