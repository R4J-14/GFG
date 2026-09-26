class Solution:
    def minimumCost(self, x: int, s: int, m: int, l: int, cs: int, cm: int, cl: int) -> int:
        max_area = x + l

        # dp[i] will store the minimum cost to get AT LEAST area i
        dp = [float('inf')] * (max_area + 1)
        dp[0] = 0  # Base case: 0 area costs 0

        pizzas = [(s, cs), (m, cm), (l, cl)]

        # Fill the DP table using the unbounded knapsack approach
        for i in range(1, max_area + 1):
            for area, cost in pizzas:
                if i >= area:
                    dp[i] = min(dp[i], dp[i - area] + cost)

        # Return the minimum cost for any area >= x
        return int(min(dp[x:]))