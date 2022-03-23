class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lft, rit, ans = 0, len(people) - 1, 0
        while lft <= rit:
            if people[lft] + people[rit] <= limit:
                lft += 1
            ans += 1
            rit -= 1   
        return ans