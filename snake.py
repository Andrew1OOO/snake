import math
import random
import pygame

class Snake():
    def __init__(self, color, surface):
        self.color = color
        self.surface = surface
        self.body = []
        self.track = []


    def paint(self, body, screen):
        for i, pos in enumerate(body):
            k=20
            while k > 5:
                pygame.draw.rect(screen, (0,0,0) ,pygame.Rect(pos[0], pos[1], k,k),2,3)
                k -= 1

    def create_body(self, track, no_pearls, distance):
        body = [(track[0])]
        track_i = 1
        for i in range(1, no_pearls):
            while track_i < len(track):
                pos = track[track_i]
                track_i += 1
                dx, dy = body[-1][0]-pos[0], body[-1][1]-pos[1]
                if math.sqrt(dx*dx + dy*dy) >= distance:
                    body.append(pos)
                    break
        while len(body) < no_pearls:
            body.append(track[-1])
        del track[track_i:]
        return body


    def hit(self, pos_a, pos_b, distance):
        dx, dy = pos_a[0]-pos_b[0], pos_a[1]-pos_b[1]
        return math.sqrt(dx*dx + dy*dy) < distance
    
    def check_tail_collision(self, body):
        #head = body[-1]
        #has_eaten_tail = False

        #for i in range(len(body) - 1):
        #    segment = body[i]
        #    if head[0] == segment[0] and head[1] == segment[1]:
        #        has_eaten_tail = True
        #print(
        return body[-1] in set(body[0:-1])
    
    def random_pos(self, body):
        return (random.randint(0,800), random.randint(0,600))