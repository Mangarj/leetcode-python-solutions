class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        
        while a > 0 or b > 0 or c > 0:
            bitA = a & 1
            bitB = b & 1
            bitC = c & 1
            
            if bitC == 1:
                if bitA == 0 and bitB == 0:
                    flips += 1
            else:
                flips += bitA + bitB
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips
        