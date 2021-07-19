from snake import Snake
import pygame, random

pygame.init()
dis=pygame.display.set_mode((800,600))
dis.fill((0,0,255))

#pygame.display.set_caption('Snake game by Andrew')
game_over=False

snake = Snake((255,255,255), dis, (30,30))

clock = pygame.time.Clock()


track = [(800//2, 600//2)]
dir = (1, 0)
length = 1
food = snake.random_pos(track)
def close(pos1, pos2):
    if(pos1[0] > pos2[0] and pos1[1] > pos2[1]):
        if(pos1[0] - pos2[0] < 50 and pos1[1] - pos2[1] < 50):
            return True
    if(pos1[0] < pos2[0] and pos1[1] > pos2[1]):
        if(pos2[0] - pos1[0] < 50 and pos1[1] - pos2[1] < 50):
            return True
    if(pos1[0] > pos2[0] and pos2[1] > pos1[1]):
        if(pos1[0] - pos2[0] < 50 and pos2[1] - pos1[1] < 50):
            return True
    if(pos1[0] < pos2[0] and pos1[1] < pos2[1]):
        if(pos2[0] - pos1[0] < 50 and pos2[1] - pos1[1] < 50):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dir = (-1, 0)
            if event.key == pygame.K_RIGHT:
                dir = (1, 0)
            if event.key == pygame.K_DOWN:
                dir = (0, 1)
            if event.key == pygame.K_UP:
                dir = (0, -1)
    track.insert(0, track[0][:])    
    track[0] = (track[0][0] + dir[0]) % 800, (track[0][1] + dir[1]) % 600

    body = snake.create_body(track, length, 20)



    if(snake.check_tail_collision(body)):
        game_over = True
    
    if snake.hit(body[0], food, 20):
        food = snake.random_pos(body)
        length += 1 
    dis.fill((0,0,255))
    k=20
    while k > 5:
        pygame.draw.rect(dis, (0,0,0) ,pygame.Rect(food[0], food[1], k,k),2,3)
        k -= 1



    snake.paint(body,dis)

    
    pygame.display.update()
    pygame.display.flip()

    clock.tick(120)
pygame.quit()
quit()