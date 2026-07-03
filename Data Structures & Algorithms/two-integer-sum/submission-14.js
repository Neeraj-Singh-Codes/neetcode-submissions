class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let newS = new Set()
        let res = 0
        for(let i = 0; i < nums.length; i++){
            res = target - nums[i]
            if(newS.has(res)){
                return [nums.indexOf(res), i]
            }
            if(!newS.has(nums[i])){
                newS.add(nums[i])
            }
        }
    }
}
