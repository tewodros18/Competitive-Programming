class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        Count = Counter(nums)
        answer = set()
        quantity.sort(reverse=True)
        def backtrack(index,answer):
            if(index >= len(quantity)):
                #answer.add(True)
                return True
            for unique in Count:
                if(Count[unique] - quantity[index] >= 0):
                    Count[unique] -= quantity[index]
                    ans = backtrack(index + 1,answer)
                    if(ans): return True
                    Count[unique] += quantity[index]
            return False
        
        return backtrack(0,answer)
