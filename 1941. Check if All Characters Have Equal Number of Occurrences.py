from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = defaultdict(int)
        for letter in s:
            counter[letter] += 1
        return len(set(counter.values())) == 1


sol = Solution()
print(sol.areOccurrencesEqual("aaabb"))
