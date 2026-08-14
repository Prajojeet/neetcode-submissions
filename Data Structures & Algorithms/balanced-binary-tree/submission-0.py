# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
# This is the entire logic where I was stuck at ie how to end the recursion if once the ans is False. Turns out I don't have to stop the recursion at all if the thing stops, its just a different variable can store the result False which is printed ahead!!!!
    def __init__(self):
        self.ans=True

    def height(self, root):
        if root==None:
            return 0
        left=self.height(root.left)
        right=self.height(root.right)

        if abs(left-right)>1:
            self.ans=False
        return 1+max(left,right)   

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.height(root)
        return self.ans