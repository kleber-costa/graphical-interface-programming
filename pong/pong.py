import tkinter as tk

# Constants
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
BALL_SIZE = 20
BALL_SPEED = 4
PADDLE_SPEED = 15


class PongGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pong")

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Make left paddle
        self.left_paddle = self.canvas.create_rectangle(
            20, HEIGHT // 2 - PADDLE_HEIGHT //2,
            20 + PADDLE_WIDTH, HEIGHT // 2 + PADDLE_HEIGHT // 2,
            fill="white"
        )

        # Make right paddle
        self.right_paddle = self.canvas.create_rectangle(
            WIDTH - 20 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT //2,
            WIDTH - 20, HEIGHT // 2 + PADDLE_HEIGHT // 2,
            fill="white"
        )

        # Make ball
        self.ball = self.canvas.create_oval(
            WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2,
            WIDTH // 2 + BALL_SIZE // 2, HEIGHT // 2 + BALL_SIZE // 2,
            fill="white"
        )

        self.ball_dx = BALL_SPEED
        self.ball_dy = BALL_SPEED

        self.bind("<w>", self.move_paddle)
        self.bind("<s>", self.move_paddle)
        self.bind("<Up>", self.move_paddle)     
        self.bind("<Down>", self.move_paddle)

        self.update_game()

    # Move the right and left paddle according to the pressed keyboard button
    def move_paddle(self, event):
        if event.keysym in ["w", "s"]:
            paddle = self.left_paddle
            direction = -1 if event.keysym == "w" else 1
        else:
            paddle = self.right_paddle
            direction = -1 if event.keysym == "Up" else 1 

        x1, y1, x2, y2 = self.canvas.coords(paddle)

        if 0 <= y1 + direction * PADDLE_SPEED and y2 + direction * PADDLE_SPEED <= HEIGHT:
            self.canvas.move(paddle, 0, direction * PADDLE_SPEED)


    def update_game(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)

        x1, y1, x2, y2 = self.canvas.coords(self.ball)

        if y1 <= 0 or y2 >= HEIGHT:
            self.ball_dy *= -1

        left_x1, left_y1, left_x2, left_y2 = self.canvas.coords(self.left_paddle)
        right_x1, right_y1, right_x2, right_y2 = self.canvas.coords(self.right_paddle)

        if (x1 <= left_x2 and left_y1 <= y1 <= left_y2) or (x2 >= right_x1 and right_y1 <= y1 <= right_y2):
            self.ball_dx *= -1

        if x1 <= 0 or x2 >= WIDTH:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over!"
                                    ,fill="white", font=("Arial", 20))
            return
    
        self.after(30, self.update_game)
    

if __name__ == "__main__":
    game = PongGame()
    game.mainloop()