import turtle

t = turtle.Screen()

don = turtle.Turtle()
don.color("blue")

def draw_line_to_circle(aTurtle, angle = 170, dist = 200):

    if dist < 2:
        return
        
    aTurtle.forward(dist)
    aTurtle.left(angle)
    
    return draw_line_to_circle(aTurtle, angle*.95, dist*.95)
    
draw_line_to_circle(don)

t.exitonclick()