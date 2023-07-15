class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        b=prices[0]
        for i in range(1,len(prices)):
            x=prices[i]-b
            m=max(x,m)
            b=min(prices[i],b)
        return m
            
        