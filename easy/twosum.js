class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map={}
         
        for (let i =0 ; i<nums.length;i+=1){
            map[nums[i]] = i // sets number to its index in the map
        }
   
        for (let i =0 ; i<nums.length;i+=1){
            let difference = target - nums[i] // identifies the second number that makes 10 and stores it in variable
        if(map[difference]!== undefined && map[difference]!== i){// if the difference is in the map and not the same index as the current number
            return [i,map[difference]]// return the current index and the diff index refering the map instead of the loop
        }
            
        }
        return []
   }
}