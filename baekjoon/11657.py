INF = int(1e9)

def bellman_ford(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost

    for _ in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = INF * -1


n, m = map(int, input().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

bellman_ford(1)
if INF * -1 in dist:
    print("-1")
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])