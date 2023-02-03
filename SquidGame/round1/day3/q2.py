class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        temp = [i for i in path if i != ""]
        stack = ["/"]
        print(temp)
        for i in temp:
            if(i == ".." and len(stack) >= 2):
                stack.pop()
            elif(i == "." or i == ".."):
                continue
            else:
                stack.append(i)
        return "/" + "/".join(stack[1:])
