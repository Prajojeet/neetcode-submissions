# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, root, output):
        if root is None:
            return
        self.func(root.left,output)
        self.func(root.right,output)
        output.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        self.func(root,output)
        return output
        