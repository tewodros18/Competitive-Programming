class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = []
        rightsum = []
        for i in range(len(nums)):
            if i == 0:
                leftsum.append(nums[i])
            else:
                leftsum.append(leftsum[i-1]+nums[i])
        nums.reverse()
        for i in range(len(nums)):
            if i == 0:
                rightsum.append(nums[i])
            else:
                rightsum.append(rightsum[i-1]+nums[i])
        rightsum.reverse()
        for i in range(len(leftsum)):
            if(leftsum[i] == rightsum[i]):
                return i
        return -1