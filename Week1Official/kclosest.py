class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Since heap is sorted in increasing order,
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of 
        heap = [self.distance(points[i]) for i in range(k)]
        heapq.heapfiy(heap)
        for i in range(k,len(points)):
            distance = -self.distance(points[i])
            if (distance > heap[0][0]):
                heapq.heappushpop(heap, (distance,i))
            
        return [points[i] for (_,i) in heap ]
    def distance(a:list)->int:
        return a[0]**2 + a[1]**2
    