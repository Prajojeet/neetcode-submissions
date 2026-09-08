# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.arranged=[]
    # I have to figure out a way to terminate the list for less than linear time
    def dfs(self, root):
        if root is None:
            return
        
        self.dfs(root.left)
        self.arranged.append(root.val)
        self.dfs(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root)
        return self.arranged[k-1]