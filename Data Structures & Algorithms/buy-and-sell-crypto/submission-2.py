class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix=[]
        n = len(prices)
        suffix = [0 for i in range(n)]
        for i in range(len(prices)):
            if not prefix:
                prefix.append(prices[i])
                suffix[-1]= prices[-1]
            else:
                prefix.append(min(prices[i],prefix[i-1]))
                suffix[(i*-1)-1]= max(prices[(i*-1)-1], suffix[(i*-1)])
        maxp = 0
        for i in range(len(prices)-1):
            p = suffix[i+1]-prices[i]
            if p> maxp:
                maxp=p
        return maxp

        