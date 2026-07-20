from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slope = defaultdict(int)

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    g = gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g

                    # Normalize sign
                    if dx < 0:
                        dx *= -1
                        dy *= -1

                slope[(dy, dx)] += 1
                ans = max(ans, slope[(dy, dx)] + 1)

        return ans
        