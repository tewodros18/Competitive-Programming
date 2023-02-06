class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        L = len(pref)
        answer = 0
        for w in words:
            if(pref == w[:L]): answer += 1
        return answer
