# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidTree(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False

            return isValidTree(node.left, left, node.val) and isValidTree(node.right, node.val, right)


        return isValidTree(root, float('-inf'), float('inf'))