class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        suffix = [0 for i in range(n)]
        for i in range(len(prices)):
            if not suffix:
                suffix[-1]= prices[-1]
            else:
                suffix[(i*-1)-1]= max(prices[(i*-1)-1], suffix[(i*-1)])
        maxp = 0
        for i in range(len(prices)-1):
            p = suffix[i+1]-prices[i]
            if p> maxp:
                maxp=p
        return maxp

        