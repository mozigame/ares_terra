import heapq
import json
from collections import defaultdict, OrderedDict


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('qrok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

pairs = {'a': 123, 'b': 444}
d = defaultdict(list)
for key, value in pairs.items():
    d[key].append(value)
print(d)

d = OrderedDict()
d['foo'] = 1
d['bar'] = 1
d['spam'] = 1
d['grok'] = 1
for key in d:
    print(key, d[key])

print(json.dumps(d))
