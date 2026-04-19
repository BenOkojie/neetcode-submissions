class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        res = {}
        nums=sorted(nums)
        while i < len(nums):
            if i and nums[i]==nums[i-1]:
                i+=1
                continue
            target = nums[i]*-1
            l= i+1
            r=len(nums)-1
            while l<r:
                cur = nums[l]+nums[r]
                if cur==target:
                    indx= [nums[i],nums[l],nums[r]]
                    if i not in res:
                        res[tuple(indx)] = 1
                    l+=1
                elif cur>target:
                    r-=1
                elif cur<target:
                    l+=1
            i+=1
        result = list(res)
        
        return result
        