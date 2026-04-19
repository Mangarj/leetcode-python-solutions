from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))  # sorted key
            res[key].append(word)
        
        return list(res.values())
        