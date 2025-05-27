import random
import json
from datetime import datetime

class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()
    
    def add_random_tile(self):
        """在随机空位置添加一个2或4的方块"""
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2 if random.random() < 0.9 else 4
    
    def move_left(self):
        """向左移动所有方块并合并"""
        moved = False
        for row in self.board:
            # 移除0并合并相同数字
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
        """向右移动所有方块并合并"""
        moved = False
        for row in self.board:
            # 移除0并合并相同数字
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
        """向上移动所有方块并合并"""
        moved = False
        for j in range(4):
            column = [self.board[i][j] for i in range(4)]
            # 移除0并合并相同数字
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
        """向下移动所有方块并合并"""
        moved = False
        for j in range(4):
            column = [self.board[i][j] for i in range(4)]
            # 移除0并合并相同数字
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
        """检查游戏是否结束"""
        # 检查是否有空格
        if any(0 in row for row in self.board):
            return False
        
        # 检查是否有可以合并的相邻方块
        for i in range(4):
            for j in range(4):
                if j < 3 and self.board[i][j] == self.board[i][j+1]:
                    return False
                if i < 3 and self.board[i][j] == self.board[i+1][j]:
                    return False
        
        return True
    
    def has_won(self):
        """检查是否达到2048获胜条件"""
        return any(num >= 2048 for row in self.board for num in row)
        
    def save_score(self):
        """保存当前分数到scores.json文件"""
        print(f"尝试保存分数: {self.score}")  # 调试输出
        
        if self.score <= 0:  # 不保存0分
            print("分数为0，不保存")
            return
            
        try:
            with open('scores.json', 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"scores": []}
            
        score_record = {
            "score": self.score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "board": self.board
        }
        data["scores"].append(score_record)
        
        try:
            with open('scores.json', 'w') as f:
                json.dump(data, f, indent=2)
            print(f"成功保存分数: {score_record}")  # 调试输出
        except Exception as e:
            print(f"保存分数出错: {e}")  # 调试输出