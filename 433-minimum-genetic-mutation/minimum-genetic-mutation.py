from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        
        # If endGene is not in bank, no solution
        if endGene not in bank_set:
            return -1
        
        queue = deque()
        queue.append((startGene, 0))  # (current_gene, steps)
        
        genes = ['A', 'C', 'G', 'T']
        visited = set()
        visited.add(startGene)
        
        while queue:
            current, steps = queue.popleft()
            
            if current == endGene:
                return steps
            
            # Try all possible mutations
            for i in range(len(current)):
                for g in genes:
                    mutated = current[:i] + g + current[i+1:]
                    
                    if mutated in bank_set and mutated not in visited:
                        visited.add(mutated)
                        queue.append((mutated, steps + 1))
        
        return -1
        