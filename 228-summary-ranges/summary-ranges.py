class Solution:
    def summaryRanges(self, nums):
        result = []
        
        for i in range(len(nums)):
            # start of range
            if i == 0 or nums[i] != nums[i - 1] + 1:
                start = nums[i]
            
            # end of range
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                end = nums[i]
                
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
        
        return result
        