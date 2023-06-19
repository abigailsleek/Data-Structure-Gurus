import string


class Solution(object):

    def __init__(self):
        self.s = None

    def isPalindrome(self, s):
        self.s = s
        self.stripNonAlphanumericCharacters()
        return self.checkIsPalindrome()

    def stripNonAlphanumericCharacters(self):
        exclude = set(string.punctuation)
        self.s = ''.join(ch for ch in self.s if ch not in exclude).lower().replace(" ", "")

    def checkIsPalindrome(self):
        for i in range(len(self.s)):
            key = len(self.s) - i - 1
            if self.s[key] != self.s[i]:
                return False
        return True


solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))
print(solution.isPalindrome('race a car'))
print(solution.isPalindrome(' '))
