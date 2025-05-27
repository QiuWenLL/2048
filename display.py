import pygame
import sys
from game import Game2048

# 初始化Pygame
pygame.init()

# 颜色定义
BACKGROUND_COLOR = (187, 173, 160)
GRID_COLOR = (205, 193, 180)
EMPTY_CELL_COLOR = (205, 193, 180)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}
TEXT_COLOR = {
    0: (205, 193, 180),
    2: (119, 110, 101),
    4: (119, 110, 101),
    8: (249, 246, 242),
    16: (249, 246, 242),
    32: (249, 246, 242),
    64: (249, 246, 242),
    128: (249, 246, 242),
    256: (249, 246, 242),
    512: (249, 246, 242),
    1024: (249, 246, 242),
    2048: (249, 246, 242)
}

# 游戏参数
CELL_SIZE = 100
CELL_PADDING = 15
GRID_SIZE = 4
WINDOW_WIDTH = CELL_SIZE * GRID_SIZE + CELL_PADDING * (GRID_SIZE + 1)
WINDOW_HEIGHT = WINDOW_WIDTH + 50  # 额外空间用于显示分数

class GameDisplay:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('2048')
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 24)
    
    def draw_board(self):
        """绘制游戏板"""
        self.screen.fill(BACKGROUND_COLOR)
        
        # 绘制网格
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                pygame.draw.rect(
                    self.screen,
                    EMPTY_CELL_COLOR,
                    pygame.Rect(
                        CELL_PADDING + j * (CELL_SIZE + CELL_PADDING),
                        CELL_PADDING + i * (CELL_SIZE + CELL_PADDING),
                        CELL_SIZE,
                        CELL_SIZE
                    ),
                    border_radius=5
                )
        
        # 绘制数字方块
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.game.board[i][j]
                if value != 0:
                    color = TILE_COLORS.get(value, (60, 58, 50))
                    pygame.draw.rect(
                        self.screen,
                        color,
                        pygame.Rect(
                            CELL_PADDING + j * (CELL_SIZE + CELL_PADDING),
                            CELL_PADDING + i * (CELL_SIZE + CELL_PADDING),
                            CELL_SIZE,
                            CELL_SIZE
                        ),
                        border_radius=5
                    )
                    
                    # 绘制数字
                    text_color = TEXT_COLOR.get(value, (249, 246, 242))
                    text = self.font.render(str(value), True, text_color)
                    text_rect = text.get_rect(
                        center=(
                            CELL_PADDING + j * (CELL_SIZE + CELL_PADDING) + CELL_SIZE // 2,
                            CELL_PADDING + i * (CELL_SIZE + CELL_PADDING) + CELL_SIZE // 2
                        )
                    )
                    self.screen.blit(text, text_rect)
        
        # 绘制分数
        score_text = self.small_font.render(f"Score: {self.game.score}", True, (119, 110, 101))
        self.screen.blit(score_text, (CELL_PADDING, WINDOW_HEIGHT - 40))
    
    def show_message(self, message):
        """显示游戏结束或胜利消息"""
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((238, 228, 218, 180))
        self.screen.blit(overlay, (0, 0))
        
        text = self.font.render(message, True, (119, 110, 101))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        
        restart_text = self.small_font.render("Press R to restart", True, (119, 110, 101))
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()