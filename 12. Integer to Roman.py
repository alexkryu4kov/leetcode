alphabet = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        answer = ''
        i = 0

        while num > 0:
            key = list(alphabet.keys())[i]
            if key <= num:
                answer += alphabet[key]
                num -= key
            else:
                i += 1
        return answer


sol = Solution()
print(sol.intToRoman(58))
