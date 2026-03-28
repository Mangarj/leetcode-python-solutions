# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root):
        curr = root
        
        while curr:
            if curr.left:
                # Find rightmost node of left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Connect right subtree
                prev.right = curr.right
                
                # Move left subtree to right
                curr.right = curr.left
                curr.left = None
            
            # Move to next node
            curr = curr.right

        