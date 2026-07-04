class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let newM = new Map()
        for(let i = 0; i < strs.length; i++){
            let alphabets = new Array(26).fill(0)
            for(let c of strs[i]){
                alphabets[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
            }
            let key = alphabets.join(',')
            if(!newM[key]){
                newM[key] = []
            }
            newM[key].push(strs[i])
        }
        return Object.values(newM)
    }
}
