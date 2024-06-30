from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)

    point1 = Point(40,40)
    point2 = Point(80,80)
    line1 = Line(point1, point2)

    point3 = Point(100,100)
    point4 = Point(120,120)
    line2 = Line(point3, point4)

    win.draw_line(line1)
    win.draw_line(line2, "red")

    c1 = Cell(win)
    c2 = Cell(win)

    c1.draw(300, 300, 400, 400)
    c2.has_bottom_wall = False
    c2.draw(400, 400, 500, 500)

    win.wait_for_close()


main()