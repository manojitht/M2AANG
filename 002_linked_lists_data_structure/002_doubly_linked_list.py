class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


H = Node(1)
A = Node(2)
B = Node(3)
C = Node(4)
D = Node(5)
T = Node(6)

H.next = A
A.prev = H
A.next = B
B.prev = A
B.next = C
C.prev = B
C.next = D
D.prev = C
D.next = T
T.prev = D

def forward_traversal(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next

def backward_traversal(tail):
    curr = tail
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.prev

def search(head, data):
    curr = head
    while curr is not None:
        if curr.data == data:
            print("yes")
        curr = curr.next

# forward_traversal(H)
# backward_traversal(T)
# search(H, 3)
