class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let freq = new Map()
        for(let i = 0; i < nums.length; i++){
            if(freq.has(nums[i])){
                freq.set(nums[i], freq.get(nums[i]) + 1)
            }else{
                freq.set(nums[i], 1)
            }
        }
            const sorted_freq = new Map([...freq].sort((a,b) => b[1] - a[1]))

        return Array.from(sorted_freq.keys()).slice(0,k);
    }
}
