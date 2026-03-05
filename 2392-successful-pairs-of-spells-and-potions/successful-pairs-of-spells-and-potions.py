class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        result = []
        m = len(potions)

        for spell in spells:
            min_potion = (success + spell - 1) // spell
            idx = bisect_left(potions, min_potion)
            result.append(m - idx)

        return result