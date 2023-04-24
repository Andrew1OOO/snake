import heapq
import random
import pygame
import numpy as np
from hamiltonian import Hamiltonian

class Board:
    def __init__(self, dimensions, window, window_size, color):
        self.dimensions = dimensions;
        self.window = window;
        self.window_size = window_size;
        self.color = color;
        self.snake = []
        self.food = (0,0)
        self.head_path = []
        self.board = [ [0]*self.dimensions[0] for i in range(self.dimensions[1])]
        self.shortest_path = []
        self.cycle = []

    def create_grid(self):
        for i in range(1, self.dimensions[0]):
            pygame.draw.line(self.window, self.color, (0, i * 20), (self.window_size[0], i * 20))
        for k in range(1, self.dimensions[1]):
            pygame.draw.line(self.window, self.color, (k * 20, 0), (k * 20, self.window_size[1]))

    def paint_pieces(self):
        self.board = [[0]*self.dimensions[0] for i in range(self.dimensions[1])]
        for l in range(len(self.snake)):
            if(l == 0):
                pygame.draw.rect(self.window, (0,0,255), (self.snake[l][0]*20, self.snake[l][1]*20, 20, 20))
            else:
                pygame.draw.rect(self.window, (0,255,0), (self.snake[l][0]*20, self.snake[l][1]*20, 20, 20))
            self.board[self.snake[l][1]][self.snake[l][0]] = 1

        self.board[self.food[1]][self.food[0]] = 2
        pygame.draw.rect(self.window, (255,0,0), (self.food[0]*20, self.food[1]*20, 20, 20))


    def place_food(self):
        num1 = random.randint(0, self.dimensions[0] - 1)
        num2 = random.randint(0, self.dimensions[1] - 1)
        
        self.food = (num1, num2);
    
    def create_snake(self):
        num1 = random.randint(0, self.dimensions[0] - 1)
        num2 = random.randint(0, self.dimensions[1] - 1)
        self.snake.append((0,0))
        self.head_path.append((0,0))

    def move_snake(self, direction):
        self.snake[0] = (self.snake[0][0] + direction[0], self.snake[0][1] + direction[1])
        self.head_path.append((self.snake[0][0], self.snake[0][1]))

        for k in range(1, len(self.snake)):
            x = self.head_path[len(self.head_path) - 1 - k]
            self.snake[k] = (x[0], x[1])
    
    def check_snakeate(self, direction):
        if(self.snake[0] == self.food):
            x = self.head_path[len(self.head_path) - 1 - len(self.snake)]
            self.snake.append((x[0], x[1]))
            self.place_food()
    
    def check_collison(self):
        if(self.snake[0] in self.snake[2:len(self.snake) - 1]):
            print(self.snake)
            return True

        return False
    
    def find_shortest_path(self):
        start = self.snake[0]
        end = self.food
        if(len(self.snake) == 1):
            hamiltonian = Hamiltonian(self.dimensions[0], self.dimensions[1])
            self.cycle = hamiltonian.get_cycle()
            self.shortest_path = self.cycle.copy()
        else:
            self.shortest_path = self.cycle.copy()

        self.shortest_path.pop(0)
        #self.shortest_path = self.astar(np.array(self.board), start, end)
        

    def print_board(self,board):
        for row in board:
            print(row)

    def ai_move(self):
        #print(self.cycle, "\n")
        if(self.snake[0] == (0,0)):
            self.move_snake((1,0))
            self.find_shortest_path()
        elif(self.snake[0] == (0,1)):
            self.move_snake((0,-1))
            self.find_shortest_path()
        else:
            try:
                if(len(self.shortest_path) > 0):
                    self.move_snake((self.shortest_path[0][0] - self.snake[0][0], self.shortest_path[0][1] - self.snake[0][1]))
                    self.shortest_path.pop(0)
            except:
                pass
        #try:
        #    if(len(self.shortest_path) > 0):
        #        self.move_snake((self.shortest_path[len(self.shortest_path) - 1][0] - self.snake[0][0], self.shortest_path[len(self.shortest_path) - 1][1] - self.snake[0][1]))
        #        self.shortest_path.pop()
        #except:
        #    self.move_snake((1,0))

    def heuristic(self, a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    def astar(self, array, start, goal):

        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

        close_set = set()

        came_from = {}

        gscore = {start:0}

        fscore = {start:self.heuristic(start, goal)}

        oheap = []

        heapq.heappush(oheap, (fscore[start], start))
    

        while oheap:

            current = heapq.heappop(oheap)[1]

            if current == goal:

                data = []

                while current in came_from:

                    data.append(current)

                    current = came_from[current]

                return data

            close_set.add(current)

            for i, j in neighbors:

                neighbor = current[0] + i, current[1] + j            

                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)

                if 0 <= neighbor[0] < array.shape[0]:

                    if 0 <= neighbor[1] < array.shape[1]:                

                        if array[neighbor[0]][neighbor[1]] == 1:

                            continue

                    else:

                        # array bound y walls

                        continue

                else:

                    # array bound x walls

                    continue
    

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):

                    continue
    

                if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:

                    came_from[neighbor] = current

                    gscore[neighbor] = tentative_g_score

                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)

                    heapq.heappush(oheap, (fscore[neighbor], neighbor)) 

