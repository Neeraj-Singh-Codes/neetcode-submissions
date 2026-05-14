class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newS = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in newS:
                newS.remove(s[l])
                l+=1
            newS.add(s[r])
            res = max(res, r-l+1)
        return res