def isValid(s):
        stack = []
        opening = '({['
        closing = ']})'
        for i in s:
            if(i in opening):
                stack.append(i)
            elif(i in closing):
                if(len(stack)==0):
                    return False
                if(i == ')' and stack[-1] == '(' ):
                    stack.pop()
                elif(i == ']' and stack[-1] == '[' ):
                    stack.pop()
                elif(i == '}' and stack[-1] == '{' ):
                    stack.pop()
        if(len(stack) == 0):
            return True 
        else:
            return False 
print(isValid('}(){}'))
