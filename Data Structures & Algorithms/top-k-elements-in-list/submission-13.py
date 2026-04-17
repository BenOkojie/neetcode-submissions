class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numscount={}
        freq=[[] for i in range(len(nums)+1)]
        res = []
        for i in nums:
            numscount[i] = 1+ numscount.get(i,0)
        for i in numscount:
            freq[numscount[i]].append(i)
        for i in reversed(freq):
            for j in i:
                res.append(j)
                if len(res)==k:
                    return res
        return res

            
        