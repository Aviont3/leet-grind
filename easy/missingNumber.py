class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        r = len(nums)
        print(nums)
        for i in range(len(nums)):
           r += i - nums[i]
          '''
           Walkthrough
use nums = [3, 0, 1]:

Initial: r = 3 (length of array)
i=0: r += 0 - 3 → r = 3 + 0 - 3 = 0
i=1: r += 1 - 0 → r = 0 + 1 - 0 = 1
i=2: r += 2 - 1 → r = 1 + 2 - 1 = 2
Result: 2 is missing ✓

Why It Works
The key insight: we're calculating n + (0 + 1 + 2 + ... + n) - (sum of all numbers in array)

We start with n
We add all indices: 0, 1, 2, ..., n-1
We subtract all values in the array
What remains is the missing number!
          '''
        return r
          
                
      




            


        
        
