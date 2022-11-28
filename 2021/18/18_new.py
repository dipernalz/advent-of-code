from collections import deque
from math import ceil, floor

inpt = open('input.txt', 'r').read().rstrip().split('\n')


class Node:
    def __init__(self, x=None):
        self.val = None
        self.left = None
        self.right = None
        self.prev = None
        self.next = None
        if isinstance(x, int):
            self.val = x
        elif isinstance(x, list):
            self.left = Node(x[0])
            self.right = Node(x[1])

    def adj(self):
        q = deque([self])
        nodes = []
        while q:
            node = q.pop()
            if not node:
                continue
            if isinstance(node.val, int):
                nodes.append(node)
            q.append(node.right)
            q.append(node.left)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]

    def add(self, other):
        new = Node()
        new.left = self
        new.right = other

        a = new.left
        while a.right:
            a = a.right
        b = new.right
        while b.left:
            b = b.left
        a.next = b
        b.prev = a

        new.reduce()
        return new

    def reduce(self):
        u = True
        while u:
            u = self._explode()
            if not u:
                u = self._split()

    def magnitude(self):
        if isinstance(self.val, int):
            return self.val
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def _explode(self):
        u = False
        q = deque([(self, 0)])
        while q:
            node, depth = q.pop()
            if not node:
                continue
            if depth == 4 and node.val is None:
                if node.left.prev:
                    node.left.prev.val += node.left.val
                    node.left.prev.next = node
                if node.right.next:
                    node.right.next.val += node.right.val
                    node.right.next.prev = node
                node.val = 0
                node.prev = node.left.prev
                node.next = node.right.next
                node.left = None
                node.right = None
                u = True
            q.append((node.right, depth + 1))
            q.append((node.left, depth + 1))
        return u

    def _split(self):
        q = deque([self])
        while q:
            node = q.pop()
            if not node:
                continue
            if isinstance(node.val, int) and node.val >= 10:
                left = Node()
                left.val = floor(node.val / 2)
                left.prev = node.prev
                if left.prev:
                    left.prev.next = left
                right = Node()
                right.val = ceil(node.val / 2)
                right.next = node.next
                if right.next:
                    right.next.prev = right
                left.next = right
                right.prev = left
                node.val = None
                node.left = left
                node.right = right
                return True
            q.append(node.right)
            q.append(node.left)
        return False

    def __str__(self):
        if isinstance(self.val, int):
            return str(self.val)
        return f'[{str(self.left)},{self.right}]'


# Part 1
node = Node(eval(inpt[0]))
node.adj()
for i in inpt[1:]:
    nxt = Node(eval(i))
    nxt.adj()
    node = node.add(nxt)
print(node.magnitude())

# Part 2
m = 0
for i in range(len(inpt)):
    for j in range(len(inpt)):
        if i == j:
            continue
        a, b = Node(eval(inpt[i])), Node(eval(inpt[j]))
        a.adj()
        b.adj()
        m = max(m, a.add(b).magnitude())
print(m)
