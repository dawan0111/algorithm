import sys

r = sys.stdin.readline
N, W = map(int, r().split())
bag = [tuple(map(int, r().split())) for _ in range(N)]

knap = [0 for _ in range(W+1)]

for i in range(N):
    for j in range(1, W + 1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])

print(knap[-1])

'''
N, K = list(map(int, input().split()))
values = [list(map(int, input().split())) for _ in range(N)]
backpack = [[0] * (K + 1) for _ in range(N + 1)]

배낭문제
물건의 갯수가 n개 일때
n번째 물건을 넣을때 n - 1 번째 물건을 넣었을때 가중치와 비교하며 최적해를 구해간다.
문제 풀이 기법
물건을 한개 넣었을때 두개 넣었을때 따로 따로 계산한 값을 저장하여 다음 n + 1 번째 물건을 넣었을때 사용해 나간다.
나는 이전 값 저장하는 방법이 햇갈렸고 저장할때 물건보다 배낭이 클때 이전값으로 저장해도 되는지 확신이 없었다.

for i in range(1, N + 1):
    weight = values[i-1][0]
    value = values[i-1][1]

    for k in range(1, K + 1):
        if (weight > k):
            backpack[i][k] = backpack[i - 1][k]
        else:
            backpack[i][k] = max(backpack[i - 1][k - weight] + value, backpack[i - 1][k])

print(backpack[N][K])
'''