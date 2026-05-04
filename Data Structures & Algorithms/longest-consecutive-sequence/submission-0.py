class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        seq = 0
        count = 0
        for i in S:
            if (i-1) not in S:
                count = 1
                while (i + count) in S:
                    count += 1

                seq = max(count, seq)
        return seq
        
        