class Solution(object):

    def __init__(self):
        self.a = None
        self.b = None

    def addBinary(self, a, b):
        self.values_to_list(a, b)
        self.match_list()
        return self.perform_sum()

    def values_to_list(self, a, b):
        self.a = list(a)
        self.b = list(b)

    def match_list(self):
        size_diff = abs(len(self.a) - len(self.b))

        if size_diff != 0:
            if len(self.a) > len(self.b):
                self.b = list("0" * size_diff) + self.b

            elif len(self.a) < len(self.b):
                self.a = list("0" * size_diff) + self.a

    def perform_sum(self):
        result = list()
        carried_over = 0
        for i in range(len(self.a)):
            key = len(self.a) - i - 1
            added_sum = int(self.a[key]) + int(self.b[key]) + carried_over
            division_count = added_sum // 2
            remainder_count = added_sum % 2
            result.insert(0, remainder_count)
            carried_over = division_count

        if carried_over != 0:
            result.insert(0, carried_over)

        return ''.join(str(x) for x in result)


solution = Solution()
print(solution.addBinary('11', '1'))
print(solution.addBinary('1010', '1011'))


