import collections

de=collections.deque([1,2,3])

de.append(4)

print("The deque after appending at the right is :")
print(de)

de.appendleft(6)

print("the deque after appending at left is :")
print(de)

de.pop()

print("the deque after deleting from right is :")
print(de)

de.popleft()

print("The deque after deleting from left is :")
print(de)