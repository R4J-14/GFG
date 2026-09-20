class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)
        if n == 0:
            return 0

        hor = [[0] * n for _ in range(n)]
        ver = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if mat[i][j] == 'X':
                    hor[i][j] = 1 if j == 0 else hor[i][j - 1] + 1
                    ver[i][j] = 1 if i == 0 else ver[i - 1][j] + 1

        max_size = 0

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                side = min(hor[i][j], ver[i][j])
                while side > max_size:
                    if hor[i - side + 1][j] >= side and ver[i][j - side + 1] >= side:
                        max_size = side
                        break
                    side -= 1

        return max_size