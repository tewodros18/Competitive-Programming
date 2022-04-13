class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        stack = []
        for i in num:
            while(len(stack) > 0 and k > 0 and stack[-1] > i ):
                stack.pop()
                k -=1
            stack.append(i)
        if(k>0): stack = stack[:-k]
        return "0" if len(stack) == 0 else str(int(''.join(stack)))
        """