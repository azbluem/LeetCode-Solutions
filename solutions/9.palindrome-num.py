class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        string=str(x)
        for count in range(len(string)//2):
            if string[count]!=string[len(string)-1-count]:
                return False
        return True
        