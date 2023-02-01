from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        stones_map = defaultdict(int)
        for stone in stones:
            stones_map[stone] += 1
        for jewel in jewels:
            answer += stones_map[jewel]
        return answer


sol = Solution()
print(sol.numJewelsInStones('z', 'ZZ'))

