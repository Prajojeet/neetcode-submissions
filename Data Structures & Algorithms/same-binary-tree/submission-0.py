# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Let's do in order traversal and compare things in the way itself
    def __init__(self):
        self.ans=True
    def traversal(self,p,q):
        if p==None and q==None:
            return 

        if (p==None and q!=None) or (p!=None and q==None):
            self.ans=False
            return
        
        if p.val!=q.val:
            self.ans=False

        self.traversal(p.left,q.left)
        self.traversal(p.right,q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.traversal(p,q)
        return self.ans