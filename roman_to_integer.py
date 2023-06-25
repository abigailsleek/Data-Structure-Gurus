class Solution(object):
    roman_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def get_roman_value(self, roman_num):
        return self.roman_int[roman_num]

    def romanToInt(self, s):
        int_sum = 0
        for i in range(len(s)):
            previous_value = 0
            if len(s) > (i - 1) >= 0:
                previous_value = self.get_roman_value(s[i - 1])

            next_value = 0
            if len(s) > (i + 1):
                next_value = self.get_roman_value(s[i + 1])

            current_value = self.get_roman_value(s[i])
            sum_value = current_value

            if 0 < current_value < next_value:
                sum_value = next_value - current_value
            elif 0 < previous_value < current_value:
                sum_value = 0

            int_sum = int_sum + sum_value
        return int_sum


solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))
