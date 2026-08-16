# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    # Two parts, find the same value first, if found then the same last question approach of comparing the trees 
    def Compare(self, root, subRoot):
        if root==None and subRoot==None:
            return True
        
        if root==None or subRoot==None:
            return False

        if root.val!=subRoot.val:
            return False

        return self.Compare(root.left,subRoot.left) and self.Compare(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot==None:
            return True

        if root==None:
            return False
        
        if self.Compare(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        


        