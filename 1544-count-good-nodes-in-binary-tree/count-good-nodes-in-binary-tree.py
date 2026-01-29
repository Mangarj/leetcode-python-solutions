# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            if not node:
                return 0
            
            good = 0
            if node.val >= max_val:
                good = 1
                max_val = node.val
            
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good
        
        return dfs(root, root.val)

        