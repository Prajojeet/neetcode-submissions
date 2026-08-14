# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root=TreeNode(val)
            return root
        curr=root
        while(curr!=None):
            prev=curr
            if val<curr.val:
                curr=curr.left
                if curr==None:
                    prev.left=TreeNode(val)
                    
            else:
                curr=curr.right
                if curr==None:
                    prev.right=TreeNode(val)
        return root