class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        result = []
        count=0
        for i in nums:
            if i == target:
                result.append(count)
            count+=1
        return result
        