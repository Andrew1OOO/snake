from snake import Snake
from board import Board
import pygame, random

pygame.init()
dis=pygame.display.set_mode((600,600))
dis.fill((145, 178, 199))
color1 = (94, 169, 190);

game_over=False
clock = pygame.time.Clock()
board = Board((30,30), dis, (600,600), color1)


board.create_grid()
board.place_food()
board.create_snake()
board.paint_pieces()

length = 1
dir1 = (0,0)

while not game_over:
    game_over = board.check_collison()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir1 = (-1, 0)
            if event.key == pygame.K_RIGHT:
                dir1 = (1, 0)
            if event.key == pygame.K_DOWN:
                dir1 = (0, 1)
            if event.key == pygame.K_UP:
                dir1 = (0, -1)
            if(event.key == pygame.K_s):
                board.print_board(board.board)
                print('\n')
                #board.find_shortest_path()

    board.ai_move()
    board.check_snakeate(dir1)
    

    dis.fill((145, 178, 199))
    board.paint_pieces()
    board.create_grid()
    

    pygame.display.update()
    pygame.display.flip()

    clock.tick(30)
pygame.quit()
quit()