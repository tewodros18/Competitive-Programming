class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def recures(index):
            if(index >= len(nums)):
                return 0
            if(dp[index] != -1): return dp[index]
            dp[index] = max(nums[index] + recures(index + 2) , + recures(index+1))
            return dp[index]
        return recures(0)