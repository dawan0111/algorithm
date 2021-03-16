import sys

R, C = map(int, sys.stdin.readline().split())
map = [list(sys.stdin.readline().strip()) for _ in range(R)]
answer = 0

stacks = [( 0, 0, map[0][0] )]
dms = ([-1, 0], [0, 1], [1, 0], [0, -1])

while stacks:
    y, x, visited = stacks.pop()
    answer = max(answer, len(visited))
    for dm in dms:
        ny = y + dm[0]
        nx = x + dm[1]
        if -1 < ny < R and -1 < nx < C and map[ny][nx] not in visited:
            stacks.append(( ny, nx, visited + map[ny][nx] ))

print(answer)