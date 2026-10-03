# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # Basically at each node compute right and left sum
        def dfs(root):
            if root == None:
                return 0
            # Check at each node, is sum from 2 sides is greater
            self.res = max((dfs(root.left) + dfs(root.right)), self.res)
            # Also calculate the longest side if above is not the case
            return 1 + max(dfs(root.left), dfs(root.right))
        
        dfs(root)
        return self.res