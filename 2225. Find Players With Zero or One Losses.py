from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = defaultdict(int)
        wins = set(match[0] for match in matches)
        for win in wins:
            loses[win] = 0
        for match in matches:
            loses[match[1]] += 1
        answer = [[], []]
        for key, elem in loses.items():
            if elem == 0:
                answer[0].append(key)
            if elem == 1:
                answer[1].append(key)
        return [sorted(answer[0]), sorted(answer[1])]


sol = Solution()
print(sol.findWinners([[2,3],[1,3],[5,4],[6,4]]))
