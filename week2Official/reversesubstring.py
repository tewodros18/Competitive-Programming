class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if(i != ')'):
                stack.append(i)
            if(i == ')'):
                result = ''
                while(True):
                    if(stack[-1]=='('):
                        stack.pop()
                        stack.append(result[::-1])
                        break
                        
                    else:
                        result = stack.pop() + result
        return ''.join(stack)
                        
            