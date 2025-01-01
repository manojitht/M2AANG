class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

R = TreeNode("R")
A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")

R.left = A
R. right = B

A.left = C
A.right = D

B.left = E
B.right = F

print("The top is - ", R.data)
print("The R left is - ", R.left.data)
print("The R right is - ", R.right.data)
