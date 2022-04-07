class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        nums.append(-inf)
        stk = [-1]
        minSums = 0
        for i in range(len(nums)):
            while stk[-1] != -1 and nums[i] < nums[stk[-1]]:
                #print((nums[i], nums[stk[-1]]))
                idx = stk.pop()
                minSums+= (nums[idx] * (i-idx) * (idx-stk[-1]))
            
            stk.append(i)
        
        nums.remove(-inf)
        nums.append(inf)
        stk = [-1]
        maxSums = 0
        for i in range(len(nums)):
            while stk[-1] != -1 and nums[i] > nums[stk[-1]]:
                idx = stk.pop()
                maxSums+= (nums[idx] * (i-idx) * (idx-stk[-1]))
            
            stk.append(i)
        
        return maxSums - minSums
