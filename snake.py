import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
h = turtle.Turtle()
h.speed(0)
h.shape('square')
h.color('white')
h.penup()
h.goto(0,0)
h.direction = 'stop'

#snake food
f = turtle.Turtle()
f.speed(0)
f.shape('square')
f.color('red')
f.penup()
f.goto(0,100)

segments = []

#scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape('square')
sc.color('white')
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write('score: 0 High score: 0',align='center',font=('ds-digital',24,'normal'))

def go_up():
    if h.direction != "down":
        h.direction = "up"
def go_down():
    if h.direction != "up":
        h.direction = "down"
def go_left():
    if h.direction != "right":
        h.direction = "left"
def go_right():
    if h.direction != "left":
        h.direction = "right"
def move():
    if h.direction == "up":
        y = h.ycor()
        h.sety(y+20)
    if h.direction == "down":
        y = h.ycor()
        h.sety(y-20)
    if h.direction == "left":
        x = h.xcor()
        h.setx(x-20)
    if h.direction == "right":
        x = h.xcor()
        h.setx(x+20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()

    #check collision with border area
    if h.xcor()>290 or h.xcor()<-290 or h.ycor()>290 or h.ycor()<-290:
        time.sleep(1)
        h.goto(0,0)
        h.direction = "stop"

        #hide the segments of body
        for segment in segments:
            segment.goto(1000,1000) #out of range
        #clear the segments
        segments.clear()

        #reset score
        score = 0

        #reset delay
        delay = 0.1

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

    #check collision with food
    if h.distance(f) <20:
        # move the food to random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        f.goto(x,y)

        #add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 

    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = h.xcor()
        y = h.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(h)<20:
            time.sleep(1)
            h.goto(0,0)
            h.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            #update the score     
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
wn.mainloop()   