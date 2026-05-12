class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        count = sorted(freq, key=freq.get, reverse=True)
        return count[ : k]































        # freq_dict = {}
        # for i in nums:
        #     if i in freq_dict:
        #         freq_dict[i] += 1
        #     else:
        #         freq_dict[i] = 1
            
        # count = sorted(freq_dict, key=freq_dict.get, reverse=True)
        # return count[ : k]