# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])
        while queue:
            rightSide = None 
            for _ in range(len(queue)): 
                node = queue.popleft()
                if node: 
                    rightSide = node 
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide: 
                res.append(rightSide.val)
        return res 
        