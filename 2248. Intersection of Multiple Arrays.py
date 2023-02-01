from collections import defaultdict
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = defaultdict(int)
        answer = []
        max_len = max((len(num) for num in nums))
        len_nums = len(nums)
        for i in range(max_len):
            for num in nums:
                try:
                    number = num[i]
                except IndexError:
                    continue
                counter[number] += 1
                if counter[number] == len_nums:
                    answer.append(number)
        return sorted(answer)


sol = Solution()
print(sol.intersection([[7,34,45,10,12,27,13],[27,21,45,10,12,13]]))
