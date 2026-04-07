class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for  i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            if i not in freq_dict:
                freq_dict[i] = 1
        
        # keys = list(freq_dict)
        keys = sorted(freq_dict, key=freq_dict.get, reverse=True)
        return keys[ : k]

        