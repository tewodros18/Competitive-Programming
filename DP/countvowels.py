class Solution:
    answer = 0
    def countVowels(self, word: str) -> int:
        Sets = {'a','e','i','o','u'}
        count = 0
        for i in range(len(word)):
            if(word[i] in Sets):
                count += (len(word) - i)*(i + 1)
        return count