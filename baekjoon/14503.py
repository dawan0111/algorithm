N, M = map(int, input().split())
r, c, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

class Robot:
    def __init__(self, r, c, d, map):
        self.map = map
        self.map_y = len(self.map) - 1
        self.map_x = len(self.map[0]) - 1
        self.x = r
        self.y = c
        self.direction = d

        self.rld = [3, 0, 1, 2]

        self.map[c][r] = 3
        self.__cleanCount = 1

    def __isOverMap(self, x, y):
        return y > self.map_y or x > self.map_y or y < 0 or x < 0

    def __isBlock(self, x, y):
        return not self.__isOverMap(x, y) and self.map[y][x] == 1

    def __isCleaning(self, x, y):
        return not self.__isOverMap(x, y) and self.map[y][x] == 2

    def __isBlockorCleaning(self, x, y):
        return self.__isBlock(x, y) or self.__isCleaning(x, y)

    def __aroundCleanOrBlock(self, x, y):
        return (
            self.__isBlockorCleaning(x - 1, y) and
            self.__isBlockorCleaning(x + 1, y) and
            self.__isBlockorCleaning(x, y - 1) and
            self.__isBlockorCleaning(x, y + 1)
        )

    def __getNowLeftPosition(self):
        if self.direction == 0:
            return [self.x - 1, self.y]
        elif self.direction == 1:
            return [self.x, self.y - 1]
        elif self.direction == 2:
            return [self.x + 1, self.y]
        elif self.direction == 3:
            return [self.x, self.y + 1]

    def __getNowBackPosition(self):
        if self.direction == 0:
            return [self.x, self.y + 1]
        elif self.direction == 1:
            return [self.x - 1, self.y]
        elif self.direction == 2:
            return [self.x, self.y - 1]
        elif self.direction == 3:
            return [self.x + 1, self.y]

    def __getNowNextLeftRotate(self):
        return self.rld[self.direction]

    def set(self, x, y):
        if (self.map[y][x] == 0):
            self.__cleanCount += 1

        self.map[self.y][self.x] = 2
        self.map[y][x] = 3
        self.x = x
        self.y = y

    def leftRotate(self):
        self.direction = self.__getNowNextLeftRotate()

    def play(self):
        j = 0
        while True:
            print(j, "try: ===================")
            for i in self.map:
                print(i)
            j += 1

            if (self.__aroundCleanOrBlock(self.x, self.y)):
                b_p = self.__getNowBackPosition()
                if (self.__isBlock(b_p[0], b_p[1])):
                    return self.__cleanCount
                else:
                    self.set(b_p[0], b_p[1])
            else:
                while True:
                    l_p = self.__getNowLeftPosition()
                    if (self.__isBlockorCleaning(l_p[0], l_p[1])):
                        self.leftRotate()
                    else:
                        self.leftRotate()
                        self.set(l_p[0], l_p[1])
                        break

robot = Robot(r, c, d, map)
cleanBlock = robot.play()

print(cleanBlock)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global ans
    if a[x][y] == 0:
        a[x][y] = 2
        ans += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if a[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if a[nx][ny] == 1:
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
clean(x, y, d)
print(ans)