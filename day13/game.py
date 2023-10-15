import time
import random
class Universe:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.next_world = [[' ' for _ in range(width)] for _ in range(length)]
        self.current_world = [[' ' for _ in range(width)] for _ in range(length)]
        
    def seed(self):
        for i in range(self.length):
            for j in range(self.width):
                if random.random() < 0.25:
                    self.current_world[i][j] = '*'
                    
    def show(self):
        print("\033[2J")
        for row in self.current_world:
            print(''.join(row))
        time.sleep(0.2)
        
    def isalive(self, x, y):
        if x < 0 or x >= self.length or y < 0 or y >= self.width:
            return False
        return self.current_world[x][y] == '*'
        
    def neighbors(self, x, y):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.isalive(x + i, y + j):
                    neighbors += 1
        return neighbors
        
    def next(self):
        for row in range(self.length):
            for column in range(self.width):
                neighbors = self.neighbors(row, column)
                if self.current_world[row][column] == '*':
                    if neighbors < 2 or neighbors > 3:
                        self.next_world[row][column] = ' '
                    else:
                        self.next_world[row][column] = '*'
                else:
                    if neighbors == 3:
                        self.next_world[row][column] = '*'
                    else:
                        self.next_world[row][column] = ' '
        self.current_world, self.next_world = self.next_world, self.current_world

if __name__ == "__main__":
    length = int(input("length=:"))
    width = int(input("width=:"))
    universe = Universe(length, width)
    universe.seed()
    while True:
        universe.show()
        universe.next()
