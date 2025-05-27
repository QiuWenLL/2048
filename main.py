import pygame
import sys
from game import Game2048
from display import GameDisplay

def main():
    game = Game2048()
    display = GameDisplay(game)
    
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
                elif event.key == pygame.K_r:
                    game = Game2048()
                    display = GameDisplay(game)
                    continue
                elif event.key == pygame.K_q:
                    running = False
                
                if moved:
                    game.add_random_tile()
        
        display.draw_board()
        
        if game.has_won():
            print("You Win!")
        elif game.is_game_over():
            print("Game Over!")
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()