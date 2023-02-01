from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        nums_len = len(nums)
        answer = float('inf')
        for index_i in range(nums_len - 2):
            first = index_i + 1
            last = nums_len - 1
            while first < last:
                sum_candidate = nums[index_i] + nums[first] + nums[last]
                if abs(target - sum_candidate) < abs(target - answer):
                    answer = sum_candidate
                if answer == target:
                    return answer
                elif sum_candidate < target:
                    first += 1
                else:
                    last -= 1
        return answer


sol = Solution()
print(sol.threeSumClosest([0, 0, 0], 1))
