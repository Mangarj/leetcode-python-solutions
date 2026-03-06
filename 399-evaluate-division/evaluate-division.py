class Solution:
    def calcEquation(self, equations, values, queries):
        
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1/value))
        def dfs(start, end, visited):
            if start not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for neighbor, val in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1:
                        return result * val
            
            return -1.0
        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, set()))
        
        return ans
        