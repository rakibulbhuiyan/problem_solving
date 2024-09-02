class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # buy=prices[0]
        n=len(prices)
        # profit=0
        # for sell in prices:
        #     if buy<sell:             
        #         profit +=sell-buy
        #         print(f'profit: {profit}')  
        #     buy=sell 
        #     print(f'buy: {buy}')
        # return profit
        profit=0
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                profit +=(prices[i]-prices[i-1])
        return profit
prices =[7,6,4,3,1]
res=Solution()
ans=res.maxProfit(prices)
print(f'ans: {ans}')