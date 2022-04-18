class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = [0] * len(prices)
        for i in range(len(prices) - 1,-1, -1):
            if(i+1<len(prices) and prices[i] - 1 == prices[i+1]):
                result[i] += result[i+1]
            result[i] +=1
        return sum(result)