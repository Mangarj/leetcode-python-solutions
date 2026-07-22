import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:

        # Min heap based on capital
        minCapital = []

        for c, p in zip(capital, profits):
            heapq.heappush(minCapital, (c, p))

        # Max heap based on profit
        maxProfit = []

        for _ in range(k):

            # Push all affordable projects
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)

            # No project can be started
            if not maxProfit:
                break

            # Pick highest profit
            w += -heapq.heappop(maxProfit)

        return w