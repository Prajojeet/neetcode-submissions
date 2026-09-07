# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bst(self, root,l,r):
        # Base Case
        if not root:
            return True

        # Main case
        if root.val<=l or root.val>=r:
            return False
        
        return self.bst(root.left, l, root.val) and self.bst(root.right, root.val,r)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bst(root, float('-inf'), float('inf'))
       