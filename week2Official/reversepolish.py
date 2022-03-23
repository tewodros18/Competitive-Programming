def evalRPN(tokens):
        stack = []
        operators = '+-*/'
        stackop = []
        for i in tokens:
            if(i not in operators):
                stack.append(int(i))
            if(i in operators):
                stackop.append(str(i))
                #a = stack.pop()
                #b = stack.pop()
                #stack.append(round(eval(str(a) + i + str(b))))
        while(len(stack) != 1):
            a = stack.pop()
            b = stack.pop()
            print(str(b) + stackop[0] + str(a))
            stack.append((eval(str(b) + stackop[0] + str(a)))//1)
            stackop.pop(0)
        return stack
print(evalRPN(["2","1","+","3","*"]))