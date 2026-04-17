class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numscount={}
        freq=[[] for i in range(len(nums)+1)]
        res = []
        for i in nums:
            if i in numscount:
                numscount[i]+=1
            else:
                numscount[i]=1
        for i in numscount:
            freq[numscount[i]].append(i)
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
       

        return res

            
        