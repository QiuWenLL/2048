import pygame
import sys
from game import Game2048
from display import GameDisplay

def main():
    # 初始化游戏和显示
    game = Game2048()
    display = GameDisplay(game)
    
    # 游戏主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                moved = False
                if event.key == pygame.K_LEFT:
                    moved = game.move_left()
                elif event.key == pygame.K_RIGHT:
                    moved = game.move_right()
                elif event.key == pygame.K_UP:
                    moved = game.move_up()
                elif event.key == pygame.K_DOWN:
                    moved = game.move_down()
                elif event.key == pygame.K_r:  # 重新开始
                    game = Game2048()
                    display = GameDisplay(game)
                    continue
                elif event.key == pygame.K_q:  # 退出
                    running = False
                
                # 如果移动有效，添加新方块
                if moved:
                    game.add_random_tile()
        
        # 绘制游戏板
        display.draw_board()
        
        # 检查游戏状态
        if game.has_won():
            display.show_message("You Win!")
            game.save_score()  # 保存胜利时的分数
        elif game.is_game_over():
            display.show_message("Game Over!")
            game.save_score()  # 保存游戏结束时的分数
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()