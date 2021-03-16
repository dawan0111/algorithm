import sys

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

        return len(current_node.children) == 0

    def consist_check(self, string):
        current_node = self.head
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        return len(current_node.children) == 0

    def clear(self):
        self.head = Node(None)

t = int(sys.stdin.readline())
trie = Trie()

for i in range(t):
    n = int(sys.stdin.readline())
    error = False
    numbers = [None] * n

    for j in range(n):
        number = str(sys.stdin.readline().rstrip())
        trie.insert(number)
        numbers[j] = number

    for number in numbers:
        if not trie.consist_check(number):
            error = True
            break

    if error:
        print("NO")
    else:
        print("YES")

    trie.clear()

