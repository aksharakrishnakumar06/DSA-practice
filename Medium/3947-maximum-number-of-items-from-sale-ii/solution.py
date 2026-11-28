from collections import defaultdict
from typing import List


class Solution:

    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        min_price = min(p for _, p in items)

        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        mult_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] == 0:
                continue
            total_divisible = 0
            for m in range(f, max_f + 1, f):
                total_divisible += freq[m]
            mult_count[f] = total_divisible - 1

        gain_by_price = defaultdict(int)
        for f, p in items:
            gain = mult_count[f]
            if gain > 0 and p < 2 * min_price:
                gain_by_price[p] += gain

        total_items = 0
        for price in sorted(gain_by_price):
            if budget < price:
                break
            can_buy = min(gain_by_price[price], budget // price)
            total_items += can_buy * 2
            budget -= can_buy * price

        total_items += budget // min_price
        return total_items
