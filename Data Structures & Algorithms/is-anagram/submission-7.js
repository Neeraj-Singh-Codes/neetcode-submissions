class Solution {
    isAnagram(s, t) {
        if(s.length != t.length){
            return false
        }
        let newS = {}
        let newBool = true
        for(let str of s){
            if(str in newS){
                newS[str] += 1
            }else{
                newS[str] = 1
            }
        }
        for(let str of t){
            if(str in newS){
                newS[str] -= 1
            }
        }
        for(let key in newS){
            if(newS.hasOwnProperty(key)){
                if(newS[key] > 0){
                    return false
                }else{
                    newBool = true
                }
            }
        }
        return newBool
    }
}
