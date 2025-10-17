# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        result = []
        queue = deque()

        if not root:
            return []
        else:
            queue.append(root)

        result.append([root.val])

        while queue:
            cur_level = []
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    cur_level.append(cur.left.val)
                if cur.right:
                    queue.append(cur.right)
                    cur_level.append(cur.right.val)
            if cur_level:
                result.append(cur_level)
        return result
            