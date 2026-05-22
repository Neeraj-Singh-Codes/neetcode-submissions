class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        a = 0
        newS = set()
        for b in range(len(s)):
            while s[b] in newS:
                newS.remove(s[a])
                a += 1
            newS.add(s[b])
            res = max(res, b-a+1)
            
        return res
            
