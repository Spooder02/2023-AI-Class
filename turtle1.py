import turtle as t

t1 = t.Turtle()
t1.shape("turtle")
t1.penup()
t1.goto(-300, 0)
t1.pensize(10)

t1.pendown()
t1.pencolor('blue')
t1.circle(90)
t1.penup()

t1.forward(200)
t1.pendown()
t1.pencolor('black')
t1.circle(90)
t1.penup()

t1.forward(200)
t1.pendown()
t1.pencolor('red')
t1.circle(90)
t1.penup()

t1.backward(400)
t1.right(90)
t1.forward(30)
t1.pendown()
t1.pencolor('yellow')
t1.circle(90)

t1.penup()
t1.goto(-75, 0)
t1.forward(30)
t1.pendown()
t1.pencolor('green')
t1.circle(90)