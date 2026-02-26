import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        
        n = len(costs)
        heap = []
        
        left = 0
        right = n - 1
        
        total_cost = 0
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(heap, (costs[left], 0))
                left += 1
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(heap, (costs[right], 1))
                right -= 1
        for _ in range(k):
            cost, side = heapq.heappop(heap)
            total_cost += cost
            if left <= right:
                if side == 0:
                    heapq.heappush(heap, (costs[left], 0))
                    left += 1
                else:
                    heapq.heappush(heap, (costs[right], 1))
                    right -= 1
        
        return total_cost
        