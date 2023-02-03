# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        di = defaultdict(list)
        answer = []
        def dfs(node,parent):
            if(node.left):
                dfs(node.left,(parent[0]+1,parent[1]-1))
            if(node.right):
                dfs(node.right,(parent[0]+1,parent[1]+1))
            di[parent[1]].append((node.val,parent[0]))
        dfs(root,(0,0))
        for k in sorted(di):
            di[k].sort(key=lambda x:[x[1],x[0]])
            t = [i[0] for i in di[k]]
            answer.append(t)
        return answer
