class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=set("AEIOUaeiou")
        start_index=0
        end_index=len(s)-1
        arr=list(s)
        while start_index < end_index:
            if arr[start_index] not in vowel:
                start_index +=1
            elif arr[end_index] not in vowel:
                end_index -=1
            else:
                arr[start_index],arr[end_index]=arr[end_index],arr[start_index]
                start_index +=1
                end_index -=1
            
        result="".join(arr)
        return result
        