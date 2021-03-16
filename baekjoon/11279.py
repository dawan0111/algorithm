
class Heap:
    def __init__(self):
        self.heap_array = [None]
        self.size = 0

    def insert(self, value):
        self.heap_array.append(value)
        self.size += 1
        i = self.size

        while i // 2 > 0:
            if self.heap_array[i // 2] < value:
                self.heap_array[i // 2], self.heap_array[i] = self.heap_array[i], self.heap_array[i // 2]
                i = i // 2
            else:
                break

    def max_delete(self):
        if (self.size == 0):
            return 0

        self.heap_array[1], self.heap_array[-1] = self.heap_array[-1], self.heap_array[1]
        root = self.heap_array.pop()
        size = self.size
        self.size -= 1

        i = 1
        while i * 2 <= size:
            k = i * 2
            if (k < size and self.heap_array[k] < self.heap_array[k + 1]):
                k += 1

            if (self.heap_array[i] < self.heap_array[k]):
                self.heap_array[i], self.heap_array[k] = self.heap_array[k], self.heap_array[i]
            else:
                break

            i = k

        return root

    def print(self):
        print(self.heap_array)

N = int(input())
heap = Heap()

for _ in range(N):
    x = int(input())
    if (x == 0):
        print(heap.max_delete())
    else:
        heap.insert(x)
