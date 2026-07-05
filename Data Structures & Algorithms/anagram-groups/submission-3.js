class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let anagrams = new Map()
        for(let i = 0; i < strs.length; i++){
            const alphabets = new Array(26).fill(0)
            for(let char of strs[i]){
                alphabets[char.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
            }
            let key = alphabets.join(',')
            if(!anagrams[key]){
                anagrams[key] = []
            }
            anagrams[key].push(strs[i])
        }
        return Object.values(anagrams)
    }
}
