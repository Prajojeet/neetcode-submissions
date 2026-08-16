# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.root=None

    def traversal(self, root, p, q): # Minding q is always greater than p
        if root.val<=q.val and root.val>=p.val:
            self.root = root
        elif root.val>p.val and root.val>q.val:
            self.traversal(root.left,p,q)
        else:
            self.traversal(root.right,p,q)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val>q.val:
            temp=p
            p=q
            q=temp
        self.traversal(root,p,q)
        return self.root


