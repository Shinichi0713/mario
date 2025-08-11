import tkinter as tk
import random
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("神経衰弱ゲーム")
        self.buttons = []
        self.first = None
        self.second = None
        self.matches = 0
        self.grid_size = 4
        self.total_pairs = (self.grid_size * self.grid_size) // 2
        self.create_board()

    def create_board(self):
        self.board = [i for i in range(1, self.total_pairs + 1)] * 2
        random.shuffle(self.board)

        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                btn = tk.Button(self.root, text='', width=10, height=5, font=("Helvetica", 20), command=lambda i=i, j=j: self.on_click(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def on_click(self, i, j):
        if self.first and self.second:
            return

        btn = self.buttons[i][j]
        btn.config(text=str(self.board[i * self.grid_size + j]), state='disabled')

        if not self.first:
            self.first = (i, j)
        elif not self.second:
            self.second = (i, j)
            self.root.after(1000, self.check_match)

    def check_match(self):
        if self.board[self.first[0] * self.grid_size + self.first[1]] == self.board[self.second[0] * self.grid_size + self.second[1]]:
            self.matches += 1
            if self.matches == self.total_pairs:
                messagebox.showinfo("おめでとうございます！", "全てのペアを見つけました！")
        else:
            self.buttons[self.first[0]][self.first[1]].config(text='', state='normal')
            self.buttons[self.second[0]][self.second[1]].config(text='', state='normal')

        self.first = None
        self.second = None


if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()