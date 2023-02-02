class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapify(nums)
        Sum = sum(nums)
        ans = 0
        while(nums and Sum > 0):
            curr = heappop(nums)
            if(curr == 0):
                continue
            for i in range(len(nums)):
                if(nums[i] > 0 and curr > 0): 
                    nums[i] -= curr
                    Sum -= curr
            ans += 1
        return ans
