import turtle
color=input("color = ")
t=int(input("leg long = "))
s=turtle.Screen()
s.title("lakposht")
lakposht=turtle.Turtle()
lakposht.color(color)
for x in range (4) :
    lakposht.forward(t)
    lakposht.left(90)
s.mainloop()