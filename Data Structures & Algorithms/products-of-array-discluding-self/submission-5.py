class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prearr = [0] * n
        postarr = [0] * n
        resarr = [0] * n

        prearr[0] = postarr[n-1] = 1
        for i in range(1, n):
            prearr[i] = nums[i-1] * prearr[i-1]
        for i in range(n-2, -1, -1):
            postarr[i] = nums[i+1] * postarr[i+1]

        for i in range(n):
            resarr[i] = prearr[i] * postarr[i]

        return resarr

        




        