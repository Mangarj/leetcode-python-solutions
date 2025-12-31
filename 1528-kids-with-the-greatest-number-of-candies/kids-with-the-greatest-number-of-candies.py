class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greates_kids=max(candies)
        result=[]
        for number in candies:
            if number+extraCandies >= greates_kids:
                result.append(True)
            else:
                result.append(False)
        return result
            
        