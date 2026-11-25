from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

    
        mod1, base1 = 1_000_000_007, 131_542_391
        mod2, base2 = 1_000_000_009, 265_443_576_1

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            x = val + 1 
            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2
            h1[i + 1] = (h1[i] * base1 + x) % mod1
            h2[i + 1] = (h2[i] * base2 + x) % mod2

        def has_unique_of_len(length: int) -> bool:
            counts = Counter()
            pow1 = p1[length]
            pow2 = p2[length]

            for start in range(n - length + 1):
                end = start + length
                sub1 = (h1[end] - h1[start] * pow1) % mod1
                sub2 = (h2[end] - h2[start] * pow2) % mod2
                counts[(sub1, sub2)] += 1

            return any(freq == 1 for freq in counts.values())

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_len(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
