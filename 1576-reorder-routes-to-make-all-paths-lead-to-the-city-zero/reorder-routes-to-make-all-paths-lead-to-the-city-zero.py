class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        # build graph
        for a, b in connections:
            graph[a].append((b, 1))  # wrong direction
            graph[b].append((a, 0))  # correct direction

        visited = set()

        def dfs(city):
            visited.add(city)
            changes = 0

            for nei, cost in graph[city]:
                if nei not in visited:
                    changes += cost
                    changes += dfs(nei)

            return changes

        return dfs(0)
        