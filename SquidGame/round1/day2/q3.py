class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        for i in logs:
            temp = i.split(" ")
            if(temp[1].isdigit()):
                digits.append(i)
            else:
                letters.append(temp)
        letters.sort(key=lambda x:[x[1:],x[:1]])
        answer = [" ".join(i) for i in letters]
        return answer + digits
        
