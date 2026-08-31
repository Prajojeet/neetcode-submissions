# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Searching the node to be deleted
    def search(self, curr, prev, target):
        # Base Case
        if curr==None or curr.val==target:
            return curr,prev

        # Recursive case
        if curr.val>target:
            node=curr.left
        else:
            node=curr.right

        # Store the previous node too    
        prev = curr
        return self.search(node, prev, target)

    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # Storing deleted and prev_node
        node_del, prev_node=self.search(root,None,val)


        # Edge case 0 - not found
        if node_del==None:
            return root

        # Edge case 1 - root is key
        if node_del==root:
            if node_del.right:
                new=node_del.right
                while(new.left!=None):
                    new=new.left
                new.left=root.left
                root=node_del.right
                return root
            else: 
                return node_del.left
            
        # Edge case 2 - left donot exist
        if node_del.left==None:
            if prev_node.val>node_del.val:
                prev_node.left=node_del.right
            else:
                prev_node.right=node_del.right
            return root

        # Edge case 3 - right donot exist
        if node_del.right==None:
            if prev_node.val>node_del.val:
                prev_node.left=node_del.left
            else:
                prev_node.right=node_del.left
            return root
            
        # Edge case 4 - Leaf node

        if node_del.right==None and node_del.left==None:
            if prev_node.val>node_del.val:
                prev_node.left=None
            else:
                prev_node.right=None
            return root

        # Normal case
        left_node=node_del.left
        right=node_del.right

        # Direct connection
        if prev_node.val>node_del.val:
            prev_node.left=left_node
        else: 
            prev_node.right=left_node

        while(left_node.right!=None):
            left_node=left_node.right
        left_node.right=right

        return root