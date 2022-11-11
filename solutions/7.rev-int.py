class Solution:
    def reverse(self, x: int) -> int:
        twoPwr31=2147483648
        while x%10==0 and x!=0:
            x=x//10
        if x==0 or x>=twoPwr31 or x<=-twoPwr31:
            return 0
        if x<0:
            output = str(x)[-1:0:-1]
            if -int(output)<=(twoPwr31*-1):
                return 0
            else:
                return "-"+output
        else:
            output = str(x)[::-1]
            if int(output)>=(twoPwr31-1):
                return 0
            else:
                return output
        