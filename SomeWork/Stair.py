import turtle

win = turtle.Screen()
st = turtle.Turtle()

#st.speed(1)
st.pensize(3)

st.penup()
st.goto(-300,300)
st.pendown()

for i in range(10):
    print(i)
    st.write(i, font=("Arial",30,"bold"))
    st.penup()
    st.forward(50)
 #   st.right(90)
 #   st.forward(50)
 #   st.left(90)
    st.pendown()


st.write("Now I'm done!", font=("Arial",30,"bold"))

print("This is print")
