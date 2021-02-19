import turtle

axiom = "0"
tempAx=""

n=len(axiom)
for i in range(1):
    for i in range(n):
        if (axiom[i]=="1"):
            tempAx=tempAx+"11"
        elif (axiom[i]=="0"):
            tempAx=tempAx+"1[0]0"
        else:
            tempAx = tempAx + ""
axiom=axiom+tempAx
tempAx= ""
print(axiom)

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.pendown()
turtle.pensize(2)

n=len(axiom)
for i in range(n):
    if (axiom[i]=="1"):
        turtle.forward(15)
    elif (axiom[i]=="0"):
        turtle.forward(15)
    elif (axiom[i]=="["):
        turtle.left(45)
    elif (axiom[i]=="]"):
        turtle.back(15)
        turtle.right(90)
turtle.update()
turtle.done()