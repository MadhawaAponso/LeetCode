from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        new_l = []
        l = {}  
        unique_counts = {}  
        unique_count = 0

        for idx, val in queries:
            prev_val = l.get(idx, 0)  
            if prev_val != 0:
                unique_counts[prev_val] -= 1
                if unique_counts[prev_val] == 0:
                    unique_count -= 1
            l[idx] = val  
            
            if val != 0:
                if val not in unique_counts or unique_counts[val] == 0:
                    unique_count += 1
                unique_counts[val] = unique_counts.get(val, 0) + 1
            
            new_l.append(unique_count)
        
        return new_l
