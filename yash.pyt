import tkinter as tk
import random

# Game settings
WIDTH = 400
HEIGHT = 400
SPACE = 20
SPEED = 100

# Colors
BG_COLOR = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

# Initial values
direction = "right"
score = 0

# Create window
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

# Score label
label = tk.Label(window, text="Score: 0", font=("Arial", 14))
label.pack()

# Canvas
canvas = tk.Canvas(window, bg=BG_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

# Snake data
snake = [(100, 100), (80, 100), (60, 100)]

# Draw snake
def draw_snake():
    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(x, y, x+SPACE, y+SPACE, fill=SNAKE_COLOR, tag="snake")

# Food
def create_food():
    x = random.randint(0, (WIDTH // SPACE) - 1) * SPACE
    y = random.randint(0, (HEIGHT // SPACE) - 1) * SPACE
    return (x, y)

food = create_food()

def draw_food():
    canvas.delete("food")
    x, y = food
    canvas.create_oval(x, y, x+SPACE, y+SPACE, fill=FOOD_COLOR, tag="food")

# Movement
def move():
    global food, score

    head_x, head_y = snake[0]

    if direction == "up":
        head_y -= SPACE
    elif direction == "down":
        head_y += SPACE
    elif direction == "left":
        head_x -= SPACE
    elif direction == "right":
        head_x += SPACE

    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    # Check food
    if new_head == food:
        score += 1
        label.config(text=f"Score: {score}")
        food = create_food()
    else:
        snake.pop()

    # Check collision
    if (head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake[1:]):
        game_over()
        return

    draw_snake()
    draw_food()
    window.after(SPEED, move)

# Controls
def change_direction(new_dir):
    global direction
    if new_dir == "up" and direction != "down":
        direction = new_dir
    elif new_dir == "down" and direction != "up":
        direction = new_dir
    elif new_dir == "left" and direction != "right":
        direction = new_dir
    elif new_dir == "right" and direction != "left":
        direction = new_dir

window.bind("<Up>", lambda e: change_direction("up"))
window.bind("<Down>", lambda e: change_direction("down"))
window.bind("<Left>", lambda e: change_direction("left"))
window.bind("<Right>", lambda e: change_direction("right"))

# Game over
def game_over():
    canvas.delete("all")
    canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", fill="white", font=("Arial", 24))

# Start game
draw_snake()
draw_food()
move()

window.mainloop()