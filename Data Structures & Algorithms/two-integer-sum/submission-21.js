class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let newM = {}
        let res = 0
        for(let i = 0; i < nums.length; i++){
            res = target - nums[i]
            if(newM.hasOwnProperty(res)){
                return [newM[res], i]
            }else{
                newM[nums[i]] = i
            }
        }
    }
}
