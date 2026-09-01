# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def vbs(self, root, r1, r2):
        # Base Case
        if root is None:
            return True

        # Check for validation
        if root.val<=r1 or root.val>=r2:
            return False

        # 0 or 1 node
        if not root.left and not root.right:
            return True
        elif not root.left:
            return self.vbs(root.right, root.val, r2)
        elif not root.right:
            return self.vbs(root.left, r1, root.val)


        return self.vbs(root.left, r1, root.val) and self.vbs(root.right, root.val, r2)

        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.vbs(root,-1000000000,1000000000)