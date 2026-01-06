class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum_value = sum(nums[:k])
        maximum_sum_value = window_sum_value

        for i in range (k,len(nums)):
            window_sum_value += nums[i]
            window_sum_value -= nums[i-k]

            maximum_sum_value = max(maximum_sum_value,window_sum_value)
        return maximum_sum_value / k
        