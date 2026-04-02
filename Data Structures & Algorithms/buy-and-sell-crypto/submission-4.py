class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=0
        l=0
        r=1
        for r in range(len(prices)):
            if prices[l]<prices[r]:
                difference=prices[r]-prices[l]
                maximum=max(difference,maximum)
            else:
                l=r

        return maximum





        