alphabet = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


class Solution:
    def romanToInt(self, s: str) -> int:

        answer = 0
        list_s = list(s)
        i = 0
        while i < len(list_s):
            flag = 0
            try:
                if i+1 < len(list_s):
                    candidate = ''.join(list_s[i:i+2])
                    if candidate in alphabet:
                        answer += alphabet[candidate]
                        i += 2
                        flag = 1
            except IndexError:
                pass
            if flag == 0:
                answer += alphabet[list_s[i]]
                i += 1

        return answer


sol = Solution()
print(sol.romanToInt("MCMXCIV"))
