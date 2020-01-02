class Solution(object):
    # houses on a line
    def robber1(self, houses):
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]
        if len(houses) == 2:
            return max(houses[0], houses[1])

        dp = [0 for _ in range(len(houses))]
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        for i in range(2, len(houses)):
            dp[i] = max(dp[i-2] + houses[i], dp[i-1])
        return dp[-1]

    # houses on a circle
    def robber2(self, houses):
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]
        if len(houses) == 2:
            return max(houses[0], houses[1])
        return max(self.robber1(houses[:-1]), self.robber1(houses[1:]))


l = [2,7,9,3,9]
a = Solution()
print(a.robber2(l))
