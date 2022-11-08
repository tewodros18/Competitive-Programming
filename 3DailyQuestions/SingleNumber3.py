class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num = 0
        for i in nums:
            num ^= i
        setBit = 0
        for i in range(32):
            if(num & (1 << i) != 0): setBit = i
        num2 = 0
        for i in nums:
            if(i & (1 << setBit) != 0):
                num2 ^= i
        return [num2,num^num2]
