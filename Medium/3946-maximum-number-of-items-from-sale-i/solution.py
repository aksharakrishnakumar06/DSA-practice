from typing import List
from collections import Counter

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        factor_counts = Counter()
        for f, p in items:
            factor_counts[f] += 1

        free_copies_gain = []
        for f, p in items:
            divisible_count = 0
    
            for multiple in range(f, 1501, f):
                if multiple in factor_counts:
                    divisible_count += factor_counts[multiple]

            free_copies_gain.append(divisible_count - 1)

        dp = [0] * (budget + 1)
        
        for i in range(n):
            f, p = items[i]
            first_copy_gain = 1 + free_copies_gain[i]
            
            next_dp = list(dp)
            
        
            for b in range(budget - p, -1, -1):
                if dp[b] > 0 or b == 0:
                    next_dp[b + p] = max(next_dp[b + p], dp[b] + first_copy_gain)    
            for b in range(p, budget + 1):
                if next_dp[b - p] > 0:
                    next_dp[b] = max(next_dp[b], next_dp[b - p] + 1)
            
            dp = next_dp
            
        return max(dp)
