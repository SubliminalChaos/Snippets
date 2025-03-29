from collections import deque

# deque is a double ended queue, can remove from both ends

d = deque()

d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
d.extend([3, 2, 1, 0])
print(d)
d.extendleft([7, 8, 9])
print(d)

d.rotate(1)  # negative values rotate left!  xD
print(d)
