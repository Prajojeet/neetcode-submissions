# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, curr, output):
        if curr==None:
            return
        output.append(curr.val)
        self.func(curr.left,output)
        self.func(curr.right,output)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        self.func(root,output)
        return output