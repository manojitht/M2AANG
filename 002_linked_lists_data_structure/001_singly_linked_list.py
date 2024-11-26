class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.next = B
B.prev = A
B.next = C
C.prev = B
C.next = D
D.prev = C
D.next = E
E.prev = D

curr = A
nodes = []
while curr is not None:
    nodes.append(str(curr.data))
    curr = curr.next
print(" -> ".join(nodes))

curr_back = E
nodes_back = []
while curr_back is not None:
    nodes_back.append(str(curr_back.data))
    curr_back = curr_back.prev
print(" -> ".join(nodes_back))