from collections import deque

class Solution:
    def areAnagrams(self, root1, root2):
        # Base edge cases
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            n1 = len(q1)
            n2 = len(q2)

            # If current level sizes don't match, they can't be anagrams
            if n1 != n2:
                return False

            level1 = []
            level2 = []

            # Extract current level elements for tree 1
            for _ in range(n1):
                node = q1.popleft()
                level1.append(node.data)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)

            # Extract current level elements for tree 2
            for _ in range(n2):
                node = q2.popleft()
                level2.append(node.data)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            # Check if sorted level elements are equal
            level1.sort()
            level2.sort()
            if level1 != level2:
                return False

        # Return True if both trees ended at the same depth
        return len(q1) == 0 and len(q2) == 0