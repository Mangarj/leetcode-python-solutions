class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_map = Counter(tuple(row) for row in grid)
        result = 0
        for c in range(n):
            column = tuple(grid[r][c] for r in range(n))
            result += row_map[column]

        return result

        