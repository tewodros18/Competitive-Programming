class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def BubbleSort(A_list):
            length_of_list = len(A_list)
            while(True):
                swapped = False
                for i in range(1,length_of_list):
                    if(A_list[i-1] > A_list[i]):
                        (A_list[i-1],A_list[i]) = (A_list[i],A_list[i-1])
                        swapped = True
                if(not swapped):
                    break
            return (A_list)          
        nums = BubbleSort(nums)
        result = []
        count=0
        for i in nums:
            if i == target:
                result.append(count)
            count+=1
        return result
        