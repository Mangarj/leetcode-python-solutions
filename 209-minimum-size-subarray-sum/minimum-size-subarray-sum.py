class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        ans = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        if ans == float('inf'):
            return 0
        return ans
        