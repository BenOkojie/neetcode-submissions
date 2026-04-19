class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        start=0
        longest = 0
        for i in numset:
            if i-1 not in nums:
                length=1
                while i+length in numset:
                    length+=1
                if length>longest:
                    longest=length
                    start=i
        return longest

