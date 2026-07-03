class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // nums.sort((a,b) => a-b )
        // for(let i = 1; i < nums.length; i++){
        //     if( nums[i] === nums [i-1]){
        //         return true
        //     }
        // }
        // return false
        // let newS = new Set()
        // for(let i  = 0; i < nums.length; i++){
        //     if(newS.has(nums[i])){
        //         return true
        //     }else{
        //         newS.add(nums[i])
        //     }
        // }
        // return false

        let newS = new Set(nums)
        if(newS.size === nums.length){
            return false
        }
        return true
    }
}
