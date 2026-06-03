# Set maxProfit = 0
# we can have a left and right pointer which represents the index of the array prices
# if prices[right] > prices[left], then we can compute the difference and store it in the
# variable called profit
# and then compute the max profit using max(maxProfit, profit) 
# else make the left pointer equal to right, and increment right pointer by 1
# Time complexity is O(n), space complexity is O(1)
# len(prices) = 6
# then r is going to be up to 5

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while(r < len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
            

        