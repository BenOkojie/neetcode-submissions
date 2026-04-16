class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict={}
        for i in range(len(nums)):
            numsdict[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in numsdict and i!=numsdict[target-nums[i]]:
                return [i,numsdict[target-nums[i]]]
        