import pygame

# 颜色定义
BACKGROUND_COLOR = (187, 173, 160)
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

class GameDisplay:
    def __init__(self, game):
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((450, 500))
        pygame.display.set_caption('2048')
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
    
    def draw_board(self):
        self.screen.fill(BACKGROUND_COLOR)
        
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(
                    self.screen,
                    EMPTY_CELL_COLOR,
                    pygame.Rect(15 + j * 105, 15 + i * 105, 100, 100),
                    border_radius=5
                )
        
        for i in range(4):
            for j in range(4):
                value = self.game.board[i][j]
                if value != 0:
                    pygame.draw.rect(
                        self.screen,
                        TILE_COLORS.get(value, (60, 58, 50)),
                        pygame.Rect(15 + j * 105, 15 + i * 105, 100, 100),
                        border_radius=5
                    )
                    
                    text = self.font.render(str(value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(65 + j * 105, 65 + i * 105))
                    self.screen.blit(text, text_rect)
        
        pygame.display.flip()