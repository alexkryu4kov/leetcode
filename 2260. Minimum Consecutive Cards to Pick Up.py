from collections import defaultdict
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hash_map = defaultdict(int)
        answer = float('inf')
        for index, card in enumerate(cards):
            if card in hash_map:
                answer = min(answer, index - hash_map[card] + 1)
            hash_map[card] = index
        return answer if answer != float('inf') else -1


sol = Solution()
print(sol.minimumCardPickup([1, 0, 5, 3]))
