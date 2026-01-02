class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_value=float('inf')
        secand_value=float('inf')
        for number in nums:
            if number <= first_value:
                first_value=number
            elif number <= secand_value:
                secand_value=number
            else:
                return True
        return False
        