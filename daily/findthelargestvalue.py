# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        answer = []
        if(root == None):
            return None
        while queue:
            level_size = len(queue)
            temp_max = queue[0].val
            for i in range(level_size):
                current_node = queue.popleft()
                if(current_node.val >= temp_max):
                    temp_max = current_node.val
                if(current_node.left):
                    queue.append(current_node.left)
                if(current_node.right):
                    queue.append(current_node.right)
            answer.append(temp_max)
        return answer