import itertools

mapping = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        lists = []
        # полный перебор, надо заменить на backtracking - а как?
        
        for digit in digits:
            lists.append([el for el in mapping[int(digit)]])
        combinations = list(itertools.product(*lists))
        return [''.join(elem) for elem in combinations]


sol = Solution()
print(sol.letterCombinations('23'))
