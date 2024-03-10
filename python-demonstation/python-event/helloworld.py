import turtle

def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def generate_inner_squares(size, num_inner_squares):
    if num_inner_squares <= 0 or num_inner_squares > size // 2:
        print("Invalid number of inner squares.")
        return None

    outer_square = []

    for i in range(num_inner_squares):
        inner_size = size - 2 * i
        inner_square = []

        for _ in range(inner_size):
            inner_square.append('X' * inner_size)

        outer_square.extend(inner_square)

    return tuple(outer_square)

if __name__ == "__main__":
    turtle.speed(1)

    outer_size = int(input("Enter the size of the outer square: "))
    inner_squares = int(input("Enter the number of inner squares: "))

    turtle.penup()
    turtle.goto(-outer_size / 2, outer_size / 2)
    turtle.pendown()

    for square in generate_inner_squares(outer_size, inner_squares):
        for row in square:
            for cell in row:
                if cell == 'X':
                    turtle.begin_fill()
                    draw_square(outer_size // (2 * inner_squares))
                    turtle.end_fill()
                turtle.forward(outer_size // inner_squares)
            turtle.backward(outer_size)
            turtle.right(90)
            turtle.forward(outer_size // inner_squares)
            turtle.left(90)

    turtle.done()
