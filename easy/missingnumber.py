class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #sum add the range of the 1 the lenght of nums(which give the sum with the missing number add) - the sum of nums without the missing number the difference give you the missing number
        
        return sum(range(1,len(nums)+1)) - sum(nums)
