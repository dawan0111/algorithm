'''
answer = 1
m, n = list(map(int, input().split()))
map = [list(map(int, input())) for _ in range(m)]

maxLength = min(n, m)

memo = []

for x in range(n):
    for y in range(m):
        if map[y][x] == 1:
            memo.append([y, x])

for i in range(1, maxLength + 1):
    _memo = []
    for j in range(len(memo)):
        if (memo[j][0] + i >= m or memo[j][1] + i >= n or map[memo[j][0] + i][memo[j][1] + i] == 0):
            continue

        isSquare = True
        for o in range(i):
            if (map[memo[j][0] + i][memo[j][1] + o] == 0 or map[memo[j][0] + o][memo[j][1] + i] == 0):
                isSquare = False
                break

        if (isSquare):
            _memo.append(memo[j])

    if (len(_memo) == 0):
        print(i ** 2)
        break
    else:
        memo = _memo
'''

n, m = map(int, input().split())
table = [list(map(int, list(input().rstrip()))) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if i>0 and j>0 and table[i][j] == 1:
            table[i][j] += min(table[i-1][j], table[i][j-1], table[i-1][j-1])
            ans = max(ans, table[i][j])

print(ans ** 2)

n, m = map(int, input().split())

data = []

for i in range(n):
    s = input()
    data.append(list(map(int, list(s))))

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
side = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if data[i - 1][j - 1] == 1:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

            if dp[i][j] > side:
                side = dp[i][j]

print(side ** 2)
