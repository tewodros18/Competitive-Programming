#referse digit
class Solution(object):
    def reverse(x):
        reverse = ""
        if x < 0:
            reverse = reverse + "-"
            x = -x
        if x == 0:
            return 0
        while(x!=0):
            reverse += str(x%10)
            x = x // 10
        if (int(reverse) > 2**31 - 1) or (int(reverse) < -2**31) :
            reverse = 0
        return(int(reverse))
