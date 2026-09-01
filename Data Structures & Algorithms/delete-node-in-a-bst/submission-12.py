# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base Case: In case the tree is empty or node not found
        if not root:
            return None
        # Searching for the node (This was the step creating so many edges)
        if key<root.val:
            root.left = self.deleteNode(root.left,key)
        elif key>root.val:
            root.right = self.deleteNode(root.right,key)

        # Found the node
        else: 
            # Edge case: only 0 or 1 node is there
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # With atleast 1 node each side
            curr = root.left
            while(curr.right!=None):
                curr=curr.right

            # Attach the node to the end
            curr.right=root.right

            # Return the left node to the deleted node
            return root.left


        return root