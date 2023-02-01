class Solution(object):

    def find_numbers(self, candidates, target, index, temp, results):
        if target == 0:
            results.append(list(temp))
            return
        for i in range(index, len(candidates)):
            if (target - candidates[i]) >= 0:
                temp.append(candidates[i])
                self.find_numbers(candidates, target-candidates[i], i, temp, results)
                temp.remove(candidates[i])

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        results = []
        temp = []
        candidates = sorted(list(set(candidates)))
        self.find_numbers(candidates, target, 0, temp, results)
        return results


sol = Solution()
print(sol.combinationSum([2, 3, 5], 8))
