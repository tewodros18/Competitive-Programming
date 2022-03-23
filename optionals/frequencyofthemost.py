def maxFrequency(nums,k):
        nums.sort()
        left = len(nums) -1
        right = len(nums) - 1
        tempk = k
        result = [0] * len(nums)
        while(right>0):
            #print(nums[right]-nums[left])
            if(tempk >= (nums[right]-nums[left])):
                result[right]+=1
                tempk-=right-left
                if(left!=0):
                    left-=1
                else:
                    tempk = -1
            else:
                right -=1
                left = right
                tempk = k
        if len(result) == 1:
            return 1
        result.sort()
        return result[-1]
print(maxFrequency([9940,9995,9944,9937,9941,9952,9907,9952,9987,9964,9940,9914,9941,9933,9912,9934,9980,9907,9980,9944,9910,9997]
,7925))