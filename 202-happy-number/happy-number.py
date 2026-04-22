class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getSum(n)
        
        return n == 1
    
    def getSum(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total