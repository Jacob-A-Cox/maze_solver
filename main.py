from graphics import Window, Point, Line


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

    win.wait_for_close()


main()