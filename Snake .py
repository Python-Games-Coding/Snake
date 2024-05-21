import random
import turtle as t
import time

t.bgcolor('yellow')
caterpiller = t.Turtle()
caterpiller.shape('square')
caterpiller.color('red')
caterpiller.speed(0)
caterpiller.penup()
caterpiller.ht()

leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.ht()
leaf.speed(0)

game_started = False
tt = t.Turtle()
tt.write('按下空格开始游戏', align='center', font=('Arial', 16, 'bold'))
tt.ht()

st = t.Turtle()
st.ht()
st.speed(0)

def outside_window():
    l_wall = -t.window_width / 2
    r_wall = t.window_width / 2
    t_wall = t.window_height / 2
    b_wall = -t.window_height / 2
    (x, y) = caterpiller.pos()
    outside = x < l_wall or x > r_wall or y < b_wall or y > t_wall
    return outside

def game_over():
    caterpiller.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.ht()
    t.write('GAMEOVER!', align='center', font=('Arial', 30, 'normal'))

def display_score(current_score):
    st.clear()
    st.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    st.setpos(x, y)
    st.write('Score: ' + str(current_score), align='right', font=('Arial', 20, 'bold'))

def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    tt.clear()
    caterpiller_speed = 1
    caterpiller_length = 3
    caterpiller.shapesize(1, caterpiller_length, 1)
    caterpiller.st()
    display_score(score)
    place_leaf()
    while 1:
        caterpiller.forward(caterpiller_speed)
        if caterpiller.distance(leaf) < 50:
            place_leaf()
            caterpiller_length = caterpiller_length + 2
            caterpiller.shapesize(1, caterpiller_length, 1)
            score = score + 10
            display_score(score)
        if outside_window:
            pass

def move_up():
    if caterpiller.heading() == 0 or caterpiller.heading() == 180:
        caterpiller.setheading(90)

def move_down():
    if caterpiller.heading() == 0 or caterpiller.heading() == 180:
        caterpiller.setheading(270)

def move_left():
    if caterpiller.heading() == 90 or caterpiller.heading() == 270:
        caterpiller.setheading(180)

def move_right():
    if caterpiller.heading() == 90 or caterpiller.heading() == 270:
        caterpiller.setheading(0)

t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down') 
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()