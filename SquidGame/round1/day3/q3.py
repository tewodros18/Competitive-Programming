class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i-1]
        
    def pickIndex(self) -> int:
        rand = random.randint(1, self.w[-1])
        left, right = 0, len(self.w) - 1
        
        while left < right:
            mid = (left + right) // 2
            if self.w[mid] >= rand:
                right = mid
            else:
                left = mid + 1
            
        return left
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
