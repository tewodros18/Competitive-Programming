class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def backtrack(index,curr):
            if(index >= len(s)):
                result.append(''.join(curr))
                return
            if(s[index].isalpha()):
                curr.append(s[index].upper())
                backtrack(index+1,curr)
                curr.pop()
                curr.append(s[index].lower())
                backtrack(index+1,curr)
                curr.pop()
            else:
                curr.append(s[index])
                backtrack(index+1,curr)
                curr.pop()
        backtrack(0,[])
        return result

