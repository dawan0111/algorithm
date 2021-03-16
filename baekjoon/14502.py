import copy
import sys
from itertools import combinations

answer = -1
V, W = map(int, sys.stdin.readline().split())
M = [list(map(int, sys.stdin.readline().split())) for _ in range(V)]

map_offsets = [[], [], []]

for i in range(V):
    for j in range(W):
        map_offsets[M[i][j]].append([i, j])

combs = []
for i in list(combinations(map_offsets[0], 3)):
    combs.append(i)

for comb in combs:
    M_c = copy.deepcopy(M)
    safety_count = len(map_offsets[0]) - 3
    for c in comb:
        M_c[c[0]][c[1]] = 1
    queue = map_offsets[2][:]
    while queue:
        now = queue.pop(-1)
        if now[0] + 1 < V and M_c[now[0] + 1][now[1]] == 0:
            safety_count -= 1
            M_c[now[0] + 1][now[1]] = 2
            queue.append([now[0] + 1, now[1]])

        if now[0] > 0 and M_c[now[0] - 1][now[1]] == 0:
            safety_count -= 1
            M_c[now[0] - 1][now[1]] = 2
            queue.append([now[0] - 1, now[1]])

        if now[1] + 1 < W and M_c[now[0]][now[1] + 1] == 0:
            safety_count -= 1
            M_c[now[0]][now[1] + 1] = 2
            queue.append([now[0], now[1] + 1])

        if now[1] > 0 and M_c[now[0]][now[1] - 1] == 0:
            safety_count -= 1
            M_c[now[0]][now[1] - 1] = 2
            queue.append([now[0], now[1] - 1])

    answer = max(answer, safety_count)

print(answer)