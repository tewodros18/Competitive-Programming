class Solution:
    def maxCoins(self, piles):
        piles.sort()
        B = 0
        A = len(piles) - 1
        M = A - 1
        count = 0
        while(len(piles)>=3):
            count+=piles[M]
            print(piles[M])
            piles.pop()
            piles.pop()
            piles.pop(0)
            A-=3
            M-=3
        return count
Solution().maxCoins([2,4,1,2,7,8])