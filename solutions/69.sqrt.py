class Solution:
    def mySqrt(self, x: int) -> int:
        target=0
        for i in range(1,x//2+2):
            if i*i<=x:
                target=i
            else:break
        return target