def checkArithmeticSubarrays(nums, l, r):
        ranges = []
        for i in range(len(l)):
            a = nums[l[i]:(r[i]+1)]
            a.sort()
            ranges.append(a)
        answer = [True] * len(ranges)
        print(ranges)
        for i in range(len(ranges)):
            for j in range(len(ranges[i])-1):
                var = ranges[i][1] - ranges[i][0]
                print(ranges[i][j+1] - ranges[i][j])
                if(ranges[i][j+1] - ranges[i][j] != var):
                    answer[i] = False
                    break
        return answer
print(checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5]))