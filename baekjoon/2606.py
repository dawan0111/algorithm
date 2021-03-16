N = int(input())
linkCount = int(input())
linkList = [None] * (N + 1)

for i in range(linkCount):
    node1, node2 = map(int, input().split())
    if linkList[node1] is None:
        linkList[node1] = []

    if linkList[node2] is None:
        linkList[node2] = []

    linkList[node1].append(node2)
    linkList[node2].append(node1)

visited = [1]
stack = [1]

while stack:
    nowNode = stack.pop()
    linkNode = linkList[nowNode]

    for node in linkNode:
        if node not in visited:
            visited.append(node)
            stack.append(node)

print(len(visited) - 1)