class Solution:
    def formPyramid(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        left = [0] * n
        right = [0] * n

        # Left pass
        left[0] = min(arr[0], 1)
        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)

        # Right pass
        right[n - 1] = min(arr[n - 1], 1)
        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)

        # Calculate maximum pyramid area (h * h)
        max_pyramid_sum = 0
        for i in range(n):
            h = min(left[i], right[i])
            max_pyramid_sum = max(max_pyramid_sum, h * h)

        return sum(arr) - max_pyramid_sum