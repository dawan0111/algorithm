T = int(input())

def printer_find():
    N, M = map(int, input().split())
    queues = list(map(int, input().split()))
    printers = [i for i in range(len(queues))]
    count = 0

    for i in range(9, 0, -1):
        while i in queues:
            queue = queues.pop(0)
            now = printers.pop(0)

            if queue != i:
                queues.append(queue)
                printers.append(now)
            else:
                count += 1
                if now == M:
                    return count
    return count

for _ in range(T):
    print(printer_find())




