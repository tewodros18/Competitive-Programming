class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = defaultdict(int)
        Dir = [[0,1],[1,0],[-1,0],[0,-1]]
        chk = lambda r,c : True if 0 <= r <len(grid) and 0 <= c < len(grid[0]) else False 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1): islands[(i,j)] = (i,j)
        def find(x):
            if(islands[x] == x): return x
            islands[x] = find(islands[x])
            return islands[x]
        def union(node1,node2):
            node1,node2 = find(node1),find(node2)
            #node2,node1 = sorted([node1,node2], key = lambda x: grid[x[0]][x[1]])
            if(node1 != node2):
                grid[node1[0]][node1[1]] += grid[node2[0]][node2[1]]
                islands[node2] = node1
        for i in islands:
            for D in Dir:
                if(chk(i[0] + D[0],i[1] + D[1]) and grid[i[0] + D[0]][i[1] + D[1]]):
                    union(i,(i[0] + D[0],i[1] + D[1]))
        Max = 0
        for i in islands:
            Max = max(Max,grid[i[0]][i[1]])
        return Max