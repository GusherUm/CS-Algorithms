# These traversals basically can be attributed to Depth-First-Search

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Problem:
    # preorder -> start from root; go left; go right
    def preorder(self, root):     # Classical DFS.(That is first traverse on left branch and then the right branch)
        if root:
            print(root.val, end = '')
            self.preorder(root.left)
            self.preorder(root.right)

    # inorder -> go left; go to parent; go to right
    # down up down up down up down up down .... down
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end = '')
            self.inorder(root.right)

    # postorder -> go left; go right jumping around the parent; go to parent
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end = '')

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.left = TreeNode(8)
root.right.left.right = TreeNode(9)

obj = Problem()
obj.preorder(root)
print()
print("$$$$$$$$$$$$$$$$$$$$$$$$")
obj.inorder(root)
print()
print("$$$$$$$$$$$$$$$$$$$$$$$$")
obj.postorder(root)
