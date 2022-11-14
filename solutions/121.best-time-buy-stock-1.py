class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=len(prices)-1
        max_high=0
        max_low=1000000
        max_profits=0
        counter=0
        while left<right:
            current_diff = prices[right]-prices[left]
            if current_diff>max_profits:
                max_profits = current_diff
            print(left,right)
            if max_high<prices[right]:
                right-=1
        return max_profits
            
            
            
        