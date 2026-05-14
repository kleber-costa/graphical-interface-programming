import tkinter as tk
import random
import time

# constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
SPEED = 150
# colors
BG_COLOR = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
# directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()

        self.snake = [(5, 5)]
        self.food = self.generate_food()
        self.direction = RIGHT
        self.score = 0

        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        self.bind("<Left>", self.left)
        self.bind("<Right>", self.right)

        self.game_over = False
        self.update()


    def generate_food(self):
        while True:
            x = random.randint(0, WIDTH // GRID_SIZE - 1)
            y = random.randint(0, HEIGHT // GRID_SIZE - 1)
            food = (x, y)
            if food not in self.snake:
                return food
            

    def draw_snake(self):
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x * GRID_SIZE,
                y * GRID_SIZE,
                (x + 1) * GRID_SIZE,
                (y + 1) * GRID_SIZE,
                fill=SNAKE_COLOR
            )


    # Better positioning of food within the limits defined by the four walls
    def draw_food(self):
        pass


    def up(self, event):
        if self.direction != DOWN:
            self.direction = UP


    def down(self, event):
        if self.direction != UP:
            self.direction = DOWN


    def left(self, event):
        if self.direction != RIGHT:
            self.direction = LEFT


    def right(self, event):
        if self.direction != LEFT:
            self.direction = RIGHT
  

    # Check if the game is over according to the conditions (i) touching one of the walls, (ii) touching one's own body.
    def is_game_over(self):
        pass


    def update(self):
        if not self.game_over:
            x, y = self.snake[0]
            dx, dy = self.direction
            new_head = (x + dx, y + dy)
            self.snake.insert(0, new_head)

            if new_head == self.food:
                self.score += 1
                self.food = self.generate_food()
            else:
                self.snake.pop()
    
            self.is_game_over()
            self.canvas.delete("all")
            self.draw_snake()
            self.draw_food()

            self.canvas.create_text(
                10, 10, text=f"Score: {self.score}", fill="white", anchor="nw"
                )
            
            self.after(SPEED, self.update)
        else:
            self.canvas.create_text(
                WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 20)
            )
        
    
if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()