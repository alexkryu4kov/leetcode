class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        answer = 0
        arr_set = set(arr)
        for elem in arr:
            if elem+1 in arr_set:
                answer += 1

        return answer


sol = Solution()
print(sol.countElements([1,3,2,3,5,0]))
