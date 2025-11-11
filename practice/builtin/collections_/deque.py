import timeit
from collections import deque

# definition
dq = deque('def')

# append
dq.append('g')
dq.appendleft('a')

print(dq)

# autoshift
dq = deque([1, 2, 3], maxlen=3)

dq.append(4)
print(dq)

dq.appendleft(1)
print(dq)

# extend
dq = deque([1, 2, 3])

dq.extend([4, 5, 6])
print(dq)

dq.extendleft([0, -1])
print(dq)

# loop shift
dq.rotate(-1)

print(dq)

# index access
print(dq[0], dq[-1])

# pop
dq.pop()
dq.popleft()
print(dq)

# example
lst = [i for i in range(100)]
dq = deque(lst, 5)
print(dq)

# list быстрее для произвольного доступа (на краях примерно одинаково)
d = deque(range(1000))
lst = list(range(1000))

print(timeit.timeit(lambda: d[500], number=100000))
print(timeit.timeit(lambda: lst[500], number=100000))
