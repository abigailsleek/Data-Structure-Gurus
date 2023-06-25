class Solution:
    def palindrome(self,s:str) -> bool:
        #first method that comes to mind is to 
        #revStr = ""
        
        #for char in s:
#             check for edge case of character not being alphanumeric
            #if char.isalnum():
                #revStr += char.lower()
        #return revStr == revStr[::-1]
        #second approach is to use two pointers
       
        # using two pointers; left pointer starts at index 0, 
        # right pointer starts at the last element
        left, right = 0, len(s) -1

        while left < right:

            # make sure both char at left and right are alphanumeric
            while left < right and not self.isalpha(s[left]):
                # increment left pointer
                left += 1
            while right > left and not self.isalpha(s[right]):
                # decrement right pointer
                right -= 1
                # catch edge case of the char not being in lower case
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        #  write a function to first check if 
        # the char is alphanumeric from capital A - Z and small a-z 
        # also check if it is a number from 0-9

    def isalpha(self, char):
        return (ord("A")<= ord(char) <= ord("Z") or
                ord("a")<= ord(char) <= ord("z") or
                ord("0")<= ord(char) <= ord("9"))
        
