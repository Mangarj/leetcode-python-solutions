# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.post_index = len(postorder) - 1
        
        def helper(left, right):
            if left > right:
                return None
            
            root_val = postorder[self.post_index]
            self.post_index -= 1
            
            root = TreeNode(root_val)
            index = inorder_map[root_val]
            
            # Important: build right subtree first
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)
        