class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            elif i in s:
                return True
        return False