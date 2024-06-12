import random

class MinesweeperGame:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.grid = self.generate_grid()
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False

    def generate_grid(self):
        grid = [["-" for _ in range(self.cols)] for _ in range(self.rows)]
        mines_placed = 0
        while mines_placed < self.num_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if grid[row][col] == "-":
                grid[row][col] = "#"
                mines_placed += 1
        return grid

    def count_adjacent_mines(self, row, col):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == "#":
                count += 1
        return str(count)
    
    def reveal_all_mines(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "#":
                    self.revealed[i][j] = True

    def reveal_cell(self, row, col):
        if self.grid[row][col] == "#":
            self.game_over = True
            self.reveal_all_mines()
            return False
        else:
            self._flood_fill(row, col)
            return True

    def _flood_fill(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols) or self.revealed[row][col]:
            return
        self.revealed[row][col] = True
        if self.grid[row][col] == "-":
            count = self.count_adjacent_mines(row, col)
            self.grid[row][col] = count
            if count == "0":
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr != 0 or dc != 0:
                            self._flood_fill(row + dr, col + dc)

    def is_victory(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.revealed[i][j] and self.grid[i][j] != "#":
                    return False
        return True
