import turtle as t
t.setup(650,650)
t.pensize(2)
t.bgcolor("black")
colors=["red","yellow","blue","green","orange","purple"]
for i in range(300):
    t.pencolor(colors[i%6])
    t.fd(i)
    t.right(59)
t.done()
