import turtle

axiom = "0"
tempAx=""

translate={"1":"11" ,"0":"1[0]0"}
for i in range(3):
    for ch in axiom:
        tempAx=tempAx+translate[ch]
axiom=axiom+tempAx
tempAx= ""
print(axiom)

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.pendown()
turtle.pensize(2)

for ch in axiom:
    if (ch=="1"):
        turtle.forward(15)
    elif (ch=="0"):
        turtle.forward(15)
    elif (ch=="["):
        turtle.left(45)
    elif (ch=="]"):
        turtle.back(15)
        turtle.right(90)
turtle.update()
turtle.done()