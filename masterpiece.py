from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

oval1 = Oval()
oval1.set_width(300)
oval1.set_height(500)
oval1.set_color('pink')
oval1.draw()

rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color('yellow')
rect2.set_x(100)
rect2.set_y(100)
rect2.draw()

tri1 = Triangle(500,500,100,500,500,100)
tri1.set_color('red')
tri1.draw()

paper.display()