#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []
trtl.speed = 0

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "turtle", "arrow", "classic", "triangle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "pink", "magenta", "turquoise", "rosy brown", "olive", "light blue", "cornflower blue", "lavender"]
# create a list of turtles

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  t.color(turtle_colors.pop())
  my_turtles.append(t)

#  
startx = 0
starty = 0
startPos = 90
forwardlength = 50

#
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.setheading(startPos)
  t.right(45)     
  t.forward(forwardlength)

#	
  startx = t.xcor()
  starty = t.ycor()
  startPos = t.heading()
  forwardlength += 5
  

wn = trtl.Screen()
wn.mainloop()
