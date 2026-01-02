class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        set_nums= set(nums)

        res = []
        for i in range(min(nums),max(nums)):
            if i not in set_nums:
                res.append(i)
            
        return res
