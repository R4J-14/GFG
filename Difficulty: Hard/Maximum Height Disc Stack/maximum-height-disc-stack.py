class Solution:
    def maxStackHeight(self, r, h):
        # Pair radius and height together
        discs = list(zip(r, h))

        # Sort by radius ascending; if radii are equal, sort by height descending
        # Descending height prevents picking two discs of identical radius
        discs.sort(key=lambda x: (x[0], -x[1]))

        max_h = max(h) if h else 1000

        # Fenwick Tree (Binary Indexed Tree) for O(log(MAX_H)) range maximum queries
        tree = [0] * (max_h + 1)

        def update(idx, val):
            while idx <= max_h:
                if val > tree[idx]:
                    tree[idx] = val
                idx += idx & -idx

        def query(idx):
            max_val = 0
            while idx > 0:
                if tree[idx] > max_val:
                    max_val = tree[idx]
                idx -= idx & -idx
            return max_val

        ans = 0
        for radius, height in discs:
            # Query the best stack height achievable with strictly smaller height
            best_prev = query(height - 1)
            current_stack = best_prev + height

            ans = max(ans, current_stack)
            update(height, current_stack)

        return ans