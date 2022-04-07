class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #DFS implementaion
        courseGraph = collections.defaultdict(list)
        inDegree = [0] * numCourses
        for course in prerequisites:
            courseGraph[course[1]].append(course[0])
        for course in prerequisites:
            if(course[0] == course[1]):return False
            inDegree[course[0]] +=1
        queue = deque([])
        count = 0
        for degree in range(len(inDegree)):
            if(inDegree[degree] == 0): queue.append(degree)
        while(queue):
            count+=1
            curr = queue.popleft()
            if(count > numCourses): return False
            for i in courseGraph[curr]:
                inDegree[i] -= 1
                if(inDegree[i] == 0): queue.append(i)
        if(count < numCourses): return False
        else: return False