class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set("aeiou")
        count_current=0
        
        for i in range (k):
            if s[i] in vowels:
                count_current +=1

            maximum_vowles=count_current

        for i in range(k , len(s)):
             if s[i] in vowels:
                 count_current +=1
                
             if s[i-k] in vowels:
                count_current -=1

             maximum_vowles = max(maximum_vowles,count_current)
        return maximum_vowles
            
                

        