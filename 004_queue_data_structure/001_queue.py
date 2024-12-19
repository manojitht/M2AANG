from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

queue.popleft()

if queue:
    print(queue)
else:
    print("queue is empty")

# the deque is the best practice when it's comes to queue DS, it could avoid number of operations when remove the item at beginning.
# O(1) operation