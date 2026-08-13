# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Write this code using deque - a functionality that I can use always no matter what!!
        q=deque()
        ans=[]
        if root is None:
            return ans
        q.append(root)
        while(len(q)>0):
            ans.append(q[-1].val)
            length=len(q)
            for i in range(length):
                node=q.popleft()
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
        return ans