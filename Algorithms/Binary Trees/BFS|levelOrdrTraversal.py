from collections import deque

class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

  def bfs(root):
    
    res, q = [], deque([root]) if root else None

    while q:
      n, temp = len(q), []

      for i in range(n):
        node = q.popleft()
        temp.append(node.val)

        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)

      res.append(temp)

    return res

x = TreeNode(1)
x.left = TreeNode(2)
x.right = TreeNode(3)
x.left.left = TreeNode(4)
x.left.right = TreeNode(5)
x.right.left = TreeNode(6)
x.right.right = TreeNode(7)
