class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            # if all characters matched
            if index == len(word):
                return True
            
            # boundary + mismatch check
            if (r < 0 or c < 0 or r >= rows or c >= cols 
                or board[r][c] != word[index]):
                return False
            
            # mark visited
            temp = board[r][c]
            board[r][c] = "#"
            
            # explore all 4 directions
            found = (
                dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1)
            )
            
            # backtrack
            board[r][c] = temp
            
            return found

        # start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False
        