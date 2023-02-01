from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for key, value in d.items():
            if value == 1:
                return key
