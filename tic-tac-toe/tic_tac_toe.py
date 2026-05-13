import tkinter as tk
import tkinter.messagebox as messagebox


class Player:
    def __init__(self, label, color):
        self.label = label
        self.color = color


class TicTacToe:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Tic Tac Toe")
        self.player1 = Player("X", "blue")
        self.player2 = Player("O", "red")
        self.current_player = self.player1
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(
                    self.parent,
                    text="",
                    width=10,
                    height=5,
                    command=lambda row=row, col=col: self.make_move(row, col)
                )
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)


    def make_move(self, row, col):
        button = self.buttons[row][col]

        if button["text"] == "":
            button["text"] = self.current_player.label
            button["fg"] = self.current_player.color

        if self.check_winner():
            messagebox.showinfo("Fim de jogo", f"O jogador {self.current_player.label} venceu!")
            self.start_game()
        elif self.check_tie():
            messagebox.showinfo("Fim de jogo", "Empate!")
            self.start_game()
        else:
            self.switch_player()


    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def check_winner(self):
        # verificar se há ganhador
        for i in range(3):
            # Verifica vitória nas linhas (horizontal)
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
        
        for i in range(3):
            # verifica vitória nas linhas vertical
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        
        # verifica vitória na diagonal principal
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True        
        # verifica vitória na diagonal secundária
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        
        return False


    def check_tie(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        
        return True


    def start_game(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
                
        self.current_player = self.player1


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()