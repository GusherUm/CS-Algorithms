class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def preorder(self, root):

        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

        return
    
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

        return
    
    def postorder(self, root):

        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

        return
    
x = TreeNode(1)
x.left = TreeNode(2)
x.right = TreeNode(3)
x.left.right = TreeNode(4)

# Preorder: 1, 2, 4, 3
# inorder: 2, 4, 1, 3
# Postorder: 4, 2, 3, 1

x.preorder(x)
x.inorder(x)
x.postorder(x)
