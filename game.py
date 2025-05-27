import random

class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()
    
    def add_random_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2 if random.random() < 0.9 else 4
    
    def move_left(self):
        moved = False
        for row in self.board:
            new_row = [num for num in row if num != 0]
            for i in range(len(new_row)-1):
                if new_row[i] == new_row[i+1]:
                    new_row[i] *= 2
                    new_row[i+1] = 0
                    self.score += new_row[i]
            new_row = [num for num in new_row if num != 0]
            new_row += [0] * (4 - len(new_row))
            if row != new_row:
                moved = True
            row[:] = new_row
        return moved
    
    def move_right(self):
        moved = False
        for row in self.board:
            new_row = [num for num in row if num != 0]
            for i in range(len(new_row)-1, 0, -1):
                if new_row[i] == new_row[i-1]:
                    new_row[i] *= 2
                    new_row[i-1] = 0
                    self.score += new_row[i]
            new_row = [num for num in new_row if num != 0]
            new_row = [0] * (4 - len(new_row)) + new_row
            if row != new_row:
                moved = True
            row[:] = new_row
        return moved
    
    def move_up(self):
        moved = False
        for j in range(4):
            column = [self.board[i][j] for i in range(4)]
            new_column = [num for num in column if num != 0]
            for i in range(len(new_column)-1):
                if new_column[i] == new_column[i+1]:
                    new_column[i] *= 2
                    new_column[i+1] = 0
                    self.score += new_column[i]
            new_column = [num for num in new_column if num != 0]
            new_column += [0] * (4 - len(new_column))
            if column != new_column:
                moved = True
            for i in range(4):
                self.board[i][j] = new_column[i]
        return moved
    
    def move_down(self):
        moved = False
        for j in range(4):
            column = [self.board[i][j] for i in range(4)]
            new_column = [num for num in column if num != 0]
            for i in range(len(new_column)-1, 0, -1):
                if new_column[i] == new_column[i-1]:
                    new_column[i] *= 2
                    new_column[i-1] = 0
                    self.score += new_column[i]
            new_column = [num for num in new_column if num != 0]
            new_column = [0] * (4 - len(new_column)) + new_column
            if column != new_column:
                moved = True
            for i in range(4):
                self.board[i][j] = new_column[i]
        return moved
    
    def is_game_over(self):
        if any(0 in row for row in self.board):
            return False
        
        for i in range(4):
            for j in range(4):
                if j < 3 and self.board[i][j] == self.board[i][j+1]:
                    return False
                if i < 3 and self.board[i][j] == self.board[i+1][j]:
                    return False
        
        return True
    
    def has_won(self):
        return any(num >= 2048 for row in self.board for num in row)