# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reversal(self,root):
        if root==None:
            return
        temp=root.left
        root.left=root.right
        root.right=temp
        self.reversal(root.right)
        self.reversal(root.left)



    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reversal(root)
        return root
        