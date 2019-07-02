class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        str1 = str(abs(x))
        str2 = str1[::-1]
        if str1 == str2:
            return True
        else:
            return False
        
