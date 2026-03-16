from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            count = 0
            seen = {}

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        result.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return result
        