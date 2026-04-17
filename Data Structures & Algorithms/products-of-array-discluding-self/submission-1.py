class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =[]
        postfix= [1 for i in range(len(nums))]
        res=[]
        precount = postcount=1
        for i in range(len(nums)):
            precount*=nums[i]
            postcount*=nums[len(nums)-i-1]
            prefix.append(precount)
            postfix[len(nums)-i-1] = postcount
        print(postfix)
        print(prefix)
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i+1])
            elif i == len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(postfix[i+1]*prefix[i-1])
        return res
