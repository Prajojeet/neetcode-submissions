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
        if curr.left==None and curr.right==None:
            output.append(curr.val)
            return
        if curr.left!=None:
            output.append(curr.val)
            self.func(curr.left,output)

        if curr.right!=None and curr.left==None:
            output.append(curr.val)
            self.func(curr.right,output)
        else:
            self.func(curr.right,output)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        self.func(root,output)
        return output