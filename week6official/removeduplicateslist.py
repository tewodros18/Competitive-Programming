class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lft =0
        rgt = 0
        while(rgt <= len(nums) - 1):
            if(nums[lft] == nums[rgt]):
                rgt+=1
            else:
                nums[lft+1] = nums[rgt]
                lft+=1
        return lft+1