class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newS = set()
        count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in newS:
                newS.remove(s[l])
                l += 1
            newS.add(s[r])

            count = max(count, r-l+1)
        return count
        
        