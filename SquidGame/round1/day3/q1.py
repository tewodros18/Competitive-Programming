class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                lft, rght = s[left:right], s[left + 1:right + 1]
                return lft == lft[::-1] or rght == rght[::-1]
            left += 1
            right -=1
        return True
