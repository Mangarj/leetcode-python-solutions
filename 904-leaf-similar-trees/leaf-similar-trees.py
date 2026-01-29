# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeaves(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            getLeaves(root.left, leaves)
            getLeaves(root.right, leaves)
        leaves1 = []
        leaves2 = []
        getLeaves(root1, leaves1)
        getLeaves(root2, leaves2)
        
        return leaves1 == leaves2

        