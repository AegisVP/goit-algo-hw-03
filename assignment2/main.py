import argparse

from turtle import Turtle, Screen


def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order-1, size/3)
            turtle.left(angle)


def draw_koch_snowflake(order, size=400):
    window = Screen()
    window.bgcolor('white')

    turtle = Turtle()
    turtle.speed(0)

    # position start
    turtle.penup()
    turtle.goto(-size/2, size/2/3**0.5)
    turtle.pendown()

    for _ in range(3):
        koch_snowflake(turtle, order, size)
        turtle.right(120)

    window.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o-', '--order', type=int, default=3)
    args = parser.parse_args()
    draw_koch_snowflake(args.order)
