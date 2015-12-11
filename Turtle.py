from turtle import *
import random as r
import numpy as np

RADIUS = 50
RADIUSC = 150

# visual of the circle
c = Turtle()
c.penup()
c.setpos(c.pos()[0], c.pos()[1]-RADIUS)
c.pendown()
c.color('blue')
c.circle(RADIUS)
c.speed(speed = 10)

# bigger circle
p = Turtle()
p.penup()
p.setpos(c.pos()[0], c.pos()[1]-(2 * RADIUS))
p.pendown()
p.color('green')
p.circle(RADIUSC)
p.speed(speed = 10)

# particle
t = Turtle()
t.color('red')

xarray = []
yarray = []

def circle(theta):
    return RADIUS * np.cos(theta), RADIUS * np.sin(theta)

def circle_c(theta):
    return RADIUSC * np.cos(theta), RADIUSC * np.sin(theta)

for i in xrange(360):
    point = circle(i)
    xarray.append(point[0])
    yarray.append(point[1])

xarrayc = []
yarrayc = []

for i in np.linspace(0., 360., 2160):
    point = circle_c(i)
    xarrayc.append(point[0])
    yarrayc.append(point[1])

point_i = r.choice(range(0, len(xarray)))
point = (xarray[point_i], yarray[point_i])

def main_loop():
    # main loop
    count = 0
    t.penup()
    t.setpos(point[0], point[1])
    if point[0] < 0 and point[1] < 0:
        t.left(r.randint(180,271))
    if point[0] < 0 and point[1] > 0:
        t.left(r.randint(90,181))
    if point[0] > 0 and point[1] < 0:
        t.left(r.randint(270,361))
    if point[0] > 0 and point[1] > 0:
        t.left(r.randint(0,91))
    t.pendown()
    t.speed(speed=10)
    t.forward(5)
    last_time_in_radius = False
    while True:
        if count != 0 and (((abs(t.pos()[0]))**2 + (abs(t.pos()[1]))**2)**(.5)) <= RADIUS:
            print 'I\'m in the core'
            if t.heading() in range(0,91):
                t.right(90)
            if t.heading() in range(90,181):
                t.right(90)
            if t.heading() in range(180,271):
                t.right(90)
            if t.heading() in range(270,361):
                t.right(90)
            t.forward(20)
        else:
            t.forward(5)
            theta = r.randint(0, 180)
            if r.randint(0, 1) == 0:
                t.left(theta)
            else:
                t.right(theta)
        if (((abs(t.pos()[0]))**2 + (abs(t.pos()[1]))**2)**(.5)) < RADIUS:
            if last_time_in_radius:
                count = 0
                continue
        if (((abs(t.pos()[0]))**2 + (abs(t.pos()[1]))**2)**(.5)) < RADIUS:
            print str(count)
            #else:
            #    last_time_in_radius = True
        if (((abs(t.pos()[0]))**2 + (abs(t.pos()[1]))**2)**(.5)) >= RADIUSC:
                break
        count += 1

    # print out the number of moves the particle made
    return str(count)

results = []
for i in xrange(5):
    results.append(main_loop())

print results
print 'We did it! dododododadora!'
done()