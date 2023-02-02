class Solution:
    def numberOfWays(self, s: str) -> int:
        result = 0
        def solve(index,zero,one,zeroOne,oneZero):
            nonlocal result
            if(index>=len(s)): return 0
            if(s[index] == "0"):
                result += zeroOne 
                oneZero += one 
                zero += 1
            else:
                result += oneZero 
                zeroOne += zero 
                one += 1
            solve(index+1,zero,one,zeroOne,oneZero)
        solve(0,0,0,0,0)
        return result
