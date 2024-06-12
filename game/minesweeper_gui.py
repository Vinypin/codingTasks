import tkinter as tk
from tkinter import messagebox
from minesweeper import MinesweeperGame

class MinesweeperGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Minesweeper game")
        self.level_window()

    def level_window(self):
        self.level_frame = tk.Frame(self.window)
        self.level_frame.pack(pady=20)

        label = tk.Label(self.level_frame, text="Select dificult level:")
        label.pack(pady=5)

        easy_button = tk.Button(self.level_frame, text="Easy", command=lambda: self.start_game(6, 6, 4))
        easy_button.pack(pady=5)

        medium_button = tk.Button(self.level_frame, text="Medium", command=lambda: self.start_game(8, 8, 8))
        medium_button.pack(pady=5)

        hard_button = tk.Button(self.level_frame, text="Hard", command=lambda: self.start_game(10, 10, 12))
        hard_button.pack(pady=5)

    def start_game(self, rows, cols, num_mines):
        self.level_frame.destroy()
        self.game = MinesweeperGame(rows, cols, num_mines)
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self._create_widgets()

    def _create_widgets(self):
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                button = tk.Button(self.window, text='', width=3, height=1, command=lambda r=r, c=c: self._on_button_click(r, c))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

    def _on_button_click(self, row, col):
        if not self.game.reveal_cell(row, col):
            self._update_buttons()
            messagebox.showerror("Game Over", "You hit a mine!")
            self.window.quit()
        else:
            self._update_buttons()
            if self.game.is_victory():
                messagebox.showinfo("Congratulations! You won!!")
                self.window.quit()

    def _update_buttons(self):
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                if self.game.revealed[r][c]:
                    if self.game.grid[r][c] == "#":
                        self.buttons[r][c].config(text='*', state='disabled', relief=tk.SUNKEN)
                    else:
                        self.buttons[r][c].config(text=self.game.grid[r][c], state='disabled', relief=tk.SUNKEN)

    def run(self):
        self.window.mainloop()
