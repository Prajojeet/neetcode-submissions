# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.arranged=[]
    # Short circuiting once reach k

    def dfs(self, root):
        if root is None:
            return
        
        self.dfs(root.left)
        
        self.k+=1

        if self.k==0:
            self.result=root.val
            return

        self.dfs(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=-k
        self.dfs(root)
        return self.result