class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        for index in range(len(flowerbed)):
            if flowerbed[index]==0:
                left=(index==0 or flowerbed[index-1]==0)
                right=(index==len(flowerbed)-1 or flowerbed[index+1]==0)

                if left and right:
                    flowerbed[index]=1
                    n-=1
                    if n==0:
                        return True
        return False
        