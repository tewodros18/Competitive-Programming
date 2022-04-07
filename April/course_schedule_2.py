class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseGraph = collections.defaultdict(list)
        inDegree = [0] * numCourses
        for course in prerequisites:
            courseGraph[course[1]].append(course[0])
        for course in prerequisites:
            if(course[0] == course[1]): return []
            inDegree[course[0]] += 1
        queue = deque([])
        count = 0
        result = []
        for i in range(len(inDegree)):
            if(inDegree[i] == 0): queue.append(i)
        while(queue):
            count += 1
            curr = queue.popleft()
            result.append(curr)
            if(count > numCourses): return []
            for i in courseGraph[curr]:
                inDegree[i] -= 1 
                if(inDegree[i] == 0): queue.append(i)
        if(count < numCourses): return []
        else: return result
                