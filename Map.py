import random

class Map():
    
    def __init__(self, obs_type):
        self.map = self.emptyMap()
        if obs_type == 1:
            self.generateObstacles1()
        elif obs_type == 2:
            self.generateObstacles2()
        elif obs_type == 3:
            self.generateObstacles3()
            
        self.generateStartFinish()

    def generateObstacles1(self):
        obstacles_placed = 0
        while obstacles_placed < 10:
            rand_row = random.randint(1,8)
            rand_col = random.randint(1,8)
            obstacles_placed += self.makeWall1(rand_row, rand_col)
            
    def generateObstacles2(self):
        obstacles_placed = 0
        while obstacles_placed < 10:
            rand_row = random.randint(1,8)
            rand_col = random.randint(1,8)
            if self.map[rand_row][rand_col] != 'X':
                self.map[rand_row][rand_col] = 'X'
                obstacles_placed += 1
            
    def generateObstacles3(self):
        obstacles_placed = 0
        while obstacles_placed < 10:
            rand_row = random.randint(1,8)
            rand_col = random.randint(1,8)
            obstacles_placed += self.makeWall3(rand_row, rand_col, 3)

    def generateStartFinish(self):
        pass
        
    def emptyMap(self):
        m = []
        for x in range(10):
            m.append(['.']*10)
        return m

    def printMap(self):
        print ' ' + '- '*(11)
        for row in self.map:
            line = '| '
            for col in row:
                line += col + ' '
            line += '|'
            print line
        print ' ' + '- '*(11)

    def placeObstacle(self,x,y):
        if self.map[x][y] != 'X':
            self.map[x][y] = 'X'
            return 1
        return 0
    
    def makeWall1(self, x, y):
        num_placed = 0
        if random.randint(0,99) < 50:
            num_placed += self.placeObstacle(x,y-1)
            num_placed += self.placeObstacle(x,y)
            num_placed += self.placeObstacle(x,y+1)
        else:
            num_placed += self.placeObstacle(x-1,y)
            num_placed += self.placeObstacle(x,y)
            num_placed += self.placeObstacle(x+1,y)
        return num_placed

    def makeWall3(self, x, y, num):
        num_placed = 0
        if random.randint(0,99) < 50:
            """ RIGHT/LEFT """
            num_placed += self.placeObstacle(x,y)
            
            num_right = random.randint(0,num)
            num_left = random.randint(0,num)
            for r in range(1,num_right+1):
                if y+r > 9:
                    break
                else:
                    num_placed += self.placeObstacle(x,y+r)
            for l in range(1, num_left+1):
                if y-l < 0:
                    break
                else:
                    num_placed += self.placeObstacle(x,y-l)
            
        else:
            """ UP/DOWN """
            num_placed += self.placeObstacle(x,y)
            
            num_up = random.randint(0,num)
            num_down = random.randint(0,num)
            for u in range(1,num_up+1):
                if x-u < 0:
                    break
                else:
                    num_placed += self.placeObstacle(x-u,y)
            for d in range(1, num_down+1):
                if x+d > 9:
                    break
                else:
                    num_placed += self.placeObstacle(x+d,y)

        return num_placed


