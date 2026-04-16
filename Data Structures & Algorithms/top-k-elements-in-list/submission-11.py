class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numscount={}
        res=[[] for i in range(len(nums)+1)]
        for i in nums:
            if i in numscount:
                numscount[i]+=1
            else:
                numscount[i]=1
        for i in numscount:
            res[numscount[i]].append(i)
        freq = [sub for sub in res if sub]   
        res = []
        for i in freq:
            for j in i:
                res.append(j)
        

        return res[::-1][:k]

            
        