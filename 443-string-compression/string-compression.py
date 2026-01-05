class Solution:
    def compress(self, chars: List[str]) -> int:
        number_of_chars = len(chars)
        if number_of_chars < 2:
            return number_of_chars

        i = 0  # read pointer
        j = 0  # write pointer

        while i < number_of_chars:
            cur = chars[i]   
            count = 0

            while i < number_of_chars and chars[i] == cur:
                i += 1
                count += 1

            chars[j] = cur 
            j += 1

            if count > 1:
                for val in str(count):
                    chars[j] = val
                    j += 1

        return j

        