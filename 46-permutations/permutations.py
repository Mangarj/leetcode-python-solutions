class Solution:
    def permute(self, nums):
        result = []
        
        def backtrack(path, used):
            # base case
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # choose
                path.append(nums[i])
                used[i] = True
                
                # explore
                backtrack(path, used)
                
                # un-choose (backtrack)
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return result
        