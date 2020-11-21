import random
import heapq

class A:
    name = 'a'
    val = 0
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def __str__(self):
        return f'<name={self.name} val={self.val}>'
    def __lt__(self, other):
        if isinstance(other, A):
            return self.val <= other.val

h = list()

for i in range(25):
    obj = A(
        name=str(random.randint(0, 9)),
        val = random.randint(0, 9)
    )
    heapq.heappush(h, obj)

for i in range(len(h)):
    children_i = [2 * i + 1, 2 * i + 2]
    for j in children_i:
        if j < len(h):
            assert h[i] < h[j]
