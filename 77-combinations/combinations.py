class Solution:
    def combine(self, n: int, k: int):
        result = []

        def backtrack(start, path):
            # Base case
            if len(path) == k:
                result.append(path[:])
                return
            
            # Explore choices
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # backtrack
        
        backtrack(1, [])
        return result

        