# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def vbs(self, root, lower, upper):
        # Base Case
        if root is None:
            return True

        # Check for validation
        if not (lower < root.val < upper):
            return False


        return self.vbs(root.left, lower, root.val) and self.vbs(root.right, root.val, upper)

        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.vbs(root,-1000000000,1000000000)