class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maximum = 0
        while right < len(prices):
            curr = 0
            if prices[left] <= prices[right]:
                curr = prices[right] - prices[left]
                right += 1
            else:
                left = right
                right += 1
            maximum = max(curr, maximum)
        return maximum