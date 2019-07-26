class Solution:
    # k == 1
    def maxProfit1(self, prices) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 1)]
        dp[0] = [float('-inf'), 0]
        for i in range(len(prices)):
            i = i + 1
            dp[i][0] = max(dp[i - 1][0], -prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i - 1])
        return dp[-1][1]

    # k == 'inf'
    def maxProfit2(self, prices):
        # length = len(prices)
        # result = 0
        # for i in range(length-1):
        #     if prices[i+1] > prices[i]:
        #         result += prices[i+1] - prices[i]
        # return result
        dp = [[0, 0] for _ in range(len(prices) + 1)]
        dp[0] = [float('-inf'), 0]
        for i in range(len(prices)):
            i = i + 1
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i - 1])
        return dp[-1][1]

    # k == 2
    def maxProfit3(self, prices) -> int:
        dp = [[[0, 0] for _ in range(len(prices) + 1)], [[0, 0] for _ in range(len(prices) + 1)]]
        dp[0][0] = [float('-inf'), 0]
        dp[1][0] = [float('-inf'), 0]
        for i in range(len(prices)):
            i = i + 1
            dp[0][i][0] = max(dp[0][i - 1][0], -prices[i - 1])
            dp[0][i][1] = max(dp[0][i - 1][1], dp[0][i - 1][0] + prices[i - 1])
            dp[1][i][0] = max(dp[1][i - 1][0], dp[0][i - 1][1] - prices[i - 1])
            dp[1][i][1] = max(dp[1][i - 1][1], dp[1][i - 1][0] + prices[i - 1])
        return dp[1][-1][1]

    # k == any value
    def maxProfit4(self, k, prices):
        # [k][days][has，nothing]
        if len(prices) <= 1 or k == 0:
            return 0
        if k >= len(prices) // 2:
            dp = [[0, 0] for _ in range(len(prices)+1)]
            dp[0][0] = float('-inf')
            dp[0][1] = 0
            for i in range(len(prices)):
                i = i+1
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i - 1])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i - 1])
            return dp[-1][1]
        else:
            dp = [[[0, 0] for _ in range(len(prices)+1)] for i in range(k)]
            for i in range(k):
                dp[i][0][0] = float('-inf')
                dp[i][0][1] = 0
            for j in range(k):
                if j == 0:
                    for i in range(len(prices)):
                        i = i + 1
                        dp[j][i][0] = max(dp[j][i - 1][0], -prices[i - 1])
                        dp[j][i][1] = max(dp[j][i - 1][1], dp[j][i - 1][0] + prices[i - 1])
                else:
                    for i in range(len(prices)):
                        i = i + 1
                        dp[j][i][0] = max(dp[j][i-1][0], dp[j-1][i-1][1] - prices[i-1])
                        dp[j][i][1] = max(dp[j][i-1][1], dp[j][i-1][0] + prices[i-1])
            print(dp)
            return dp[-1][-1][1]


if __name__ == '__main__':
    s = Solution()
    a = [3,3,5,0,0,3,1,4]
    b = [1,2,3,4,5,6]
    c = [3,2,6,5,0,9]
    print(s.maxProfit4(1, c))
