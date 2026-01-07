class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_side_window = 0
        zero_count = 0
        maximum_len = 0

        for right in range (len(nums)):
            if nums[right] == 0:
                zero_count +=1

            while zero_count > 1:
                if nums[left_side_window] == 0:
                    zero_count -=1
                left_side_window +=1

            maximum_len = max(maximum_len,right-left_side_window)

        return maximum_len
                        