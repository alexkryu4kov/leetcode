from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = ['b', 'a', 'n']
        double_letters = ['l', 'o']
        counts = defaultdict(int)
        for letter in text:
            counts[letter] += 1
        l = []
        for elem in letters:
            l.append(counts[elem])
        for elem in double_letters:
            l.append(counts[elem] // 2)
        return min(l)


sol = Solution()
print(sol.maxNumberOfBalloons("loonbalxballpoon"))
