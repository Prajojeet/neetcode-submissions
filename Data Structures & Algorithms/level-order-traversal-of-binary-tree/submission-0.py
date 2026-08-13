# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[[root.val]]
        pointer=0
        queue=[root]

        while(pointer<len(queue)):
            level=[]
            for i in range(pointer,len(queue),1):
                if queue[i].left!=None:
                    level.append(queue[i].left.val)
                    queue.append(queue[i].left)
                if queue[i].right!=None:
                    level.append(queue[i].right.val)
                    queue.append(queue[i].right)
                pointer+=1
            if len(level)>0:
                ans.append(level)  
        return ans
