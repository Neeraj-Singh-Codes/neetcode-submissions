class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        greatest = [0] * n
        right = -1
        for i in range(n-1, -1, -1):
            greatest[i] = right
            right = max(right, arr[i])
        
        return greatest