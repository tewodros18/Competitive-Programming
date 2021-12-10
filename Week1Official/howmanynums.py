class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        count = 0
        for i in nums:
            for j in nums:
                if j < i:
                    result[count] += 1
            count+=1
        return result