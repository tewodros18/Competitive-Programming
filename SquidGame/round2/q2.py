class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = defaultdict(int)
        words.sort(key=lambda x:len(x))
        for word in words:
            temp = []
            for i in range(len(word)):
                temp.append(memo[word[:i] + word[i+1:]] + 1)
            memo[word] = max(temp)
        return max(memo.values())
