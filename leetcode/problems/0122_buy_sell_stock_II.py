"""
Best Time to Buy and Sell Stock II, https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

class Solution(object):
    def maxProfit(self, prices):
        high, low = -1, -1
        i, N = 0, len(prices)
        res = 0
        while(i < N-1):
            while(i < N-1 and prices[i]>=prices[i+1]):
                i += 1
            low = prices[i]
            while (i < N-1 and prices[i]<=prices[i+1]):
                i += 1
            high = prices[i]
            res += (high - low)
        return res 


def main():
    prices = [7,1,5,3,6,4]
    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)


if __name__ == '__main__':
    main()
