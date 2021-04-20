"""
Best Time to Buy and Sell Stock II, https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

class Solution(object):

    def is_low_point(self, idx, prices):
        N = len(prices)
        lower_left = idx==0 or prices[idx]<=prices[idx-1]
        lower_right = idx==N-1 or prices[idx]<=prices[idx+1]
        return lower_left and lower_right


    def is_high_point(self, idx, prices):
        N = len(prices)
        higher_left = idx==0 or prices[idx]>=prices[idx-1]
        higher_right = idx==N-1 or prices[idx]>=prices[idx+1]
        return higher_left and higher_right and idx != 0


    def maxProfit(self, prices):
        res = 0
        buy, sell = float('inf'), 0
        if len(prices) <= 1:
            return 0
        else:
            N = len(prices)
            for i in range(len(prices)):
                if self.is_low_point(i, prices):
                    buy = min(prices[i], buy)
                if self.is_high_point(i, prices):
                    sell = prices[i]
                    res = max(sell-buy, res)
            return res


def main():
    prices = [7,1,5,3,6,4]
    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)


if __name__ == '__main__':
    main()
