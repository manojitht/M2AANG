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

def count(head):
    curr = head
    length = 0
    while curr is not None:
        length += 1
        curr = curr.next
    print(f"The count of the LL is {length}.")

def insert_first(head, data):
    new_node = Node(data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node

def insert_last(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    return head


# forward_traversal(H)
# backward_traversal(T)
# search(H, 3)
# count(H)

## insert first
# h = insert_first(H, 7)
# forward_traversal(h)

## insert last
# h = insert_last(H, 7)
# forward_traversal(h)
