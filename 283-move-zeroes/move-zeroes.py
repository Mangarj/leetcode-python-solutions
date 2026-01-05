class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_point=0
        for i in range (len(nums)):
                  if nums[i] != 0:
                    nums[non_zero_point]=nums[i]
                    non_zero_point+=1
        while non_zero_point<len(nums):
            nums[non_zero_point]=0
            non_zero_point+=1
        