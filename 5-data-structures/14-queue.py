from collections import deque

dequeList = deque([])

dequeList.append(1)
dequeList.append(2)
dequeList.append(3)
dequeList.append(4)
dequeList.append(5)

print(dequeList)

dequeList.popleft()
print(dequeList)

print(type(dequeList))