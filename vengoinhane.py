#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

# Khởi tạo màn hình đồ họa
screen = turtle.Screen()
screen.bgcolor('pink')

# Vẽ ngôi nhà
house = turtle.Turtle()
house.color('white')
house.fillcolor('white')
house.penup()
house.goto(0, -150)
house.pendown()
house.begin_fill()
for _ in range(4):
    house.forward(200)
    house.left(90)

house.end_fill()


roof = turtle.Turtle()
roof.color('red')
roof.fillcolor('red')
roof.penup()
roof.goto(200, 50)
roof.pendown()
roof.begin_fill()
roof.goto(100, 150)
roof.goto(0, 50)
roof.end_fill()

# Vẽ cửa sổ
window = turtle.Turtle()
window.color('lightblue')
window.fillcolor('lightblue')
window.penup()
window.goto(25, -50)
window.pendown()
window.begin_fill()
for _ in range(4):
    window.forward(60)
    window.left(90)
window.end_fill()

window = turtle.Turtle()
window.color('lightblue')
window.fillcolor('lightblue')
window.penup()
window.goto(125, -50)
window.pendown()
window.begin_fill()
for _ in range(4):
    window.forward(60)
    window.left(90)
window.end_fill()
# Vẽ mặt trời
sun = turtle.Turtle()
sun.color('yellow')
sun.fillcolor('yellow')
sun.penup()
sun.goto(200, 200)
sun.pendown()
sun.begin_fill()
sun.circle(100)
sun.end_fill()

# Vẽ cây
tree = turtle.Turtle()
tree.color('brown')
tree.fillcolor('brown')
tree.penup()
tree.goto(-300, -200)
tree.pendown()
tree.begin_fill()
tree.forward(80)
tree.left(90)
tree.forward(200)
tree.left(90)
tree.forward(80)
tree.left(90)
tree.forward(200)
tree.left(90)
tree.end_fill()

tree.penup()
tree.goto(-250, 0)
tree.pendown()
tree.color('green')
tree.fillcolor('green')
tree.begin_fill()
tree.circle(100)
tree.end_fill()

# Ẩn con rùa
house.hideturtle()
window.hideturtle()
sun.hideturtle()
tree.hideturtle()

# Hoàn thành vẽ
turtle.done()


# In[ ]:




