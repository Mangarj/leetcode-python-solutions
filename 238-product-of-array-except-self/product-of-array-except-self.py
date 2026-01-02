class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[1]*length
        for i in range(1,length):
            result[i]=result[i-1]*nums[i-1]
        right_to_left_value=1
        for i in range(length-1,-1,-1):
            result[i]=result[i] * right_to_left_value
            right_to_left_value=right_to_left_value * nums[i]
        return result

        